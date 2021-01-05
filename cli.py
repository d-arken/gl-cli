#!/usr/bin/env python3
import argparse
import sys
import importlib


MODULES = ['setup_gitlab_credentials']

def _build_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser()
  parser.set_defaults(func=None)

  subparsers = parser.add_subparsers(help="sub-commands")

  imports = (
    "commands.%s" % module for module in MODULES
  )
  
  for module in (importlib.import_module(name) for name in imports):
    module.register(subparsers)

  return parser
  

def main():
  parser = _build_parser()

  args = parser.parse_args()

  if args.func is None:
    parser.print_usage()
    sys.exit(1)
  
  args.func(args)


if __name__ == "__main__":
  main()