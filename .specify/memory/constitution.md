<!--
Sync Impact Report
Version change: template -> 1.0.0
Modified principles: five template placeholders replaced with strict Python project rules
Added sections: Engineering Constraints; Development Workflow
Removed sections: none
Follow-up TODOs: Confirm the original ratification date.
-->

# Strict Python Project Constitution

## Core Principles

### I. Standard Library First
The Python standard library MUST be preferred for functionality it provides
adequately. A third-party dependency MUST have a documented benefit that
justifies its installation, maintenance, security, and supply-chain cost.

### II. PEP 8 Code Quality
All Python source code MUST follow PEP 8, use four-space indentation, and keep
lines at 79 characters or fewer unless a documented exception is necessary.
Formatting and import organization MUST be checked automatically.

### III. Strict Static Typing
All public functions, methods, parameters, return values, and non-obvious
module or class attributes MUST have type annotations. Static type checking
MUST run in strict mode, and new type errors MUST be resolved before merge.

### IV. Tests and Documentation
Every behavior change MUST include automated tests at the appropriate level.
Public APIs and non-obvious implementation decisions MUST be documented.
Tests MUST be deterministic, repeatable, and runnable without undeclared
external services.

### V. Explicit Versioning and Review
Changes to public behavior MUST follow semantic versioning. Breaking changes
MUST be identified and documented. Every change MUST receive code review before
integration, and reviewers MUST verify compliance with this constitution.

## Engineering Constraints

The project MUST target a supported Python version declared by the project.
Dependencies MUST be pinned or constrained through the chosen project
configuration, and dependency additions MUST include a rationale. Configuration,
linting, formatting, type checking, and test commands MUST be reproducible in a
clean virtual environment.

## Development Workflow

Each change MUST pass formatting, import organization, strict type checking,
and the automated test suite before review approval. Reviewers MUST reject
untyped public interfaces, unexplained dependencies, PEP 8 violations, missing
tests for changed behavior, and undocumented breaking changes. Exceptions MUST
be recorded in the change description with their rationale and follow-up plan.

## Governance

This constitution is the highest-level development policy for the project.
When another document conflicts with it, this constitution takes precedence.
Amendments MUST be proposed in a reviewed change, state their rationale and
impact, and update the version and amendment date. Version changes follow
semantic versioning: MAJOR for incompatible governance changes, MINOR for new
principles or materially expanded requirements, and PATCH for clarifications.
The constitution MUST be reviewed for compliance during every code review.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): confirm original adoption date | **Last Amended**: 2026-09-25
