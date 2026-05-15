import io
import unittest
from contextlib import redirect_stdout

from agentic_index.cli import main


class CliTests(unittest.TestCase):
    def run_cli(self, *args: str) -> str:
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exit_code = main(list(args))
        self.assertEqual(exit_code, 0)
        return stdout.getvalue()

    def test_list_outputs_top_projects(self) -> None:
        output = self.run_cli("list", "--limit", "2")

        self.assertIn("claude-mem", output)
        self.assertIn("awesome-mcp-servers", output)

    def test_search_outputs_matching_project(self) -> None:
        output = self.run_cli("search", "context7")

        self.assertIn("context7", output)
        self.assertIn("Up-to-date code documentation", output)

    def test_show_outputs_project_details(self) -> None:
        output = self.run_cli("show", "awesome-codex-skills")

        self.assertIn("Awesome Codex Skills", output)
        self.assertIn("https://github.com/ComposioHQ/awesome-codex-skills", output)
        self.assertIn("Why it matters", output)

    def test_recommend_outputs_client_goal_matches(self) -> None:
        output = self.run_cli("recommend", "--client", "codex", "--goal", "skills", "--limit", "2")

        self.assertIn("awesome-codex-skills", output)
        self.assertIn("codex-skill-manager", output)

    def test_export_markdown_outputs_heading(self) -> None:
        output = self.run_cli("export", "--format", "markdown", "--limit", "1")

        self.assertIn("# Agentic Index", output)
        self.assertIn("##", output)

    def test_export_json_outputs_array(self) -> None:
        output = self.run_cli("export", "--format", "json", "--limit", "1")

        self.assertTrue(output.strip().startswith("["))
        self.assertIn('"slug"', output)


if __name__ == "__main__":
    unittest.main()
