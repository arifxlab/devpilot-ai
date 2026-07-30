# DevPilot AI - Personal Engineering Assistant

## Project Overview

DevPilot AI is a personal AI engineering assistant designed to improve software development productivity by helping developers understand projects, navigate codebases, answer technical questions, generate implementation plans, and review architecture. Rather than acting as a general-purpose chatbot, the agent focuses on a single job: assisting with engineering workflows throughout the software development lifecycle.

The initial version is intentionally scoped to a small, achievable feature set that can be completed within approximately ten hours while remaining extensible for future improvements.

---

# Job To Be Done

Software engineers frequently lose time switching between documentation, source code, Git history, and AI assistants.

DevPilot AI provides one unified assistant capable of:

- Understanding project context
- Searching source code
- Reading documentation
- Answering engineering questions
- Generating implementation plans
- Maintaining project memory

Instead of replacing the developer, the agent accelerates routine engineering tasks while keeping the human responsible for all final decisions.

---

# Primary User

The primary user is an individual software engineer working on personal or professional software projects.

The first version is optimized for:

- Backend Engineers
- Full Stack Developers
- AI Engineers
- Students building portfolio projects

---

# Usage Frequency

Expected usage:

- Multiple times per development session
- Before implementing new features
- During debugging
- During project planning
- While reviewing architecture
- Before committing code

---

# Core Responsibilities

The agent should be able to:

1. Answer engineering questions about a project.
2. Search files and documentation.
3. Explain architecture.
4. Generate implementation plans.
5. Remember previous project context.
6. Recommend next engineering tasks.

The agent intentionally does **not** modify code automatically.

---

# Required Tools

## File Search

Purpose:

Locate files relevant to a user's question.

Access Plan:

Python pathlib.

---

## File Reader

Purpose:

Read project files.

Access Plan:

Python standard library.

---

## Memory Store

Purpose:

Store important project knowledge.

Access Plan:

SQLite database.

---

## Embedding Search

Purpose:

Semantic retrieval over stored notes.

Access Plan:

Sentence Transformers with FAISS.

---

## Git Integration

Purpose:

Read Git history.

Access Plan:

GitPython.

---

# Data Sources

The agent can access:

- Source code
- Markdown documentation
- README files
- Configuration files
- Local memory database
- Git repository

The first version intentionally excludes:

- Cloud storage
- Email
- Calendar
- Browser automation

---

# Draft System Instructions

The assistant should:

- Answer only using available project context.
- Prefer project documentation over assumptions.
- Explain reasoning clearly.
- Recommend safe engineering practices.
- Ask for clarification when context is missing.
- Never fabricate project information.

---

# Evaluation Cases

## Evaluation 1

Question:

"What does this project do?"

Expected Result:

Correct summary generated from README.

---

## Evaluation 2

Question:

"Where is authentication implemented?"

Expected Result:

Locate relevant files.

---

## Evaluation 3

Question:

"Create an implementation plan for JWT refresh tokens."

Expected Result:

Structured engineering plan.

---

## Evaluation 4

Question:

"Explain the architecture."

Expected Result:

Correct explanation using documentation.

---

## Evaluation 5

Question:

"What should I work on next?"

Expected Result:

Recommend logical next engineering tasks based on project context.

---

# Risks

Potential risks include:

- Hallucinating project information
- Outdated memory
- Incorrect code interpretation
- Missing files

---

# Guardrails

The agent must:

- Never invent files.
- Never claim code exists unless found.
- Never modify source code automatically.
- Always ask before destructive actions.
- Clearly distinguish facts from suggestions.
- Prefer retrieval over generation whenever possible.

---

# Build Platform

Platform Selected:

**Python Scripted Agent**

Justification:

A scripted Python agent offers maximum flexibility, runs entirely locally, integrates easily with engineering tools, and requires no paid subscriptions. It also provides production-quality architecture suitable for future extension into APIs, IDE integrations, and multi-agent workflows.

Alternative Considered:

Custom GPT

Reason not selected:

Although easier to configure, it depends on a paid platform, provides limited control over tools and architecture, and is less suitable as a portfolio-quality software engineering project.

---

# Future Enhancements

- Multi-agent workflows
- IDE integration
- GitHub integration
- Documentation generation
- Pull request reviews
- Local LLM support
- Voice interaction

---

# Estimated Development Time

Approximately 10 hours for the initial MVP.