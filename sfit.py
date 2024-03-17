import argparse
import importlib

commands = ["init", "add", "commit", "branch", "checkout", "merge", "tag"]

def parse_args() -> argparse.Namespace:
  # Top level parser
  parser = argparse.ArgumentParser()

  # Subparsers to parse subcommands
  subparsers = parser.add_subparsers(title="subcommands", required=True)
  
  # Import command modules
  # Each command has a module with the corresponding name in the commands directory
  
  # The module exposes an initialize function which takes the subparsers object and
  # adds a subparser for the command it represents

  # Also attaches the command handler function as func in the args namespace
  # This allows the parser to directly call the correct function from the
  # parsed args namespace in the main function
  
  for command in commands:
    command_module = importlib.import_module("commands." + command)
    command_module.initialize(subparsers)

  return parser.parse_args()

def main(args) -> int:
  if hasattr(args, "func"):
    args.func(args)
  else:
    print("invalid usage")

if __name__=="__main__":
  raise SystemExit(main(parse_args()))
