import textwrap

import click

from modern_python_valbaca import wikipedia

from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern python project"""
    data = wikipedia.random_page()
    title = data["title"]
    extract = data["extract"]
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
