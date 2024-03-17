from argparse import ArgumentParser

def initialize(subparsers):
  subparser: ArgumentParser = subparsers.add_parser("checkout", help="move working directory to reference")
  subparser.add_argument("reference", help="name of branch or tag to move to")
  subparser.set_defaults(func=main)

def main(args):
  ...

if __name__ == "__main__":
  print("invalid usage")