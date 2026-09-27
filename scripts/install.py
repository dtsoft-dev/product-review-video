#!/usr/bin/env python3
"""Install the bundled Codex skill, backing up an existing copy on update."""

import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import shutil
import sys
import tempfile

NAME = "product-review-video"
SOURCE = Path(__file__).resolve().parents[1] / "skills" / NAME


def install(skills_dir: Path, update: bool) -> Path:
    skills_dir = skills_dir.expanduser().resolve()
    destination = skills_dir / NAME
    if not (SOURCE / "SKILL.md").is_file():
        raise ValueError("Missing bundled SKILL.md; run this from a complete repository clone.")
    if destination.is_symlink():
        raise ValueError(f"Refusing to replace a symlink: {destination}")
    if destination.exists() and (not update or not destination.is_dir()):
        raise ValueError(f"Already exists: {destination}. Use --update to back up and replace a skill directory.")
    if destination == SOURCE or SOURCE in destination.parents or destination in SOURCE.parents:
        raise ValueError("The installation destination must be separate from the repository source.")

    skills_dir.mkdir(parents=True, exist_ok=True)
    backup = None
    with tempfile.TemporaryDirectory(prefix=".skill-install-", dir=skills_dir.parent) as temp:
        staged = Path(temp) / NAME
        shutil.copytree(SOURCE, staged)
        if destination.exists():
            # Keep backups outside skills/ so they cannot be discovered as duplicate skills.
            backup_root = skills_dir.parent / "skill-backups"
            backup_root.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup = backup_root / f"{NAME}-{stamp}"
            destination.rename(backup)
        try:
            staged.rename(destination)
        except OSError:
            if backup is not None and not destination.exists():
                backup.rename(destination)
            raise
    if backup is not None:
        print(f"Previous version backed up to: {backup}")
    print(f"Installed: {destination}")
    print("Restart Codex to load the updated skill.")
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    codex_dir = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    parser.add_argument("--skills-dir", type=Path, default=codex_dir / "skills",
                        help="Skills directory (default: $CODEX_HOME/skills or ~/.codex/skills)")
    parser.add_argument("--update", action="store_true",
                        help="Back up an existing installation, then replace it")
    args = parser.parse_args()
    try:
        install(args.skills_dir, args.update)
    except (OSError, ValueError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
