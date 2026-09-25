import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CliTests(unittest.TestCase):
    def test_cli_stdout_success(self):
        manifest_path = Path(__file__).parent / "fixtures" / "manifest_complete.json"
        result = subprocess.run(
            [sys.executable, "-m", "dbt_metadata_dictionary", str(manifest_path)],
            capture_output=True,
            text=True,
            cwd=Path(__file__).resolve().parents[1],
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("# dbt Metadata Data Dictionary", result.stdout)
        self.assertIn("## Semantic Models", result.stdout)
        self.assertIn("## Metrics", result.stdout)

    def test_cli_writes_output_file(self):
        manifest_path = Path(__file__).parent / "fixtures" / "manifest_complete.json"
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "dictionary.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "dbt_metadata_dictionary",
                    str(manifest_path),
                    "--output",
                    str(output_path),
                ],
                capture_output=True,
                text=True,
                cwd=Path(__file__).resolve().parents[1],
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(output_path.exists())
            self.assertIn("## Semantic Models", output_path.read_text())
            self.assertEqual(result.stdout, "")

    def test_cli_reports_invalid_manifest(self):
        invalid_path = Path(__file__).parent / "fixtures" / "manifest_invalid.json"
        result = subprocess.run(
            [sys.executable, "-m", "dbt_metadata_dictionary", str(invalid_path)],
            capture_output=True,
            text=True,
            cwd=Path(__file__).resolve().parents[1],
            check=False,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr.lower())

    def test_cli_help_lists_usage(self):
        result = subprocess.run(
            [sys.executable, "-m", "dbt_metadata_dictionary", "--help"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).resolve().parents[1],
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("manifest", result.stdout.lower())
        self.assertIn("--output", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
