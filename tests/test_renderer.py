import unittest

from dbt_metadata_dictionary.models import DataDictionary, ManifestRecord
from dbt_metadata_dictionary.renderer import render_dictionary


class RendererTests(unittest.TestCase):
    def test_renderer_includes_sections_and_multivalue_cells(self):
        dictionary = DataDictionary(
            semantic_models=[
                ManifestRecord(
                    category="semantic model",
                    name="customers",
                    dimensions=["customer_id", "region"],
                    entities=["customer", "order"],
                    data_types=["string", "numeric"],
                )
            ],
            metrics=[
                ManifestRecord(
                    category="metric",
                    name="revenue",
                    dimensions=["date"],
                    entities=["customer", "product"],
                    data_types=["numeric", "float"],
                )
            ],
        )

        markdown = render_dictionary(dictionary)

        self.assertIn("# dbt Metadata Data Dictionary", markdown)
        self.assertIn("## Semantic Models", markdown)
        self.assertIn("## Metrics", markdown)
        self.assertIn("customer_id\\|region", markdown)
        self.assertIn("customer\\|order", markdown)
        self.assertIn("numeric\\|float", markdown)
        self.assertIn("date", markdown)

    def test_renderer_uses_empty_placeholder_for_missing_values(self):
        dictionary = DataDictionary(
            semantic_models=[
                ManifestRecord(
                    category="semantic model",
                    name="orders",
                    dimensions=[],
                    entities=[],
                    data_types=[],
                )
            ],
            metrics=[],
        )

        markdown = render_dictionary(dictionary)

        self.assertIn("—", markdown)


if __name__ == "__main__":
    unittest.main()
