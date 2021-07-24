from pathlib import Path
from click.testing import CliRunner
import pytest
import splitter.splitter
import splitter.splitter_exceptions
import sys
import runpy


def test_when_execute_split_command_without_sequences_file_path_argument_then_return_exit_error_code_one():
    runner = CliRunner()
    result = runner.invoke(splitter.splitter.splitter_group, ["split", ""])
    assert result.return_value is None
    assert result.exit_code == 1
    assert result.exc_info[0] == FileNotFoundError
    assert str(result.exception) == "FASTA sequences file not found!"


def test_when_execute_split_command_with_sequences_file_path_argument_then_return_successful_exit_code_zero():
    temporary_sequences_file = Path("sequences.fasta")
    with open(temporary_sequences_file, mode="w") as sequences_file:
        sequences_file.write(">Sequence1|text1\nAAA\n")
        sequences_file.write(">Sequence2 |text2\nCCC\n")
        sequences_file.write(">Sequence3\nGGG\n")
    runner = CliRunner()
    result = runner.invoke(splitter.splitter.splitter_group,
                           ["split", str(temporary_sequences_file)])
    assert result.return_value is None
    assert result.exit_code == 0
    assert result.exc_info[0] == SystemExit
    assert result.exception is None
    temporary_sequences_file.unlink()


def test_when_execute_main_function_without_sequences_file_path_argument_then_throws_file_not_found_exception():
    sys.argv = ["", ""]
    with pytest.raises(FileNotFoundError) as pytest_wrapped_e:
        runpy.run_path("splitter/splitter.py", run_name="__main__")
    assert pytest_wrapped_e.type == FileNotFoundError
    assert str(pytest_wrapped_e.value) == "FASTA sequences file not found!"
