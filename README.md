# ⚖️ AI Contract Analyzer using OCR

> AI-powered legal document intelligence platform that extracts, analyzes, and summarizes contracts using OCR, Natural Language Processing, and automated risk detection.

---

## 🚀 Overview

AI Contract Analyzer is an intelligent document processing system designed to automate legal contract review.

The platform extracts text from scanned contracts and PDF documents using OCR, processes legal clauses through NLP pipelines, and generates structured insights that help users quickly understand obligations, risks, terms, and critical contract information.

Instead of manually reviewing lengthy legal documents, users can upload a contract and receive AI-generated analysis within seconds.

---

## 🎯 Problem Statement

Contract review is often:

* Time-consuming
* Error-prone
* Expensive
* Difficult for non-legal users

Organizations frequently deal with:

* Vendor agreements
* Employment contracts
* NDAs
* Service-level agreements
* Procurement documents

Manually identifying important clauses such as payment terms, termination conditions, liabilities, confidentiality agreements, and penalties can take hours.

This project automates that workflow using Artificial Intelligence and Optical Character Recognition.

---

## 💡 Key Features

### 📄 OCR-Based Document Extraction

Extracts text from:

* Scanned PDFs
* Image-based contracts
* Legal document screenshots

### 🤖 AI-Powered Contract Analysis

Automatically identifies:

* Parties involved
* Contract duration
* Payment terms
* Termination clauses
* Liability clauses
* Confidentiality agreements
* Obligations and responsibilities

### ⚠️ Risk Detection

Highlights potentially risky clauses such as:

* Unlimited liability
* Auto-renewal conditions
* Hidden penalties
* Ambiguous obligations

### 📊 Structured Insights

Converts unstructured legal documents into:

* Summaries
* Key points
* Risk reports
* Actionable recommendations

### 🔍 Searchable Analysis

Enables quick navigation across extracted contract information.

---

## 🏗️ System Architecture

```text
                ┌─────────────────────┐
                │ Contract Upload     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ OCR Processing      │
                │ Text Extraction     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ NLP Pipeline        │
                │ Clause Detection    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Risk Analysis       │
                │ Classification      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ AI Insights Engine  │
                │ Summary Generation  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ User Dashboard      │
                └─────────────────────┘
```

---

## 🛠️ Technology Stack

### Backend

* Python
* Flask

### Artificial Intelligence

* Natural Language Processing (NLP)
* OCR Engine
* Text Classification
* Clause Extraction

### Frontend

* HTML
* CSS
* JavaScript

### Database

* SQLite

### Development Tools

* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```bash
AI-CONTRACT-ANALYSER-USING-OCR/
│
├── app/
│   ├── routes/
│   ├── models/
│   ├── templates/
│   ├── static/
│
├── uploads/
├── database/
├── requirements.txt
├── run.py
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/AxArjun/AI-CONTRACT-ANALYSER-USING-OCR.git
cd AI-CONTRACT-ANALYSER-USING-OCR
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python run.py
```

---

## 📈 Potential Use Cases

### Legal Teams

Accelerate contract review workflows.

### Startups

Understand agreements before signing.

### Procurement Departments

Analyze vendor contracts.

### HR Teams

Review employment agreements.

### Enterprises

Automate large-scale document intelligence pipelines.

---

## 🔮 Future Enhancements

* LLM-based legal reasoning
* Multi-agent contract review
* RAG-powered legal knowledge retrieval
* Contract comparison engine
* Compliance validation
* Cloud deployment
* Role-based dashboards
* Real-time collaboration

---

## 📊 Engineering Highlights

* OCR-based text extraction pipeline
* Automated clause identification
* AI-driven risk assessment
* Modular Flask architecture
* Scalable document processing workflow
* End-to-end legal document intelligence system

---

## 👨‍💻 Author

**Arjun R K**

GitHub: https://github.com/AxArjun

---

## 📜 License

This project is licensed under the MIT License.
