# Implementation Plan: dbt Metadata Data Dictionary

**Branch**: `001-dbt-metadata-dictionary` | **Date**: 2026-09-25 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/001-dbt-metadata-dictionary/spec.md`

## Summary

Build a local command-line utility that reads a dbt `manifest.json`, extracts
supported `semantic_models` and `metrics` metadata, and renders deterministic
Markdown tables. The implementation uses Python 3.13's standard library only,
with a small typed parsing and rendering core exposed through an `argparse`
command-line entry point.

## Technical Context

**Language/Version**: Python 3.13.3; support the project's declared Python 3.13 baseline

**Primary Dependencies**: Python standard library only (`argparse`, `json`, `pathlib`, `dataclasses`, `typing`)

**Storage**: Local input and output files; no persistent storage

**Testing**: `unittest` with temporary directories and in-memory fixtures

**Target Platform**: Local macOS, Linux, and Windows environments with the supported Python version

**Project Type**: Command-line utility with importable library modules

**Performance Goals**: Generate output for at least 25 supported records in under 2 seconds on a typical development laptop

**Constraints**: Offline-capable, standard-library-only, strict type checking, PEP 8 formatting, deterministic output, and no mutation of the input manifest

**Scale/Scope**: Local documentation generation for a single manifest per invocation; semantic models and metrics only; no remote sources or publishing integrations

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Standard Library First**: PASS. No third-party runtime or test dependencies are planned.
- **PEP 8 Code Quality**: PASS. Source and tests will use four-space indentation and 79-character lines, with automated checks documented in the quickstart.
- **Strict Static Typing**: PASS. Public interfaces and non-obvious fields will be annotated and checked in strict mode.
- **Tests and Documentation**: PASS. Unit tests, CLI validation scenarios, and usage documentation are part of the design.
- **Explicit Versioning and Review**: PASS. The CLI contract will document behavior changes, and the feature requires review before integration.
- **Engineering Constraints**: PASS. The design is reproducible in the existing virtual environment and introduces no external service dependency.

## Project Structure

### Documentation (this feature)

```text
specs/001-dbt-metadata-dictionary/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── cli.md
└── tasks.md              # Created by /speckit-tasks
```

### Source Code (repository root)

```text
src/
└── dbt_metadata_dictionary/
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    ├── errors.py
    ├── models.py
    ├── parser.py
    └── renderer.py

tests/
├── fixtures/
│   ├── manifest_complete.json
│   ├── manifest_empty.json
│   └── manifest_invalid.json
├── test_cli.py
├── test_parser.py
└── test_renderer.py
```

**Structure Decision**: Use a small `src` package with separate typed models,
parsing, rendering, and CLI boundaries. Keep tests divided by those public
behaviors and use fixture files for representative manifest shapes.

## Complexity Tracking

No constitution violations require justification.
