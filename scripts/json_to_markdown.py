#!/usr/bin/env python3
"""Render a saved Cardano API JSON result as readable Markdown."""

import argparse
import json
from pathlib import Path
from typing import Any


def scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def render(value: Any, title: str) -> str:
    lines = [f"# {title}", ""]
    if isinstance(value, list) and all(isinstance(row, dict) for row in value):
        keys = sorted({key for row in value for key in row})
        if keys:
            lines.append("| " + " | ".join(keys) + " |")
            lines.append("| " + " | ".join("---" for _ in keys) + " |")
            for row in value:
                lines.append("| " + " | ".join(scalar(row.get(key, "")).replace("|", "\\|") for key in keys) + " |")
            return "\n".join(lines) + "\n"
    if isinstance(value, dict):
        lines.extend(["| Field | Value |", "| --- | --- |"])
        for key, item in value.items():
            lines.append(f"| {key} | {scalar(item).replace('|', '\\|')} |")
        return "\n".join(lines) + "\n"
    lines.append("```json")
    lines.append(json.dumps(value, ensure_ascii=False, indent=2))
    lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    output = render(data, args.input.stem)
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
