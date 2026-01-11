from dotenv import load_dotenv
load_dotenv()  # Loads GEMINI_API_KEY from .env

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from services.document_loader import load_contract
from services.agent_graph import analyze_with_agents

app = FastAPI(
    title="AI Contract Analyzer",
    description="AI tool to read and analyze legal contracts automatically using multi-agent planning",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "AI Contract Analyzer is running"}


@app.post("/upload")
async def upload_contract(file: UploadFile = File(...)):
    """
    Upload a contract PDF and extract raw text
    """
    try:
        text = load_contract(file)
        return {
            "characters_extracted": len(text),
            "text_preview": text[:500]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/analyze")
async def analyze_contract_endpoint(file: UploadFile = File(...)):
    """
    Upload a contract PDF → Planner → LangGraph → Agents
    """
    try:
        # Load contract text
        text = load_contract(file)

        # Run planner + multi-agent graph
        analysis_result = analyze_with_agents(text)

        return analysis_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
