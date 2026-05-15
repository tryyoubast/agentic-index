import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from agentic_index.catalog import (
    Catalog,
    CatalogError,
    load_catalog,
    recommend_projects,
    search_projects,
)


class CatalogTests(unittest.TestCase):
    def test_load_catalog_validates_seed_data(self) -> None:
        catalog = load_catalog()

        self.assertGreaterEqual(len(catalog.projects), 20)
        self.assertEqual(catalog.by_slug("context7").name, "Context7")
        self.assertIn("codex", catalog.by_slug("awesome-codex-skills").clients)

    def test_search_projects_matches_names_summaries_and_tags(self) -> None:
        catalog = load_catalog()

        results = search_projects(catalog, "memory")

        self.assertEqual(
            [project.slug for project in results][:2],
            ["claude-mem", "claude-memory-compiler"],
        )

    def test_recommend_projects_filters_by_client_and_goal(self) -> None:
        catalog = load_catalog()

        results = recommend_projects(catalog, client="codex", goal="skills", limit=3)

        self.assertTrue(results)
        self.assertEqual(results[0].slug, "awesome-codex-skills")
        self.assertTrue(all("codex" in project.clients for project in results))
        self.assertTrue(
            all(
                "skills" in project.use_cases or project.category == "skills"
                for project in results
            )
        )

    def test_catalog_rejects_duplicate_slugs(self) -> None:
        with TemporaryDirectory() as tmp:
            data_file = Path(tmp) / "projects.json"
            data_file.write_text(
                """
                [
                  {
                    "slug": "dupe",
                    "name": "One",
                    "url": "https://github.com/example/one",
                    "summary": "One",
                    "category": "skills",
                    "clients": ["codex"],
                    "use_cases": ["skills"],
                    "stars": 1,
                    "install": "n/a",
                    "why_it_matters": "n/a",
                    "caveats": "n/a",
                    "tags": ["x"]
                  },
                  {
                    "slug": "dupe",
                    "name": "Two",
                    "url": "https://github.com/example/two",
                    "summary": "Two",
                    "category": "skills",
                    "clients": ["codex"],
                    "use_cases": ["skills"],
                    "stars": 2,
                    "install": "n/a",
                    "why_it_matters": "n/a",
                    "caveats": "n/a",
                    "tags": ["y"]
                  }
                ]
                """,
                encoding="utf-8",
            )

            with self.assertRaisesRegex(CatalogError, "duplicate slug"):
                Catalog.from_file(data_file)

    def test_catalog_rejects_unknown_category(self) -> None:
        with TemporaryDirectory() as tmp:
            data_file = Path(tmp) / "projects.json"
            data_file.write_text(
                """
                [
                  {
                    "slug": "bad",
                    "name": "Bad",
                    "url": "https://github.com/example/bad",
                    "summary": "Bad",
                    "category": "unknown",
                    "clients": ["codex"],
                    "use_cases": ["skills"],
                    "stars": 1,
                    "install": "n/a",
                    "why_it_matters": "n/a",
                    "caveats": "n/a",
                    "tags": ["x"]
                  }
                ]
                """,
                encoding="utf-8",
            )

            with self.assertRaisesRegex(CatalogError, "unknown category"):
                Catalog.from_file(data_file)


if __name__ == "__main__":
    unittest.main()
