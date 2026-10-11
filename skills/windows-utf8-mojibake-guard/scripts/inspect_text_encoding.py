#!/usr/bin/env python3
"""Read-only UTF-8/mojibake inspector for Windows-heavy Codex workflows."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


MARKERS = [
    "\ufeff",
    "\ufffd",
    "閳",
    "閿",
    "閻",
    "閹",
    "娑",
    "锟",
    "脗",
    "脙",
    "鐏",
    "瓊",
    "娴",
    "竴",
    "綘",
    "鏈",
    "浼",
    "氳",
    "鍝",
    "涔",
    "爜",
    "濂",
    "鈥",
    "銆",
    "绋",
    "嬫",
    "浣",
    "鍚",
    "鐨",
    "濂?",
    "娴?",
    "銆?",
    "锛",
]


def inspect(path: Path) -> dict:
    data = path.read_bytes()
    result = {
        "path": str(path),
        "bytes": len(data),
        "exists": path.exists(),
        "utf8": False,
        "bom_utf8": data.startswith(b"\xef\xbb\xbf"),
        "nul_bytes": data.count(b"\x00"),
        "markers": {},
        "sample": "",
        "error": None,
    }
    try:
        text = data.decode("utf-8")
        result["utf8"] = True
    except UnicodeDecodeError as exc:
        result["error"] = f"utf8_decode_error: {exc}"
        text = data.decode("utf-8", errors="replace")

    result["sample"] = text[:240].replace("\n", "\\n")
    for marker in MARKERS:
        count = text.count(marker)
        if count:
            result["markers"][marker] = count

    suffix = path.suffix.lower()
    if suffix == ".json" and result["utf8"]:
        try:
            json.loads(text.lstrip("\ufeff"))
            result["json_parse"] = "ok"
        except Exception as exc:  # noqa: BLE001 - diagnostic output
            result["json_parse"] = f"error: {exc}"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect text files for UTF-8/BOM/mojibake risk.")
    parser.add_argument("paths", nargs="+", help="Files to inspect")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    results = [inspect(Path(item)) for item in args.paths]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    for item in results:
        print(f"== {item['path']}")
        print(f"bytes: {item['bytes']}  utf8: {item['utf8']}  bom_utf8: {item['bom_utf8']}  nul_bytes: {item['nul_bytes']}")
        if item.get("json_parse"):
            print(f"json_parse: {item['json_parse']}")
        if item["error"]:
            print(f"error: {item['error']}")
        if item["markers"]:
            markers = ", ".join(f"{key}={value}" for key, value in item["markers"].items())
            print(f"markers: {markers}")
        else:
            print("markers: none")
        print(f"sample: {item['sample']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
