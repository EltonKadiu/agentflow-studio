import requests
import streamlit as st

st.set_page_config(page_title="AgentFlow Studio", layout="wide")
st.title("⚡ AgentFlow Studio")
st.write("Multi-agent code refactoring on Nebius Token Factory (NVIDIA Nemotron) + Tavily search")

code_input = st.text_area("Paste legacy / messy code:", height=250)
query_input = st.text_input("Library / framework context:", "Python best practices")

if st.button("Run AI Refactor"):
    if not code_input.strip():
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Agents are searching docs, auditing, refactoring, writing tests..."):
            try:
                res = requests.post("http://127.0.0.1:8000/process",
                                    json={"code": code_input, "query": query_input},
                                    timeout=300)
            except requests.exceptions.ConnectionError:
                st.error("Backend is not running. Start it in the other window first.")
                st.stop()
        if res.status_code != 200:
            st.error(f"Backend error: {res.text}")
        else:
            d = res.json()
            st.success("Done!")
            st.subheader("1. Audit"); st.markdown(d["audit"])
            st.subheader("2. Refactored code"); st.markdown(d["refactored"])
            st.subheader("3. Unit tests"); st.markdown(d["tests"])
            st.subheader("Sources found by Tavily")
            for s in d["sources"]:
                st.markdown(f"- [{s['title']}]({s['url']})")