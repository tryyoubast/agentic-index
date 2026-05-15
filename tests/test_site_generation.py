import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from agentic_index.catalog import load_catalog
from scripts.generate_site import render_site, write_site


class SiteGenerationTests(unittest.TestCase):
    def test_render_site_includes_all_projects_and_core_sections(self) -> None:
        catalog = load_catalog()

        html = render_site(catalog)

        self.assertIn("<title>Agentic Index", html)
        self.assertIn("Stop hunting through awesome lists", html)
        for project in catalog.projects:
            self.assertIn(project.name, html)
            self.assertIn(project.url, html)

    def test_write_site_creates_html_file(self) -> None:
        catalog = load_catalog()
        with TemporaryDirectory() as tmp:
            output = Path(tmp) / "index.html"

            write_site(catalog, output)

            self.assertTrue(output.exists())
            self.assertIn("Agentic Index", output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
