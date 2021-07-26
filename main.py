import splitter.splitter
import click


def print_supported_fasta_file_extensions(ctx, _, value) -> None:
    if not value or ctx.resilient_parsing:
        return
    click.echo("Supported fasta file extensions: " + str(splitter.splitter.get_supported_fasta_file_extensions())
               .replace("[", "").replace("]", "").replace("'", ""))
    ctx.exit(0)


@click.group()
@click.version_option(package_name="fasta-splitter", message="%(prog)s version %(version)s")
@click.option("--supported-extensions",
              callback=print_supported_fasta_file_extensions,
              is_flag=True,
              expose_value=False,
              is_eager=True,
              help="Show the supported fasta file extensions and exit.")
def main_group():
    """
    Command line tool to split one multiple sequences fasta file into individual sequences fasta files.
    """


main_group.add_command(splitter.splitter.split)
