import json

from jina_cli.utils import format_bibtex_results


def test_format_bibtex_results_json_preserves_unicode_and_empty_values():
    """JSON mode must not lose API fields that are empty or non-ASCII."""
    results = [
        {
            "bibtex": "@article{café,\n  title={研究}\n}",
            "doi": "",
            "citations": 0,
        },
        {},
    ]

    rendered = format_bibtex_results(results, as_json=True)

    assert "café" in rendered
    assert "研究" in rendered
    assert json.loads(rendered) == results


def test_format_bibtex_results_ignores_empty_bibtex_entries_in_text_mode():
    assert format_bibtex_results([{"bibtex": ""}, {}]) == ""
