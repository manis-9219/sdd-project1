# Data Model: dbt Metadata Data Dictionary

## Manifest

Represents the parsed root document from a local dbt `manifest.json`.

| Field | Type | Required | Validation |
|---|---|---:|---|
| semantic_models | collection of records | No | If present, must be a supported collection shape. |
| metrics | collection of records | No | If present, must be a supported collection shape. |
| other content | unknown | No | Ignored after supported sections are extracted. |

A manifest is valid for dictionary generation when it is readable JSON and its
supported sections are absent, empty, or valid collections of records. A valid
manifest with no supported records produces a valid empty-state dictionary.

## Metadata Record

The normalized representation shared by semantic models and metrics.

| Field | Type | Required | Validation |
|---|---|---:|---|
| category | semantic model or metric | Yes | Determines the output section. |
| name | text | No | Preserve when present; use the documented empty representation when absent. |
| dimensions | ordered collection of text | No | Normalize supported dimension names and preserve all values. |
| entities | ordered collection of text | No | Normalize supported entity names and preserve all values. |
| data_types | ordered collection of text | No | Normalize supported type values and preserve all values. |

The normalized record MUST retain category and all supported values without
inventing missing values. Values are rendered in a stable, escaped form so
Markdown separators and line breaks cannot corrupt table structure.

## Data Dictionary

Represents the generated Markdown document.

| Component | Rule |
|---|---|
| Title | Identifies the document as a dbt metadata data dictionary. |
| Semantic-model section | Present with a labeled table when records exist; otherwise uses the documented empty state. |
| Metric section | Present with a labeled table when records exist; otherwise uses the documented empty state. |
| Table columns | Fixed and clearly labeled for name, dimensions, entities, and data types. |
| Empty values | One consistent representation for absent optional metadata. |
| Multi-values | One readable, deterministic representation that retains every value. |
| Escaping | Cell content is escaped so source text cannot break Markdown tables. |

## Relationships

- A `Manifest` contains zero or more `Metadata Record` values in each supported category.
- Each `Metadata Record` belongs to exactly one category: semantic model or metric.
- A `Data Dictionary` contains the normalized records grouped by category.
