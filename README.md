# ⚖️ AI Contract Analyzer

A professional AI-powered tool to analyze legal contracts using Multi-Agent systems.

## 📋 Prerequisites
- **Python 3.10+** must be installed on the system.

## 🚀 Setup Instructions

### 1. Unzip the Project
Extract the zip file to a folder on your computer.

### 2. Set up the Environment
It is recommended to create a virtual environment first.

**Using default Python venv:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
Install all required libraries for both backend and frontend.

```powershell
pip install -r frontend/requirements.txt
pip install -r backend/requirements.txt
```

### 4. Configure API Key
1.  Open `backend/.env` file.
2.  Add your Google Gemini API Key:
    ```
    GEMINI_API_KEY="your_api_key_here"
    ```

---

## ▶️ How to Run

You need to run the **Backend** and **Frontend** in two separate terminals.

### Terminal 1: Backend (FastAPI)
```powershell
cd INFOSYS/backend
uvicorn app.main:app --reload
```
*You should see "Uvicorn running on http://127.0.0.1:8000"*

### Terminal 2: Frontend (Streamlit)
```powershell
cd INFOSYS/frontend
streamlit run app.py
```
*The app will automatically open in your browser at http://localhost:8501*

---

## ✨ Features
- **Legal Risk Analysis**: Identifies risky clauses.
- **Compliance Check**: GDPR and regulatory checks.
- **Session History**: Tracks analyzed files in the current session.
- **Premium UI**: Light/Dark theme support with professional styling.
