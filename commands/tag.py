from argparse import ArgumentParser

def initialize(subparsers):
  subparser: ArgumentParser = subparsers.add_parser("tag", help="create tag at current state")
  subparser.add_argument("name", help="name of tag")
  subparser.set_defaults(func=main)

def main(args):
  ...

if __name__ == "__main__":
  print("invalid usage")