import click
import sys
import json

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

stdin = getattr(sys.stdin, 'buffer', sys.stdin)
#print(stdin.read())
args = json.loads(stdin.read().decode('utf-8'))
print(args)
#if __name__ == '__main__':
#    hello()