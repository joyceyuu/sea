"""Sea command line interface."""
import logging
import click
from typing import Any
from sea.model import classify as _classify


@click.group()
@click.option('--verbosity',
              type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR']),
              default='INFO', help='Logging level')
def cli(verbosity):
    """Docstring."""
    lg = logging.getLogger("")
    lg.setLevel(verbosity)


@cli.command()
def classify() -> Any:
    """Apply regression models to data."""
    _classify()
