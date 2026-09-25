from __future__ import annotations

from .models import DataDictionary, ManifestRecord

_EMPTY_VALUE = "—"


def _escape_cell(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace("|", "\\|")
    return escaped.replace("\r\n", "<br>").replace("\n", "<br>").replace("\r", "<br>")


def _format_cell(values: list[str]) -> str:
    if not values:
        return _EMPTY_VALUE
    escaped_values = [_escape_cell(value) for value in values]
    return "\\|".join(escaped_values)


def _render_table(records: list[ManifestRecord]) -> str:
    if not records:
        return "| Name | Dimensions | Entities | Data types |\n| --- | --- | --- | --- |\n| — | — | — | — |"

    rows = [
        "| Name | Dimensions | Entities | Data types |",
        "| --- | --- | --- | --- |",
    ]
    for record in records:
        rows.append(
            "| {name} | {dims} | {ents} | {types} |".format(
                name=_escape_cell(record.name or _EMPTY_VALUE),
                dims=_format_cell(record.dimensions),
                ents=_format_cell(record.entities),
                types=_format_cell(record.data_types),
            )
        )
    return "\n".join(rows)


def render_dictionary(dictionary: DataDictionary) -> str:
    sections: list[str] = ["# dbt Metadata Data Dictionary"]
    sections.append("## Semantic Models")
    sections.append(_render_table(dictionary.semantic_models))
    sections.append("")
    sections.append("## Metrics")
    sections.append(_render_table(dictionary.metrics))
    return "\n".join(sections) + "\n"


def render_markdown(dictionary: DataDictionary) -> str:
    return render_dictionary(dictionary)
