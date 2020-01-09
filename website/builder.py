import os
import htmlmin
from jinja2 import Environment, FileSystemLoader, Template


def build(src, target, files=None):
    """
    Build "files" from "src" to "target".
    If "files" is None, build everything in "src".
    """
    env = Environment(loader=FileSystemLoader(src))
    # Get build targets
    # render HTML
    # minify
    # write to target folder
    template = env.get_template("path/to/file.html")
    html = template.render()
    html = htmlmin.minify(html)
