from argparse import ArgumentParser

def initialize(subparsers):
  subparser: ArgumentParser = subparsers.add_parser("add", help="stage changes made to file")
  subparser.set_defaults(func=main)

def main(args):
  ...

if __name__ == "__main__":
  print("invalid usage")