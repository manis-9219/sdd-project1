# dbt Metadata Data Dictionary

This project generates a Markdown data dictionary from a dbt `manifest.json` file. It extracts supported metadata from `semantic_models` and `metrics`, then renders deterministic tables for easy review in documentation or pull requests.

## Installation

```bash
python -m pip install -e .
```

## Usage

Generate output to standard output:

```bash
python -m dbt_metadata_dictionary path/to/manifest.json
```

Write the result to a file:

```bash
python -m dbt_metadata_dictionary path/to/manifest.json --output docs/data-dictionary.md
```

## Behavior

- Reads one local dbt manifest file.
- Ignores unsupported top-level content.
- Preserves supported values in a readable Markdown table.
- Returns a non-zero status with a concise error to stderr for missing paths, invalid JSON, and invalid collection shapes.
- Leaves the source manifest unchanged.

## Testing

```bash
.venv/bin/python -m unittest discover -s tests -v
```
