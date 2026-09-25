# CLI Contract: dbt Metadata Data Dictionary

## Invocation

```text
python -m dbt_metadata_dictionary INPUT_MANIFEST [--output OUTPUT_PATH]
```

The command reads one local dbt `manifest.json` path. `--output` is optional.
When omitted, Markdown is emitted to standard output. When supplied, the
command writes the complete Markdown document to that path.

## Help

```text
python -m dbt_metadata_dictionary --help
```

Help MUST describe the required input path, optional output path, generated
format, and failure behavior.

## Success Contract

- Exit status is `0`.
- The output is a complete deterministic Markdown document.
- With `--output`, standard output remains free of the document unless the
  command explicitly documents a status message format.
- The input manifest is not modified.

## Failure Contract

- Exit status is non-zero.
- An actionable diagnostic is written to standard error.
- No partial Markdown document is written to the requested output path.
- Input errors include missing or unreadable paths, directories supplied as
  files, invalid JSON, and invalid supported collection shapes.

## Markdown Contract

The document contains distinct labeled sections for semantic models and
metrics. Each section uses fixed columns for:

1. Name
2. Dimensions
3. Entities
4. Data types

Absent values use the documented empty representation. Multiple values are
retained in a deterministic readable cell format. Cell content is escaped so
pipes and line breaks in source values do not break table layout.
