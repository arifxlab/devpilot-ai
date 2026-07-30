# DevPilot AI - Pre-Build Evaluation Plan

## Purpose

Evaluation is defined before implementation to ensure the agent is measured against real engineering tasks rather than subjective impressions. Each evaluation verifies that the agent retrieves project information accurately, follows instructions, and avoids hallucinations.

---

# Evaluation Criteria

The agent will be evaluated on:

- Correctness
- Retrieval accuracy
- Completeness
- Instruction following
- Safety
- Consistency

Each evaluation is graded as:

- PASS
- PARTIAL
- FAIL

---

# Evaluation Case 1

## Goal

Verify project understanding.

### Prompt

> What does this project do?

### Expected Result

- Reads the README.
- Produces a concise summary.
- Does not invent features.

### Failure Conditions

- Hallucinates functionality.
- Ignores project documentation.

---

# Evaluation Case 2

## Goal

Verify code retrieval.

### Prompt

> Where is authentication implemented?

### Expected Result

- Searches project files.
- Returns the correct file paths.
- Explains the implementation.

### Failure Conditions

- References nonexistent files.
- Misses the correct implementation.

---

# Evaluation Case 3

## Goal

Verify implementation planning.

### Prompt

> Create an implementation plan for JWT refresh tokens.

### Expected Result

- Produces a step-by-step engineering plan.
- Identifies affected modules.
- Lists dependencies.

### Failure Conditions

- Generates vague advice.
- Omits key implementation steps.

---

# Evaluation Case 4

## Goal

Verify architectural reasoning.

### Prompt

> Explain the project architecture.

### Expected Result

- Uses available documentation.
- Describes modules and responsibilities.
- Explains component interactions.

### Failure Conditions

- Incorrect architecture description.
- Missing major components.

---

# Evaluation Case 5

## Goal

Verify engineering recommendations.

### Prompt

> What should I build next?

### Expected Result

- Reviews project context.
- Suggests logical next tasks.
- Prioritizes work clearly.

### Failure Conditions

- Generic or unrelated recommendations.
- Suggestions unsupported by project context.

---

# Evaluation Case 6

## Goal

Verify memory retrieval.

### Prompt

> What important decisions have already been made?

### Expected Result

- Retrieves stored project memory.
- Summarizes previous engineering decisions.
- Avoids duplication.

### Failure Conditions

- Ignores stored memory.
- Fabricates previous decisions.

---

# Success Metrics

The MVP is considered successful if:

- At least 5 of 6 evaluations pass.
- No critical hallucinations occur.
- No destructive actions are performed.
- Retrieval-based answers are preferred over generated assumptions.

---

# Future Evaluations

Future versions will include:

- Multi-file reasoning
- Git history analysis
- Large repository indexing
- Tool selection accuracy
- Long-term memory consistency
- Multi-turn conversation evaluation