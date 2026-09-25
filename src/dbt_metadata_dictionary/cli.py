from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from .errors import (DataDictionaryError, InputPathError,
                     ManifestValidationError, OutputWriteError)
from .parser import load_manifest
from .renderer import render_dictionary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dbt_metadata_dictionary",
        description="Generate a Markdown data dictionary from a dbt manifest.json file.",
    )
    parser.add_argument("manifest", help="Path to the dbt manifest.json file to read.")
    parser.add_argument(
        "--output",
        dest="output",
        help="Optional destination path for the generated Markdown document.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        dictionary = load_manifest(args.manifest)
        markdown = render_dictionary(dictionary)
        if args.output:
            output_path = Path(args.output)
            try:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                temp_path = output_path.with_suffix(output_path.suffix + ".tmp")
                temp_path.write_text(markdown, encoding="utf-8")
                temp_path.replace(output_path)
            except OSError as exc:
                raise OutputWriteError(f"Unable to write output file '{output_path}': {exc}") from exc
            return 0
        sys.stdout.write(markdown)
        return 0
    except InputPathError as exc:
        print(f"Error: Invalid input path: {exc}", file=sys.stderr)
        return 1
    except ManifestValidationError as exc:
        print(f"Error: Invalid manifest: {exc}", file=sys.stderr)
        return 1
    except OutputWriteError as exc:
        print(f"Error: Output error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
