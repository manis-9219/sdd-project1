from __future__ import annotations

from pathlib import Path

from dbt_metadata_dictionary.models import ManifestRecord


def make_record(
    category: str,
    name: str,
    dimensions: list[str] | None = None,
    entities: list[str] | None = None,
    data_types: list[str] | None = None,
) -> ManifestRecord:
    return ManifestRecord(
        category=category,
        name=name,
        dimensions=dimensions or [],
        entities=entities or [],
        data_types=data_types or [],
    )


def fixture_path(name: str) -> Path:
    return Path(__file__).parent / "fixtures" / name
