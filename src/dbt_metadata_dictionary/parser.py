from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .errors import InputPathError, ManifestValidationError
from .models import DataDictionary, ManifestRecord


def _normalize_scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (int, float, bool)):
        return str(value)
    return str(value)


def _normalize_values(value: Any, *, field_name: str) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        text = value.strip()
        return [text] if text else []
    if isinstance(value, (list, tuple)):
        normalized: list[str] = []
        for item in value:
            if item is None:
                continue
            text = _normalize_scalar(item)
            if text:
                normalized.append(text)
        return normalized
    if isinstance(value, dict):
        # A single mapping means the field was not represented in the list form.
        # Keep the value only when it is a direct scalar string and preserve the
        # contract's trustworthiness by discarding empty dict payloads.
        text = _normalize_scalar(value)
        return [text] if text else []
    text = _normalize_scalar(value)
    return [text] if text else []


def _normalize_record(record: Any, category: str) -> ManifestRecord:
    if not isinstance(record, dict):
        raise ManifestValidationError(f"{category} record must be an object, got {type(record).__name__}")

    raw_name = record.get("name")
    name = _normalize_scalar(raw_name)

    dimensions = _normalize_values(record.get("dimensions"), field_name="dimensions")
    entities = _normalize_values(record.get("entities"), field_name="entities")
    data_types = _normalize_values(
        record.get("data_types")
        if "data_types" in record
        else record.get("data_type"),
        field_name="data_types",
    )

    return ManifestRecord(
        category=category,
        name=name,
        dimensions=dimensions,
        entities=entities,
        data_types=data_types,
    )


def _normalize_section(section: Any, *, label: str) -> list[ManifestRecord]:
    if section is None:
        return []
    if not isinstance(section, list):
        raise ManifestValidationError(f"{label} must be a list of objects or be absent")
    return [_normalize_record(record, label) for record in section]


def parse_manifest(data: Any) -> DataDictionary:
    if not isinstance(data, dict):
        raise ManifestValidationError("Manifest root must be a JSON object")

    semantic_models = _normalize_section(data.get("semantic_models"), label="semantic model")
    metrics = _normalize_section(data.get("metrics"), label="metric")

    return DataDictionary(semantic_models=semantic_models, metrics=metrics)


def load_manifest(path: str | Path) -> DataDictionary:
    manifest_path = Path(path)
    if not manifest_path.exists():
        raise InputPathError(f"Input manifest does not exist: {manifest_path}")
    if manifest_path.is_dir():
        raise InputPathError(f"Input manifest path is a directory: {manifest_path}")
    if not manifest_path.is_file():
        raise InputPathError(f"Input manifest is not a readable file: {manifest_path}")

    try:
        with manifest_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ManifestValidationError(
            f"Invalid manifest JSON in {manifest_path}: {exc.msg} at line {exc.lineno}, column {exc.colno}"
        ) from exc
    except OSError as exc:
        raise InputPathError(f"Unable to read manifest: {manifest_path} ({exc})") from exc

    return parse_manifest(payload)


def generate_dictionary(path: str | Path) -> str:
    from .renderer import render_dictionary

    return render_dictionary(load_manifest(path))
