from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"name", "description", "metadata", "license"}


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    try:
        _, raw, _ = text.split("---", 2)
    except ValueError as exc:
        raise ValueError(f"{path}: malformed frontmatter") from exc

    data: dict[str, object] = {}
    current = None
    for line in raw.strip().splitlines():
        if not line.strip():
            continue
        if line.startswith("  ") and current == "metadata":
            continue
        match = re.match(r"^([a-zA-Z0-9_-]+):(?:\s*(.*))?$", line)
        if match:
            key, value = match.groups()
            current = key
            data[key] = value or {}
    return data


def main() -> int:
    registry = json.loads((ROOT / "skills" / "registry.json").read_text())
    paths = [ROOT / "SKILL.md"] + [ROOT / "skills" / row["path"] for row in registry["skills"]]
    paths.append(ROOT / "integrations" / "leadux-competitor-research" / "skills" / "strategy-handoff" / "SKILL.md")

    names: set[str] = set()
    for path in paths:
        if not path.exists():
            raise SystemExit(f"missing skill file: {path}")
        fm = parse_frontmatter(path)
        missing = REQUIRED - set(fm)
        if missing:
            raise SystemExit(f"{path}: missing frontmatter keys {sorted(missing)}")
        name = str(fm["name"])
        if name in names:
            raise SystemExit(f"duplicate skill name: {name}")
        names.add(name)

    registered = {row["name"] for row in registry["skills"]}
    dirs = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
    if registered != dirs:
        raise SystemExit(f"registry mismatch: registered={sorted(registered)} dirs={sorted(dirs)}")

    print(f"skills OK: {len(paths)} files, {len(registered)} registered modules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
