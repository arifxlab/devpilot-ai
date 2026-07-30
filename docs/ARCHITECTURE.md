# DevPilot AI Architecture

## Overview

DevPilot AI is a modular AI agent system designed around three main principles:

1. Separation of responsibilities
2. Extensible tools
3. Replaceable AI providers

The architecture allows new capabilities to be added without rewriting the core agent.

---

# High-Level Architecture

            User
             |
             v
      FastAPI Application
             |
             v
      Agent Service Layer
             |
             v
        Agent Engine
             |
  +----------+----------+
  |                     |
  v                     v

Tool Registry AI Provider
|
|
+----+----------------+
| | |
v v v
Filesystem Read File Directory Tree


---

# Core Components

## API Layer

Location:


app/main.py
app/api/


Responsibility:

- Receive user requests
- Validate input
- Return agent responses

The API layer does not contain business logic.

---

# Agent Engine

Location:


app/agent/engine.py


Responsibility:

- Coordinate the agent workflow
- Manage prompts
- Decide whether to use tools or providers
- Return structured responses

The engine acts as the central orchestrator.

---

# Tool System

Location:


app/tools/


The tool system follows a registry pattern.

Each tool:

- Has a unique name
- Has a description
- Implements execution logic
- Returns structured output

Current tools:

## Filesystem Tool

Provides:

- Directory inspection
- File discovery

---

## Read File Tool

Provides:

- Safe file reading
- File metadata

---

## Directory Tree Tool

Provides:

- Project visualization
- Structure understanding

---

# Tool Registry

Location:


app/tools/registry.py


The registry provides dynamic tool management.

Benefits:

- Adding tools does not require engine changes.
- Tools remain independent.
- Future integrations are easier.

Future tools:

- Git analysis
- Code search
- Documentation generation
- Semantic retrieval

---

# Memory Layer

Location:


app/memory/


The memory layer abstracts how the agent stores information.

Current implementation:

- In-memory storage

Future implementations:

- PostgreSQL
- Redis
- Vector databases

---

# Provider Abstraction

Location:


app/agent/provider.py


The provider layer isolates the agent from a specific LLM.

Possible providers:

- OpenAI
- Claude
- Gemini
- Ollama
- Local models

This allows changing models without changing application logic.

---

# Design Decisions

## Why FastAPI?

FastAPI provides:

- Async support
- Automatic documentation
- Strong validation
- Production-ready API development

---

## Why Tool Registry Pattern?

Agents evolve over time.

A registry allows adding capabilities without modifying existing orchestration logic.

---

## Why Read-Only Tools Initially?

Safety.

The first version focuses on understanding projects rather than modifying them.

This reduces risk and makes evaluation easier.

---

# Current Limitations

The current prototype does not include:

- Persistent memory
- Real LLM providers
- Semantic retrieval
- Authentication
- Multi-user support

These are planned improvements.