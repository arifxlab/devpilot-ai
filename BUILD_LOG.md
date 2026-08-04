# DevPilot AI – Build Log

## Project

DevPilot AI is a modular backend AI engineering assistant capable of understanding software projects using real tools before generating responses.

---

# Original Goal

Build an AI agent capable of:

- Understanding software projects
- Using real tools
- Reading project files
- Inspecting directory structures
- Producing grounded answers instead of hallucinating

---

# Iteration 1

Implemented the initial FastAPI application.

Completed:

- FastAPI backend
- Ollama provider
- Conversation memory
- Agent engine
- Basic routing

Issue:

The agent answered only from the language model and could not inspect projects.

Decision:

Introduce a tool system.

---

# Iteration 2

Built a modular Tool Registry.

Implemented:

- BaseTool
- Tool Registry
- Dynamic tool loading

Result:

Tools became independently extensible.

---

# Iteration 3

Implemented project inspection tools.

Added:

- Filesystem Tool
- Directory Tree Tool
- Read File Tool
- Project Scan Tool

Issue:

Only one tool could execute per request.

---

# Iteration 4

Introduced planning.

Implemented:

- Agent Planner

The planner detects which tools are required based on the user's request.

Result:

The system became capable of selecting tools automatically.

---

# Iteration 5

Implemented Multi Tool Execution.

Added:

- MultiToolExecutor

Now the agent can execute multiple tools before contacting the language model.

Example:

User:

Analyze my project and read README.md

Execution:

- Project Scan
- Directory Tree
- Read README

All execute before AI generation.

---

# Iteration 6

Implemented Context Builder.

Instead of sending raw tool output to the LLM, structured context is generated.

Benefits:

- Reduced hallucination
- Better reasoning
- Multiple tools combined into one prompt

---

# Iteration 7

Improved architecture.

Refactored responsibilities.

Planner:

Responsible only for deciding tools.

Executor:

Responsible only for execution.

Engine:

Responsible only for orchestration.

This reduced coupling and improved maintainability.

---

# Issues Encountered

## Import Problems

Issue:

Modules were moved during refactoring.

Resolution:

Updated imports and consolidated the executor into a single location.

---

## Executor Design

Issue:

Initially the executor expected a list of tasks while the engine supplied natural language.

Resolution:

Refactored executor to internally call the planner.

The engine now only passes the user request.

---

## Context Generation

Issue:

The model often focused on a single tool result.

Resolution:

Introduced structured context combining every tool output before inference.

---

# Current MVP

The completed MVP supports:

- AI conversation
- Conversation memory
- Automatic planning
- Multiple tool execution
- Project inspection
- File reading
- Directory analysis
- Grounded LLM responses

---

# Deviations from Initial Plan

Originally planned:

- Full MCP integration

Current implementation:

- Native project tools

Reason:

Delivering a stable end-to-end agent was prioritized for the MVP.

The architecture allows MCP servers to be integrated later without redesigning the system.

---

# Next Improvements

Planned after MVP:

- MCP support
- Semantic search
- Vector memory
- Plugin architecture
- Parallel tool execution
- Tool confidence scoring
- Better planning
- Production logging
- Docker deployment