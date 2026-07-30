# FlyRank AI Submission

## Project

# DevPilot AI — Personal Software Engineering Assistant

---

# Problem Statement

Software engineers frequently work with unfamiliar or complex codebases.

Understanding project structure, locating important files, and gaining context before making changes can consume significant development time.

DevPilot AI solves this problem by creating an AI agent that can interact with a software project through controlled tools and provide context-aware assistance.

---

# Agent Goal

The goal of DevPilot AI is:

> Help developers understand and navigate software projects by combining natural language interaction with safe project inspection tools.

The agent focuses on one core job:

**Software project understanding.**

---

# Why an Agent?

A traditional chatbot only answers based on its training data.

DevPilot AI uses an agent approach because it can:

- Understand user intent
- Decide when additional project information is needed
- Use tools to retrieve relevant context
- Provide grounded responses

The combination of:

- Model
- Tools
- Instructions

creates a more useful engineering assistant.

---

# Technical Approach

## Architecture

The system consists of:


User
|
FastAPI API
|
Agent Engine
|
+----------------+
| |
Tools Provider
|
+----------------+
|
Project Files


---

# Implemented Capabilities

## Filesystem Inspection

Allows the agent to understand project organization.

Capabilities:

- List directories
- Discover files
- Validate paths

---

## File Understanding

Allows the agent to inspect source code and documentation.

Capabilities:

- Read files safely
- Return structured metadata
- Handle invalid resources

---

## Directory Visualization

Allows developers to quickly understand repository structure.

---

# Technology Stack

## Backend

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn

## Architecture

- Agent Engine
- Tool Registry Pattern
- Provider Abstraction
- Memory Abstraction

## Testing

- Pytest
- AnyIO

---

# Evaluation Strategy

The agent was evaluated using predefined scenarios:

## 1. Project Understanding

The agent should retrieve and explain project structure.

Result:

PASS

---

## 2. File Analysis

The agent should read files and provide grounded explanations.

Result:

PASS

---

## 3. Missing Resources

The agent should handle unavailable files without hallucinating.

Result:

PASS

---

## 4. Tool Failures

The agent should return meaningful errors.

Result:

PASS

---

## 5. Safety Behavior

The agent should reject destructive operations.

Result:

PASS

---

# Safety and Guardrails

The agent follows these restrictions:

- No file modification
- No destructive operations
- No command execution
- File size limitations
- Explicit tool boundaries

The first version intentionally focuses on safe read-only capabilities.

---

# Platform Decision

## Selected Platform

Custom scripted agent using Python.

## Reason

A custom implementation provides:

- Full architectural control
- Custom tool development
- Provider flexibility
- Better demonstration of engineering ability

Compared with hosted agent platforms, this approach provides greater control over the complete system design.

---

# Future Improvements

Future versions will include:

- Real LLM integrations
- Persistent memory
- Semantic code search
- Vector databases
- Git integration
- MCP support
- Multi-agent workflows

---

# Final Outcome

DevPilot AI demonstrates how a practical AI agent can be designed using:

- Clear scope
- Controlled tools
- Modular architecture
- Evaluation-driven development

The project establishes the foundation for a production-grade AI engineering 