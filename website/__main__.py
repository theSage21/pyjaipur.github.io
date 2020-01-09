import argparse

parser = argparse.ArgumentParser(
    description=(
        "Helper functions to build a static site. Folder structure of"
        "the source is preserved.Files starting with `.` are ignored."
    )
)
parser.add_argument(
    "cmd",
    default="build",
    choices=["build", "watch"],
    help="What action do you want to take?",
)

args = parser.parse_args()
if args.cmd == "build":
    from site.builder import build

    build(src="templates", target="docs")
