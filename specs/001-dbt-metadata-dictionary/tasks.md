---

description: "Task list for the dbt metadata data dictionary feature"
---

# Tasks: dbt Metadata Data Dictionary

**Input**: Design documents from `specs/001-dbt-metadata-dictionary/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, and `contracts/`

**Tests**: Included because the feature specification requires automated coverage for success paths, formatting, malformed input, empty metadata, and file errors.

**Organization**: Tasks are grouped by user story so each increment can be implemented and tested independently.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the planned source and test layout and establish the local usage documentation.

- [X] T001 Create the source package directories and test fixture directories from the implementation plan in `src/dbt_metadata_dictionary/` and `tests/`.
- [X] T002 [P] Add package initialization and module entry-point files in `src/dbt_metadata_dictionary/__init__.py` and `src/dbt_metadata_dictionary/__main__.py`.
- [X] T003 [P] Document local setup, module invocation, test discovery, and quality-gate commands in `README.md`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish typed domain objects and shared error behavior required by every user story.

**Critical**: Complete this phase before user-story implementation begins.

- [X] T004 Define typed `ManifestRecord` and `DataDictionary` domain models with normalized category, name, dimensions, entities, and data-type fields in `src/dbt_metadata_dictionary/models.py`.
- [X] T005 Define actionable input, structure, and output exception types in `src/dbt_metadata_dictionary/errors.py`.
- [X] T006 [P] Add shared test helpers for temporary manifests, output paths, and representative record construction in `tests/test_helpers.py`.

**Checkpoint**: Shared typed models, errors, and test infrastructure are ready for story work.

---

## Phase 3: User Story 1 - Generate a metadata data dictionary (Priority: P1) - MVP

**Goal**: Read supported semantic-model and metric metadata and produce deterministic labeled Markdown tables.

**Independent Test**: Run the parser and renderer tests against a complete fixture and verify that every supported name, dimension, entity, and data type appears in the correct labeled section.

### Tests for User Story 1

- [X] T007 [P] [US1] Create a complete manifest fixture containing semantic models and metrics with names, dimensions, entities, data types, and unrelated top-level content in `tests/fixtures/manifest_complete.json`.
- [X] T008 [P] [US1] Write parser extraction tests covering both supported collections and preservation of all supported metadata values in `tests/test_parser.py`.
- [X] T009 [P] [US1] Write renderer tests covering labeled sections, fixed columns, multi-value cells, Markdown escaping, and deterministic output in `tests/test_renderer.py`.
- [X] T010 [P] [US1] Write the happy-path CLI contract test for `python -m dbt_metadata_dictionary INPUT_MANIFEST` and standard-output Markdown in `tests/test_cli.py`.

### Implementation for User Story 1

- [X] T011 [US1] Implement version-tolerant manifest loading and normalization of `semantic_models` and `metrics` records in `src/dbt_metadata_dictionary/parser.py`.
- [X] T012 [US1] Implement deterministic Markdown section, table, cell-escaping, and multi-value rendering in `src/dbt_metadata_dictionary/renderer.py`.
- [X] T013 [US1] Implement the required input-path command-line argument, standard-output behavior, and successful exit status in `src/dbt_metadata_dictionary/cli.py` and `src/dbt_metadata_dictionary/__main__.py`.

**Checkpoint**: User Story 1 independently generates a complete Markdown dictionary from a representative manifest.

---

## Phase 4: User Story 2 - Use the utility safely with project files (Priority: P2)

**Goal**: Support file output and actionable failures without modifying the source manifest or emitting misleading partial output.

**Independent Test**: Run CLI tests with a destination path, missing paths, directories, malformed JSON, invalid supported collections, and unwritable output destinations; verify exit statuses, diagnostics, and output-file behavior.

### Tests for User Story 2

- [X] T014 [P] [US2] Add malformed JSON, missing input, directory input, invalid collection, and output-error fixtures or temporary-file scenarios in `tests/fixtures/manifest_invalid.json` and `tests/test_cli.py`.
- [X] T015 [US2] Write CLI contract tests for `--output`, help text, non-zero failures, standard-error diagnostics, no partial output, and unchanged source manifests in `tests/test_cli.py`.

### Implementation for User Story 2

- [X] T016 [US2] Add explicit JSON decoding, path, and supported-collection validation with actionable typed errors in `src/dbt_metadata_dictionary/parser.py` and `src/dbt_metadata_dictionary/errors.py`.
- [X] T017 [US2] Add `--output OUTPUT_PATH` handling, atomic complete-document writing, error-to-standard-error reporting, and non-zero failure statuses in `src/dbt_metadata_dictionary/cli.py`.
- [X] T018 [US2] Add command-line help text describing the manifest argument, optional output path, Markdown format, and failure behavior in `src/dbt_metadata_dictionary/cli.py`.

**Checkpoint**: User Stories 1 and 2 both work independently; successful output can be printed or written to a file, and failures do not create misleading output.

---

## Phase 5: User Story 3 - Preserve incomplete metadata honestly (Priority: P3)

**Goal**: Render absent, empty, null, mixed-shape, and multi-value metadata consistently without inventing or dropping supported values.

**Independent Test**: Run parser and renderer tests against empty and incomplete fixtures and verify valid Markdown with the documented empty representation and complete multi-value retention.

### Tests for User Story 3

- [X] T019 [P] [US3] Create an empty and incomplete manifest fixture covering absent sections, missing names, empty metadata, null values, and multiple values in `tests/fixtures/manifest_empty.json`.
- [X] T020 [US3] Write normalization tests for missing fields, empty values, mixed supported record shapes, unsupported top-level content, and complete multi-value preservation in `tests/test_parser.py`.
- [X] T021 [US3] Write renderer tests for the empty-state dictionary, consistent empty cells, and readable escaped multi-value cells in `tests/test_renderer.py`.

### Implementation for User Story 3

- [X] T022 [US3] Implement consistent empty-value normalization and record-shape handling without inferred metadata in `src/dbt_metadata_dictionary/parser.py`.
- [X] T023 [US3] Implement empty-state sections and stable rendering of absent, null, and multi-value fields in `src/dbt_metadata_dictionary/renderer.py`.

**Checkpoint**: All three user stories are independently testable and preserve the trustworthiness of incomplete metadata.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Verify the complete feature against the constitution, contract, and performance expectations.

- [X] T024 [P] Add module, function, and CLI usage documentation for the public interfaces in `src/dbt_metadata_dictionary/` and `README.md`.
- [X] T025 [P] Add a 25-record performance fixture and test that dictionary generation completes within the two-second target in `tests/test_renderer.py`.
- [X] T026 Run the quickstart scenarios from `specs/001-dbt-metadata-dictionary/quickstart.md` and record any corrections in `README.md`.
- [X] T027 Run formatting, import-organization, strict type-checking, and the full `unittest` suite; resolve all violations before review in the affected source and test files.
- [X] T028 Review the implementation against `specs/001-dbt-metadata-dictionary/contracts/cli.md`, `data-model.md`, and the project constitution before integration.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; create the package and test layout first.
- **Foundational (Phase 2)**: Depends on Setup; blocks all user-story work.
- **User Story 1 (Phase 3)**: Depends on Foundational and is the MVP increment.
- **User Story 2 (Phase 4)**: Depends on the shared parser, renderer, and CLI from User Story 1; extends the same independently testable command.
- **User Story 3 (Phase 5)**: Depends on the shared parser and renderer from User Story 1; can be developed after the MVP and tested independently.
- **Polish (Phase 6)**: Depends on the desired user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 2; no dependency on another user story.
- **User Story 2 (P2)**: Depends on User Story 1's parser, renderer, and CLI boundaries, then adds safe file output and failure behavior.
- **User Story 3 (P3)**: Depends on User Story 1's normalized model and renderer, then adds incomplete-data behavior.

### Within Each User Story

- Tests MUST be written before implementation and initially fail.
- Domain models and shared errors precede parser and renderer behavior.
- Parser behavior precedes CLI integration.
- Each checkpoint MUST pass before moving to the next story.

## Parallel Opportunities

- **Setup**: T002 and T003 can run in parallel after T001 creates the directories.
- **Foundational**: T006 can run in parallel with T004 and T005.
- **User Story 1 tests**: T007, T008, T009, and T010 can be prepared in parallel because they use separate fixture or test concerns.
- **User Story 3 tests**: T019 can run in parallel with the planning of T020 and T021, but implementation waits for the tests.
- **Polish**: T024 and T025 can run in parallel; T026-T028 run after implementation is complete.

## Parallel Example: User Story 1

```text
Task T007: Create tests/fixtures/manifest_complete.json
Task T008: Write parser tests in tests/test_parser.py
Task T009: Write renderer tests in tests/test_renderer.py
Task T010: Write CLI happy-path tests in tests/test_cli.py
```

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup.
2. Complete Phase 2: Foundational.
3. Complete Phase 3: User Story 1.
4. Run the independent extraction, rendering, and CLI tests.
5. Validate the representative dictionary output before expanding scope.

### Incremental Delivery

1. Add User Story 2 for safe file output and actionable failures.
2. Add User Story 3 for incomplete and variable metadata.
3. Complete Phase 6 quality gates and review.
4. Each story preserves the previous story's behavior and remains independently testable.

## Notes

- Every task uses a checkbox, sequential task ID, optional parallel marker, and
	story label where required; each task names at least one concrete file path.
- `[P]` marks tasks that can proceed in parallel without depending on incomplete work in another file.
- User story labels map directly to the priorities in `spec.md`.
- The suggested MVP is User Story 1.
