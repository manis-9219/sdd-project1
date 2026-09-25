# Research: dbt Metadata Data Dictionary

## Decision: Use the Python standard library only

**Rationale**: The feature needs JSON parsing, filesystem access, command-line
argument handling, typed value objects, and Markdown string generation. Python's
standard library provides all of these capabilities, which satisfies the
constitution's dependency-minimization requirement and keeps the utility
offline-capable.

**Alternatives considered**: A third-party CLI framework or schema-validation
package could reduce some boilerplate, but would add dependency and versioning
cost without being necessary for this local utility.

## Decision: Treat the manifest as a version-tolerant JSON document

**Rationale**: dbt manifest structures can evolve, and the requested metadata
is limited to records under `semantic_models` and `metrics`. The parser will
validate the supported collection shapes and normalize only the fields needed
by the data dictionary rather than attempting to model the entire manifest.
Missing optional fields will be represented as empty values instead of inferred
values.

**Alternatives considered**: Strictly validating the entire dbt manifest schema
would couple the utility to one dbt release and reject otherwise useful
metadata when unrelated fields change.

## Decision: Render deterministic Markdown tables with explicit sections

**Rationale**: Separate headings and fixed columns make semantic models and
metrics easy to scan. Stable source ordering, stable field ordering, and
consistent empty-value and multi-value formatting make output suitable for
diffing and documentation review.

**Alternatives considered**: A generic Markdown serializer would not establish
the required data-dictionary contract. A JSON or CSV output would not satisfy
the requested documentation format.

## Decision: Use `unittest` and temporary filesystem fixtures

**Rationale**: `unittest` is available in the standard library and supports
isolated parser, renderer, and CLI tests. Temporary directories allow file and
permission/error scenarios to be tested without modifying repository files.

**Alternatives considered**: `pytest` is widely used, but it would introduce a
third-party test dependency that is not needed for the feature's scope.

## Decision: Fail before rendering when the input cannot be parsed or validated

**Rationale**: The specification requires no misleading partial output. The
command will report an actionable error and return a non-success status before
writing output when the source path, JSON document, or supported collection
shape is invalid.

**Alternatives considered**: Best-effort rendering could preserve some data,
but would make omissions difficult to distinguish from valid absence and would
violate the no-misleading-output requirement.
