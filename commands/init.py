from argparse import ArgumentParser, Namespace
from pathlib import Path

def initialize(subparsers):
  subparser: ArgumentParser = subparsers.add_parser("init", help="initialize sfit for filename")
  subparser.add_argument("filename", help="name of file to be tracked")
  subparser.set_defaults(func=command_handler)

def command_handler(args: Namespace):
  # Create .sfit folder
  sfit_folder = Path(".sfit")
  try:
    sfit_folder.mkdir()
  except FileExistsError:
    print("sfit already initialized")
    return

  # Create config file
  config_file = sfit_folder / "config"
  with config_file.open("w") as f:
    f.write(args.filename)

  # Create .sfit folders
  folders = ["refs", "objects"]
  for folder in folders:
    (sfit_folder / folder).mkdir(parents=True, exist_ok=True)

  # Create refs file
  (sfit_folder / "refs" / "heads").mkdir(parents=True, exist_ok=True)
  (sfit_folder / "refs" / "tags").mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
  print("invalid usage")