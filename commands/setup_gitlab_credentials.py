import os
from configparser import ConfigParser


def setup(args):
  CONFIG_PATH = '../config.ini'
  GITLAB = 'gitlab'
  ACCESS_TOKEN = 'access_token'

  config = ConfigParser()
  config.read(CONFIG_PATH)

  if not config.has_option(GITLAB, ACCESS_TOKEN):
    print("Please input your gitlab personal access token (i promise to keep it secret)")
    token = input()
    config.add_section(GITLAB)
    config.set(GITLAB, ACCESS_TOKEN, token)

    with open('config.ini', 'w') as f:
        config.write(f)
  else:
    print("You already told me your secret!")


def register(subparsers):
    parser = subparsers.add_parser("setup", help="Setup your gitlab credentials")
    parser.set_defaults(func=setup)
