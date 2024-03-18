from argparse import ArgumentParser, Namespace

def initialize(subparsers):
  subparser:ArgumentParser = subparsers.add_parser("merge", help="merge two references")
  subparser.add_argument("reference1", help="reference to merge to")
  subparser.add_argument("reference2", help="reference to be merged")
  subparser.set_defaults(func=command_handler)

def command_handler(args: Namespace):
  ...

if __name__ == "__main__":
  print("invalid usage")