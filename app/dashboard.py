import typer

app = typer.Typer(help="View dashboards and project summaries")

@app.command()
def show(all: bool = False, open: bool = False, done: bool = False, closed: bool = False):
    """
    Show dashboard of projects.
    
    Options:
        --all     : Show all projects
        --open    : Show only open projects
        --done    : Show only completed projects
        --closed  : Show only closed projects
    
    Example:
        solon dashboard show --all
    """
    filters = []
    if all:
        filters.append("all")
    if open:
        filters.append("open")
    if done:
        filters.append("done")
    if closed:
        filters.append("closed")
    
    if not filters:
        filters.append("all")
    
    print(f"Showing dashboard with filters: {', '.join(filters)}")
    # TODO: Fetch projects from DB and display
