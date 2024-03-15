import argparse

def parse_args()->argparse.Namespace:
  ...

def main(args) -> int:
  return 0


if __name__=="__main__":
  raise SystemExit(main(parse_args()))
