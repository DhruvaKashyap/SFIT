from argparse import ArgumentParser, Namespace

def initialize(subparsers):
  subparser: ArgumentParser = subparsers.add_parser("checkout", help="move working directory to reference")
  subparser.add_argument("reference", help="name of branch or tag to move to")
  subparser.set_defaults(func=command_handler)

def command_handler(args: Namespace):
  ...

if __name__ == "__main__":
  print("invalid usage")