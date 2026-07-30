# DevPilot AI - System Architecture

## Overview

DevPilot AI follows a modular architecture that separates the AI agent, tools, memory, services, and API into independent components. This structure makes the project maintainable, testable, and easy to extend with additional capabilities in the future.

The MVP is designed as a local-first engineering assistant that can understand project context, retrieve information, and generate engineering guidance without modifying source code.

---

# High-Level Architecture

```
                User
                  │
                  ▼
        ┌──────────────────┐
        │  CLI / FastAPI   │
        └──────────────────┘
                  │
                  ▼
        ┌──────────────────┐
        │   Agent Engine   │
        └──────────────────┘
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     Memory     Tools    Prompt Manager
        │         │
        ▼         ▼
 SQLite / FAISS   File System
                  Git Repository
                  Documentation
```

---

# Components

## Agent Engine

Responsibilities:

- Receive user requests
- Select the appropriate tools
- Build prompts
- Coordinate retrieval
- Generate responses

The Agent Engine is the central coordinator of the application.

---

## Prompt Manager

Responsibilities:

- Store system prompts
- Build user prompts
- Maintain prompt templates
- Standardize interactions with the LLM

---

## Tool Layer

Responsibilities:

- File search
- File reading
- Git history lookup
- Documentation lookup
- Future integrations

Each tool performs one specific task and returns structured results to the agent.

---

## Memory Layer

Responsibilities:

- Store project knowledge
- Store engineering decisions
- Retrieve relevant context
- Enable semantic search

The MVP will use SQLite for structured storage and FAISS with Sentence Transformers for semantic retrieval.

---

## Services Layer

Responsibilities:

- Business logic
- Context assembly
- Response generation
- Retrieval orchestration

Services isolate application logic from the agent and tools.

---

## Models

Responsibilities:

- Pydantic schemas
- Request models
- Response models
- Internal data structures

Using typed models improves reliability and validation.

---

## Configuration

Responsibilities:

- Environment variables
- Model configuration
- Application settings
- Path management

---

## API Layer

Responsibilities:

- HTTP endpoints
- Future frontend integration
- Health checks
- Agent request handling

FastAPI is selected because it is lightweight, asynchronous, and production-ready.

---

# Data Flow

1. User submits a request.
2. Agent analyzes the request.
3. Required tools are selected.
4. Relevant project context is retrieved.
5. Memory is searched.
6. Prompt is constructed.
7. LLM generates a response.
8. Response is validated.
9. Final answer is returned.

---

# Design Principles

- Modular architecture
- Single responsibility
- Local-first execution
- Tool-based reasoning
- Retrieval before generation
- Typed data models
- Safe-by-default behavior

---

# Future Extensions

The architecture supports future additions without major refactoring, including:

- Multi-agent collaboration
- IDE plugins
- GitHub integration
- Local LLMs
- Web search
- Documentation generation
- Code review automation
- Workflow automation