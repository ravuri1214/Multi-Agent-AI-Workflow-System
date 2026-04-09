# Multi-Agent-AI-Workflow-System

# Multi-Agent AI Workflow System

## Overview

This project demonstrates a simple multi-agent workflow for handling complex tasks by separating them into planning, execution, and validation stages.

## Problem

Single-step prompts often fail on multi-step tasks because they do not explicitly separate reasoning, execution, and verification.

## Solution

This system breaks a user request into smaller workflow steps using three components:

* Planner
* Executor
* Validator

## Workflow

1. Planner interprets the input request
2. Executor processes each step
3. Validator checks whether the workflow completed successfully

## Project Structure

* `planner.py` → creates task steps
* `executor.py` → executes each step
* `validator.py` → validates the result
* `main.py` → connects all workflow stages

## Example Run

Input:
`Summarize customer support issues`

Output:

* Completed: Understand the request
* Completed: Break the task into smaller steps
* Completed: Prepare a structured response

## Results / Observations

* Demonstrates modular workflow design
* Improves clarity over a single-step prompt approach
* Makes debugging easier by separating workflow stages

## Future Improvements

* Replace rule-based steps with LLM-based planning
* Add structured outputs using JSON
* Add logging and API deployment
