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

##  Setup & Running the Project

Follow these step-by-step instructions to get AgentFlow Studio up and running locally on your machine.

Prerequisites
* **Python 3.10+** installed
* API keys for **Nebius** and **Tavily**


### Step 1: Clone the Repository & Setup Environment

Open your command prompt or terminal and run:

1. Clone the repository
git clone [https://github.com/EltonKadiu/agentflow-studio.git](https://github.com/EltonKadiu/agentflow-studio.git)

2. Install required dependencies
pip install -r requirements.txt


### Step 2: Configure Environment Variables
Create a file named .env in the root folder (Desktop\agentflow-studio) and add your API keys:

Code snippet

NEBIUS_API_KEY=your_nebius_api_key_here

TAVILY_API_KEY=your_tavily_api_key_here


### Step 3: Run the Application (Requires 2 Terminal Windows)
To run the full stack (FastAPI backend + Streamlit frontend), open two separate Command Prompt / Terminal windows:

Window 1: Start the Backend (FastAPI)

Open the first window and execute:

cd Desktop\agentflow-studio

python -m uvicorn main:app --reload

Note: Wait until you see the log output: Application startup complete. before proceeding to the next window.

Window 2: Start the Frontend (Streamlit)

Open a second window and execute:

cd Desktop\agentflow-studio

python -m streamlit run app.py

Once both commands are running, Streamlit will automatically open your web browser at http://localhost:8501.
