from argparse import ArgumentParser, Namespace

def initialize(subparsers):
  subparser: ArgumentParser = subparsers.add_parser("init", help="initialize sfit for filename")
  subparser.add_argument("filename", help="name of file to be tracked")
  subparser.set_defaults(func=command_handler)

def command_handler(args: Namespace):
  ...

if __name__ == "__main__":
  print("invalid usage")