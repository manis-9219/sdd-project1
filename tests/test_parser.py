import unittest
from pathlib import Path

from dbt_metadata_dictionary.errors import ManifestValidationError
from dbt_metadata_dictionary.parser import load_manifest


class ParserTests(unittest.TestCase):
    def test_complete_manifest_extracts_supported_records(self):
        dictionary = load_manifest(Path(__file__).parent / "fixtures" / "manifest_complete.json")

        self.assertEqual(len(dictionary.semantic_models), 2)
        self.assertEqual(len(dictionary.metrics), 2)
        self.assertEqual(dictionary.semantic_models[0].name, "customers")
        self.assertEqual(dictionary.metrics[0].name, "revenue")
        self.assertEqual(dictionary.semantic_models[0].dimensions, ["customer_id", "region"])
        self.assertEqual(dictionary.semantic_models[0].entities, ["customer", "order"])
        self.assertEqual(dictionary.semantic_models[0].data_types, ["string", "numeric"])

    def test_empty_manifest_renders_empty_sections(self):
        dictionary = load_manifest(Path(__file__).parent / "fixtures" / "manifest_empty.json")

        self.assertEqual(dictionary.semantic_models, [])
        self.assertEqual(dictionary.metrics, [])

    def test_invalid_collection_shape_raises(self):
        with self.assertRaises(ManifestValidationError):
            load_manifest(Path(__file__).parent / "fixtures" / "manifest_invalid.json")


if __name__ == "__main__":
    unittest.main()
