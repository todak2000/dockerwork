#!/user/bin/env python
import click

@click.command()
def hello():
    click.echo("Hell WOrld!")


if __name__ == '__main__':
    hello()