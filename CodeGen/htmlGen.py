from __future__ import annotations

import subprocess
import yaml
from functools import lru_cache

from .GenSections import Section
from .utils import InitError, indent


@lru_cache
def parse_yaml(filename: str = r"CodeGen\functions.yaml") -> dict:
    with open(filename, "r") as file:
        return yaml.safe_load(file)


def get_file_head():
    return """<head>
    <meta charset="UTF-8">
    <title>NumXX - Documentation</title>
    <link rel="icon" href="../media/numxx_icon.svg">
    <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="stylesheet" href="../css/hamburger_menu.css">
    <link rel="stylesheet" href="../css/code_blocks.css">
</head>
"""

def get_body(sidebar, main_content):
    # Body contains sidebar and main content
    return f"""<body>
{sidebar}

{main_content}

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/cpp.min.js"></script>
    <script src="../scripts/hamburger_menu_script.js"></script>
    <script src="../scripts/rotate_header_script.js"></script>
    <script>const MEDIA_PATH = '../';</script>
    <script src="../scripts/code_blocks_script.js"></script>

</body>
"""

def get_sidebar_code(func_names: list[str]):
    sidebar_actions = []
    for func in func_names:
        short_name = func.removeprefix("numxx::") if func.startswith("numxx::") else func
        long_name = func if func.startswith("numxx::") else f"numxx::{func}"

        if short_name != "template":
            if len(sidebar_actions) == 0:
                sidebar_actions.append(f"""<li><a href="#" data-section="{short_name}" class="active">{long_name}()</a></li>""")
            else:
                sidebar_actions.append(f"""<li><a href="#" data-section="{short_name}">{long_name}()</a></li>""")

    return f"""
    <!-- Sidebar -->
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <h3>Array Creation APIs</h3>
        </div>
        <ul class="sidebar-menu">
{indent("\n".join(sidebar_actions), no_indents=3)}
        </ul>
    </aside>
"""


def get_main_content(code_documentation: str):
    header_and_nav = """<header>
    <div class="container">
        <div class="left-container">

            <div class="big-logo">
                <a href="../index.html">
                    <img src="../media/numxx_logo_plain.svg" alt="NumXX">
                </a>
            </div>

            <div class="logo-text-container">
                <a href="../index.html">
                    <img src="../media/NumXX_text_light.svg" alt="NumXX">
                </a>
                C++ Numerical Computing Library
            </div>

        </div>

        <div class="small-logo">
            <a href="https://github.com/abdallahsoliman00/NumXX" target="_blank" title="NumXX GitHub">
                <img src="../media/github-logo-light.svg" alt="NumXX GitHub">
            </a>
        </div>
    </div>
</header>

<nav>
    <div class="container">
        <button class="menu-toggle" id="menuToggle">
            <span></span>
            <span></span>
            <span></span>
        </button>
        <ul>
            <li><a href="../index.html">Home</a></li>
            <li><a href="../getting_started.html">Getting Started</a></li>
            <li><a href="../documentation.html">Documentation</a></li>
            <li><a href="../examples.html">Examples</a></li>
        </ul>
    </div>
</nav>
"""

    footer = """
<footer>
    <div class="container">
        <p>&copy; 2025 abdallahsoliman00.</p>
    </div>
</footer>"""


    return f"""<div class="main-content">
{indent(header_and_nav)}

    <main class="container">
{code_documentation}
    </main>

{indent(footer)}
</div>
"""


def get_documentation_code_from_yaml(filename: str = r"CodeGen\functions.yaml"):
    html_data = parse_yaml(filename);
    html_docs = ""
    for func in html_data:
        try:
            sec = Section(func, html_data)
            html_docs += sec.write_section()
        except InitError:
            print(f"Warning: Skipped intialization of {func}.")

    return html_docs


def group_file(functions_yaml: str = r"CodeGen\functions.yaml"):
    parsed_yaml = parse_yaml(functions_yaml)
    function_names = parsed_yaml.keys()
    docs_html = get_documentation_code_from_yaml(functions_yaml)

    sidebar_code = get_sidebar_code(function_names)
    main_content_code = get_main_content(docs_html)
    
    return f"""<!DOCTYPE html>
<html lang="en">
{get_file_head()}

{get_body(sidebar_code, main_content_code)}

</html>
"""


# Run from root directory using:
#   python -m CodeGen.htmlGen
if __name__ == "__main__":
    full_html = group_file(r"CodeGen\functions.yaml")

    out_filename = r"docs_mini_pages\array_creation.html"
    with open(out_filename, "w") as outFile:
        write_success = outFile.write(full_html)

    fmt_success = subprocess.run(
        f"npx prettier --write {out_filename} --config .prettierrc.json",
        shell=True
    )

    if write_success and fmt_success:
        print(f"Success! See {out_filename}")
