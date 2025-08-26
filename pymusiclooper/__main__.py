import logging

from pymusiclooper.cli import cli_main


def cli():
    try:
        cli_main(prog_name="pymusiclooper")  # pylint: disable=no-value-for-parameter
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    cli()
