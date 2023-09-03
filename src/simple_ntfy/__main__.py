"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Simple ntfy."""


if __name__ == "__main__":
    main(prog_name="simple-ntfy")  # pragma: no cover
