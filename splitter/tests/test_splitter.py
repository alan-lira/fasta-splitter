from click.testing import CliRunner
import pytest
import splitter.splitter
import splitter.splitter_exceptions
import sys
import runpy


def test_when_execute_split_command_with_valid_argument_then_return_successful_exit_code_zero():
    valid_argument = ""
    runner = CliRunner()
    result = runner.invoke(splitter.splitter.splitter_group,
                           ["split", valid_argument])
    assert result.return_value is None
    assert result.exit_code == 0
    assert result.exc_info[0] == SystemExit
    assert result.exception is None


def test_when_execute_split_function_with_valid_argument_then_ok():
    sys.argv = ["", ""]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        runpy.run_path("splitter/splitter.py", run_name="__main__")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0
