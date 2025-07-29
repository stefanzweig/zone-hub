# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os
from sphinx.ext.autodoc import PropertyDocumenter
from subprocess import Popen, PIPE

sys.path.insert(0, os.path.abspath("../../"))

project = "Zone Hub"
copyright = "2025, Z-One"
author = "刘海江"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "zh_CN"
# add_module_names = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

autodoc_default_options = {
    "members": True,
    "special-members": "__init__",
    "undoc-members": True,
    "property-no-value": True,
    "hide-property-decorators": True,
}
html_css_files = [
    'custom.css',
]
pipe = Popen("git describe --tags --always", stdout=PIPE, shell=True)
git_version = pipe.stdout.read().decode("utf8")

if git_version:
    version = git_version.rsplit("-", 1)[0]
    release = git_version
else:
    version = ""
    release = ""


# 方法1：修改PropertyDocumenter的显示方式
def skip_property_header(self, sig):
    # 完全跳过property的header生成
    pass


def setup(app):
    # 方法1：直接修改PropertyDocumenter的行为
    PropertyDocumenter.add_directive_header = skip_property_header

    # 方法2：同时添加事件处理（双保险）
    app.connect(
        "autodoc-process-signature",
        lambda app, what, name, obj, options, sig, ret: (
            (None, ret) if isinstance(obj, property) else (sig, ret)
        ),
    )

    return {"version": "1.0"}  # 必须返回字典
