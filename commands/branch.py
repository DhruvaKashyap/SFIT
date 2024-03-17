from argparse import ArgumentParser

def initialize(subparsers):
  subparser: ArgumentParser = subparsers.add_parser("branch", help="create new branch")
  subparser.add_argument("name", help="name of branch to be created")
  subparser.set_defaults(func=main)

def main(args):
  ...

if __name__ == "__main__":
  print("invalid usage")