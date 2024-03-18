from argparse import ArgumentParser, Namespace

def initialize(subparsers):
  subparser: ArgumentParser = subparsers.add_parser("add", help="stage changes made to file")
  subparser.set_defaults(func=command_handler)

def command_handler(args: Namespace):
  ...

if __name__ == "__main__":
  print("invalid usage")