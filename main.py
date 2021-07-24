from splitter.splitter import split
import click


@click.group()
@click.version_option(package_name="fasta-splitter", message="%(prog)s version %(version)s")
def main_group():
    """
    Command line tool to split one multiple sequences fasta file into individual sequences fasta files.
    """


main_group.add_command(split)
