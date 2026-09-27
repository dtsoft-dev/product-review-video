"""Verify fresh installs, safe updates, and configurable destinations."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAME = "product-review-video"


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        self.skills = self.home / "skills"

    def run_install(self, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts/install.py"), *args],
            env={**os.environ, "CODEX_HOME": str(self.home)},
            capture_output=True, text=True,
        )

    def test_fresh_install_copies_every_skill_file(self):
        result = self.run_install()
        self.assertEqual(result.returncode, 0, result.stderr)
        source = ROOT / "skills" / NAME
        for path in source.rglob("*"):
            if path.is_file():
                self.assertEqual(path.read_bytes(), (self.skills / NAME / path.relative_to(source)).read_bytes())

    def test_existing_install_requires_explicit_update(self):
        self.assertEqual(self.run_install().returncode, 0)
        custom = self.skills / NAME / "local-notes.txt"
        custom.write_text("Keep these local changes")
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual(custom.read_text(), "Keep these local changes")

    def test_update_backs_up_local_changes_outside_skills(self):
        self.assertEqual(self.run_install().returncode, 0)
        custom = self.skills / NAME / "local-notes.txt"
        custom.write_text("Local customization")
        result = self.run_install("--update")
        self.assertEqual(result.returncode, 0, result.stderr)
        backups = list((self.home / "skill-backups").glob(f"{NAME}-*"))
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / "local-notes.txt").read_text(), "Local customization")
        self.assertFalse(custom.exists())
        self.assertEqual([p.name for p in self.skills.iterdir()], [NAME])

    def test_custom_directory_with_spaces(self):
        target = self.home / "custom agent" / "skills"
        result = self.run_install("--skills-dir", str(target))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((target / NAME / "SKILL.md").is_file())
        self.assertFalse(self.skills.exists())

    @unittest.skipUnless(hasattr(os, "symlink"), "Symlinks unavailable")
    def test_update_does_not_replace_symlink(self):
        self.skills.mkdir()
        original = self.home / "external-skill"
        original.mkdir()
        (original / "SKILL.md").write_text("Original")
        (self.skills / NAME).symlink_to(original, target_is_directory=True)
        result = self.run_install("--update")
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.skills / NAME).is_symlink())
        self.assertEqual((original / "SKILL.md").read_text(), "Original")


if __name__ == "__main__":
    unittest.main()
