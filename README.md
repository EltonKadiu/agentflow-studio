#  AgentFlow Studio

AgentFlow Studio is an autonomous AI code refactoring and documentation pipeline built to modernize legacy codebases. Submitted for the **Coding and Agentic Engineering** track (also competing for the **Best Use of Tavily** prize).

## The Pipeline
Our agentic workflow operates in four distinct, sequential steps:
1. Search: Retrieves real-time documentation, syntax updates, and best practices using the "Tavily Search API".
2. Audit: Analyzes legacy code for anti-patterns, security flaws, and performance bottlenecks.
3. Refactor: Restructures and modernizes the code using open-source LLMs via "Nebius Token Factory".
4. Tests: Automatically generates comprehensive, modern unit tests to verify the refactored code.

##  Key Features
- Real-Time Context Retrieval: Powered by "Tavily" to fetch current library versions and best practices.
- Autonomous Refactoring Pipeline: Structured 4-step pipeline (Search -> Audit -> Refactor -> Tests).
- High-Throughput LLM Inference: Employs open-source AI models via "Nebius Token Factory" (nvidia/Nemotron-3_5-Lightning).
- Interactive UI & Backend: Simple interface built with "Streamlit and a fast FastAPI backend.

##  Built With
- nebius (Nebius Token Factory)
- tavily (Tavily Search API)
- nvidia / nemotron (`nvidia/Nemotron-3_5-Lightning`)
- python
- fastapi
- streamlit

##  Challenges & Solutions
During development, we encountered endpoint configuration hurdles and strict model naming requirements when integrating with the "Nebius Token Factory" (specifically handling precise identifiers like "nvidia/Nemotron-3_5-Lightning"). We resolved this by implementing custom wrapper handlers with robust error logging and environment fallback checks to maintain seamless, high-throughput inference stability.

