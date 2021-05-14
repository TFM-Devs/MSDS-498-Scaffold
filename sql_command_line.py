import click

@click.command(help='this is just a basic app')
@click.option('--name', prompt="I need your name", help="Need name")
@click.option('--color', prompt='I need your color', help="Need color")

def hello(name, color):
    if name == 'Thor':
        click.echo("Thor you are always red")
        click.echo(click.style(f"Hello World! {name}", fg="red"))
    else:
        click.echo(click.style(f"Hello World! {name}", fg="color"))
        
if __name__ == '__main__':
    hello()
    
    