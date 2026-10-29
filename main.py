import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from openai import OpenAI
from tavily import TavilyClient

load_dotenv()
app = FastAPI()

MODEL = os.getenv("NEBIUS_MODEL")
llm = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_API_KEY"),
)
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def ask(system: str, user: str) -> str:
    resp = llm.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=0.2,
    )
    return resp.choices[0].message.content


@app.post("/process")
def process_code(data: dict):
    code = data.get("code", "")
    query = data.get("query", "python best practices")
    if not MODEL:
        raise HTTPException(500, "NEBIUS_MODEL is missing in .env")
    try:
        # Agent 1: live documentation search (Tavily)
        try:
            res = tavily.search(query=query, search_depth="basic", max_results=3)
            sources = [{"title": r["title"], "url": r["url"], "content": r["content"]}
                       for r in res.get("results", [])]
        except Exception:
            sources = []
        docs = "\n".join(s["content"] for s in sources)

        # Agent 2: auditor
        audit = ask("You are a strict code reviewer. List bugs, security issues and "
                    "outdated patterns as short bullet points.",
                    f"Docs:\n{docs}\n\nCode:\n{code}")

        # Agent 3: refactorer
        refactored = ask("You are a senior engineer. Rewrite the code to fix the issues. "
                         "Return only the code in one code block, then a short explanation.",
                         f"Issues:\n{audit}\n\nDocs:\n{docs}\n\nCode:\n{code}")

        # Agent 4: test writer
        tests = ask("You write pytest unit tests. Return only a code block.",
                    f"Write tests for this code:\n{refactored}")

        return {"audit": audit, "refactored": refactored, "tests": tests, "sources": sources}
    except Exception as e:
        raise HTTPException(500, f"{type(e).__name__}: {e}")