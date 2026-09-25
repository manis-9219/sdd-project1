# Quickstart Validation: dbt Metadata Data Dictionary

## Prerequisites

- Python 3.13.3 available through the project virtual environment.
- A local dbt `manifest.json` containing zero or more `semantic_models` and
  `metrics` records.
- The project dependencies installed in `.venv`. The feature itself requires
  only the Python standard library.

## Run the Automated Checks

From the repository root:

```text
.venv/bin/python -m unittest discover -s tests -v
```

Expected result: all parser, renderer, and CLI tests pass, including malformed
input, missing metadata, deterministic output, and file error scenarios.

## Generate to Standard Output

```text
.venv/bin/python -m dbt_metadata_dictionary path/to/manifest.json
```

Expected result: a Markdown document appears on standard output with separate
semantic-model and metric sections.

## Generate to a File

```text
.venv/bin/python -m dbt_metadata_dictionary \
  path/to/manifest.json \
  --output docs/data-dictionary.md
```

Expected result: the complete Markdown document is written to the requested
path, the command exits successfully, and the source manifest is unchanged.

## Check Help

```text
.venv/bin/python -m dbt_metadata_dictionary --help
```

Expected result: help identifies the manifest argument, the optional output
argument, Markdown output, and error behavior.

## Validate Failure Behavior

Run the command with a missing path and with a malformed JSON fixture.

Expected result for each case:

- The command exits with a non-zero status.
- A concise actionable message is written to standard error.
- No partial output file is created or overwritten.

## Quality Gates

Before review, run the repository's configured formatting, import organization,
strict type-checking, and test commands. The implementation must use the
standard library only unless a reviewed exception is documented.
