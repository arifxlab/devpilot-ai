# DevPilot AI

A modular AI engineering assistant capable of understanding software projects using real tools instead of relying solely on LLM reasoning.

---

## Features

- Rule-based agent planner
- Multi-tool execution
- Project scanner
- Directory tree inspection
- File reader
- Context builder
- Conversation memory
- Ollama integration
- FastAPI REST API

---

## Architecture

User
      │
      ▼
FastAPI
      │
      ▼
Agent Engine
      │
      ▼
Agent Planner
      │
      ▼
Multi Tool Executor
      │
      ▼
Registered Tools
      │
      ├── Project Scan
      ├── Directory Tree
      ├── Read File
      └── Filesystem

      │
      ▼
Context Builder
      │
      ▼
LLM Provider (Ollama)
      │
      ▼
Response

---

## Current Tools

- Project Scanner
- Directory Tree
- Filesystem
- Read File

---

## Technology Stack

- Python 3.11+
- FastAPI
- Ollama
- Pydantic
- Typer
- SQLAlchemy
- Sentence Transformers

---

## Installation

```bash
git clone https://github.com/<your-username>/devpilot-ai.git

cd devpilot-ai

python -m venv .venv

.venv\Scripts\activate

pip install -e .