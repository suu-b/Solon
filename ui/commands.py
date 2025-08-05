import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}!")


@app.command()
def add(x: int, y: int):
    print("Adding...")
    print(f"{x} + {y} = {x + y}")