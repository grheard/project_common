import argparse
import json
import os
import sys

from .logger import logger


def parse_command_line_arguments() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', nargs=1, default='', help='Configuration json in string or file form')
    args = parser.parse_args()

    if args.config:
        config = parse_config(args.config[0])
        if config is None:
            print('--config could not be reconciled. See log for details.')
            parser.print_help()
            sys.exit(1)
        return config


def parse_config(input) -> dict:
    try:
        # Try to parse a json object directly
        config = json.loads(input)
        logger.info("configuration successfully parsed from the command line.")
        return config
    except json.JSONDecodeError:
        logger.info(f"'{input}' is not JSON, it will be attempted as a file.")

    # Try loading it as a file
    if not os.path.isfile(input):
        logger.error(f"'{input}' is neither a JSON object or a file.")
        return None

    try:
        file = open(input)
    except OSError:
        logger.error(f"'{input}' cannot be opened.")
        return None

    try:
        config = json.load(file)
        logger.info(f"'{input}' successfully parsed.")
        return config
    except json.JSONDecodeError:
        logger.error(f"'{input}' does not contain a valid JSON object.")
        return None
