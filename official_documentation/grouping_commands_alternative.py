"""For simple scripts"""

import click


@click.group()
def cli():
    pass


@cli.command()
def init_db():
    click.echo('Initialized the database')


@cli.command()
def drop_db():
    click.echo('Dropped the database')

if __name__ == '__main__':
    cli()
