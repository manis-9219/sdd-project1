# Feature Specification: dbt Metadata Data Dictionary

**Feature Branch**: `001-dbt-metadata-dictionary`

**Created**: 2026-09-25

**Status**: Draft

**Input**: User description: "Build a local Python CLI utility that parses a dbt project's `manifest.json`. It must extract metadata under `semantic_models` and `metrics` (names, dimensions, entities, and data types) and format it into a clean Markdown table data dictionary."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Generate a metadata data dictionary (Priority: P1)

As a data practitioner, I want to point the utility at a dbt project's `manifest.json` and receive a Markdown data dictionary so that I can inspect semantic-model and metric metadata without manually navigating the manifest.

**Why this priority**: Producing a usable dictionary is the core value of the feature and enables every other workflow.

**Independent Test**: Run the utility against a representative manifest containing semantic models and metrics, then verify that the generated Markdown contains the expected metadata in readable tables.

**Acceptance Scenarios**:

1. **Given** a valid manifest containing semantic models with names, dimensions, entities, and data types, **When** the user generates the dictionary, **Then** the output contains one clearly labeled table with the available semantic-model metadata.
2. **Given** a valid manifest containing metrics with names, dimensions, entities, and data types, **When** the user generates the dictionary, **Then** the output contains one clearly labeled table with the available metric metadata.
3. **Given** a valid manifest containing both supported metadata categories, **When** the user generates the dictionary, **Then** the output is deterministic and can be saved directly as a Markdown document.

---

### User Story 2 - Use the utility safely with project files (Priority: P2)

As a data practitioner, I want clear input and output behavior so that I can use the utility repeatedly in local documentation workflows without changing the source manifest.

**Why this priority**: Predictable file handling prevents accidental source changes and makes the utility practical for regular use.

**Independent Test**: Run the utility with valid and invalid input paths, with output directed to a file and to standard output, and verify that source data remains unchanged and failures are understandable.

**Acceptance Scenarios**:

1. **Given** a readable manifest path and a requested output destination, **When** the user runs the utility, **Then** the dictionary is written to that destination and the manifest is unchanged.
2. **Given** a readable manifest path and no output destination, **When** the user runs the utility, **Then** the dictionary is emitted as Markdown for immediate viewing or redirection.
3. **Given** a missing, unreadable, or malformed manifest, **When** the user runs the utility, **Then** it reports a concise actionable error and does not produce misleading dictionary content.

---

### User Story 3 - Preserve incomplete metadata honestly (Priority: P3)

As a data practitioner, I want missing or optional metadata represented consistently so that the dictionary does not imply information that was absent from the manifest.

**Why this priority**: dbt manifests can vary across projects and versions; honest representation keeps the output trustworthy.

**Independent Test**: Run the utility against fixtures where dimensions, entities, or data types are absent or empty, then verify that the output remains valid Markdown and distinguishes unavailable values from present values.

**Acceptance Scenarios**:

1. **Given** a supported object with no dimensions or entities, **When** the dictionary is generated, **Then** the corresponding cells use a consistent empty-value representation.
2. **Given** a supported object with multiple dimensions, entities, or data types, **When** the dictionary is generated, **Then** all values remain readable within their table cells without silently dropping entries.
3. **Given** a manifest with unsupported top-level content, **When** the dictionary is generated, **Then** unsupported content is ignored and supported metadata is still rendered.

### Edge Cases

- The input path does not exist, points to a directory, or cannot be read.
- The manifest is not valid JSON or is structurally incomplete.
- `semantic_models` or `metrics` is absent, empty, or not a collection of supported records.
- A record has a missing name or contains null, empty, or mixed-shape metadata fields.
- A metadata value contains Markdown table characters, line breaks, or repeated values.
- The manifest contains no supported metadata at all.
- The output destination cannot be created or written.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The utility MUST accept a local dbt `manifest.json` path as input.
- **FR-002**: The utility MUST read the manifest without modifying the source file.
- **FR-003**: The utility MUST extract supported records under `semantic_models` and `metrics`.
- **FR-004**: The utility MUST include each supported record's name in the generated dictionary when available.
- **FR-005**: The utility MUST include dimensions, entities, and data types associated with each supported record when available.
- **FR-006**: The utility MUST produce clean, consistently labeled Markdown tables that distinguish semantic models from metrics.
- **FR-007**: The utility MUST preserve all supported values in a readable representation when a record has multiple dimensions, entities, or data types.
- **FR-008**: The utility MUST represent missing or empty supported metadata consistently without inventing values.
- **FR-009**: The utility MUST allow generated Markdown to be written to a user-selected destination or emitted for standard output when no destination is selected.
- **FR-010**: The utility MUST report actionable errors for missing, unreadable, malformed, or structurally invalid input.
- **FR-011**: The utility MUST avoid emitting misleading partial output when the input cannot be parsed or validated.
- **FR-012**: The utility MUST ignore unsupported manifest content while continuing to process valid supported metadata.
- **FR-013**: The utility MUST produce deterministic output for the same manifest and invocation options.
- **FR-014**: The utility MUST provide usage guidance through its command-line help behavior.
- **FR-015**: The utility MUST be covered by automated tests for successful extraction, formatting, empty metadata, malformed input, and file errors.

### Key Entities *(include if feature involves data)*

- **Manifest**: A dbt project metadata document that may contain semantic models, metrics, and other top-level content.
- **Semantic Model**: A supported manifest record identified by a name and optional dimensions, entities, and data types.
- **Metric**: A supported manifest record identified by a name and optional dimensions, entities, and data types.
- **Data Dictionary**: The generated Markdown document containing labeled tables for supported semantic models and metrics.
- **Metadata Value**: A dimension, entity, or data-type value associated with a supported record.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: For a valid fixture containing at least 25 supported records, users receive a complete Markdown dictionary in under 2 seconds on a typical development laptop.
- **SC-002**: 100% of supported names, dimensions, entities, and data types present in the input fixture appear in the generated dictionary.
- **SC-003**: 100% of malformed, missing, unreadable, or structurally invalid input cases produce a non-success result with an actionable error and no misleading dictionary output.
- **SC-004**: Repeated runs with the same manifest and options produce byte-for-byte identical Markdown output.
- **SC-005**: A reviewer can identify the semantic-model and metric sections and locate any included metadata within 30 seconds for a representative fixture.
- **SC-006**: The automated test suite covers all primary success paths and listed error categories before the feature is approved for integration.

## Assumptions

- The input is a local dbt `manifest.json` file encoded as JSON.
- The supported manifest structures for semantic models and metrics are based on representative dbt manifest fixtures and may evolve through future feature work.
- The first release supports local generation only; remote files, interactive services, and publishing to external documentation systems are out of scope.
- Markdown table output is intended for common repository documentation viewers and does not require a custom renderer.
- When a source record omits an optional metadata field, the dictionary will use a documented consistent empty-value representation.
- Users have permission to read the source manifest and write to the requested output destination.
- The project constitution requires standard-library use where practical, strict type checking, automated tests, documentation, and code review; these are quality constraints rather than user-visible behavior.
