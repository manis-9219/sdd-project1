from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ManifestRecord:
    category: str
    name: str = ""
    dimensions: list[str] = field(default_factory=list)
    entities: list[str] = field(default_factory=list)
    data_types: list[str] = field(default_factory=list)


@dataclass(slots=True)
class DataDictionary:
    semantic_models: list[ManifestRecord] = field(default_factory=list)
    metrics: list[ManifestRecord] = field(default_factory=list)
