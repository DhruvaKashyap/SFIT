from argparse import ArgumentParser, Namespace

def initialize(subparsers):
  subparser: ArgumentParser = subparsers.add_parser("branch", help="create new branch")
  subparser.add_argument("name", help="name of branch to be created")
  subparser.set_defaults(func=command_handler)

def command_handler(args: Namespace):
  ...

if __name__ == "__main__":
  print("invalid usage")