#!/usr/bin/env python3
"""Validate a DRD JSON document against the public generic schema."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


DEFAULT_SCHEMA = Path(__file__).resolve().parents[1] / "schemas" / "drd.schema.json"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drd_json", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()

    try:
        document = json.loads(args.drd_json.read_text(encoding="utf-8"))
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(document), key=lambda item: list(item.path))
    if errors:
        for error in errors:
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            print(f"ERROR {location}: {error.message}", file=sys.stderr)
        return 1

    print("DRD validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
