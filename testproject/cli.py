# -*- coding: utf-8 -*-

"""Console script for testproject."""

import click


@click.command()
def main(args=None):
    """Console script for testproject."""
    click.echo("Replace this message by putting your code into "
               "testproject.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
