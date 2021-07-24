from pathlib import Path
import click
import splitter.splitter_exceptions
import sys


@click.group()
def splitter_group() -> None:
    pass


@splitter_group.command("split", short_help="Split one multiple sequences file into individual sequences files.")
@click.argument("sequences_file_path", nargs=1, type=Path, required=True)
def split(sequences_file_path: Path) -> None:
    """
    Split one multiple sequences fasta file into individual sequences fasta files.\n
    """
    # BEGIN

    # END
    sys.exit(0)


if __name__ == "__main__":
    split()
