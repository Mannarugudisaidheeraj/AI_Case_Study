# AI_Case_Study

# Draconic AI Case Study – Customer Support Ticket Analyzer

## Overview
This project demonstrates a multi-agent AI system using Pydantic for categorizing and routing customer support tickets.

### Agents
- **CategoryAgent** — Determines the category (bug, feature request, UI issue, security, etc.)
- **RoutingAgent** — Routes tickets to the right team (backend, frontend, security, priority support, general)

---

## Architecture
The system uses a multi-agent approach:
- The Category Agent analyzes subject/message.
- The Routing Agent uses category and customer tier to decide the routing team.

---

## Evaluation
Evaluates results across five test cases:
- Prints category and routing decisions.
- Placeholder for accuracy and agreement metrics.

---

## Getting Started
**Install Dependencies**:
```bash
pip install pydantic
