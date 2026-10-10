import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "bitbotXLzero"
author = "Michal Hnatek"
release = "1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Google-style "Args:" / "Returns:" sections
]

# These only exist on the micro:bit itself, so fake them for the docs build.
autodoc_mock_imports = ["microbit", "utime", "neopixel"]
autodoc_member_order = "bysource"

html_theme = "sphinx_rtd_theme"
html_title = "BitBot XL library"

exclude_patterns = ["_build"]


def _literal_examples(app, what, name, obj, options, lines):
    """Show "Example:" / "Usage:" blocks in docstrings as code blocks."""
    out = []
    for line in lines:
        if line.strip() in ("Example:", "Usage:"):
            out.append(line.strip() + ":")
            out.append("")
        else:
            out.append(line)
    lines[:] = out


def setup(app):
    # priority below napoleon's (500) so this runs first
    app.connect("autodoc-process-docstring", _literal_examples, priority=100)
