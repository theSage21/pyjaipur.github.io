import argparse
from website.builder import build
from website.watcher import watch

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
parser.add_argument("--src", default="templates")
parser.add_argument("--target", default="docs")

args = parser.parse_args()
if args.cmd == "build":

    build(src=args.src, target=args.target)
elif args.cmd == "watch":

    def on_change():
        build(src=args.src, target=args.target)

    watch(args.src, on_change)
