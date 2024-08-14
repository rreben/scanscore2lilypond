import pytest
import os
from click.testing import CliRunner
from scanscore2lilypond import cli
import subprocess
from unittest.mock import patch
from scanscore2lilypond.cli import run_musicxml2ly


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def test_files_path():
    return os.path.join(os.path.dirname(__file__), 'test_files')


@pytest.fixture
def test_files(test_files_path: str):
    test_folder = test_files_path
    input_file = os.path.join(test_folder, 'Pleyel_Presto_I.xml')
    output_file = os.path.join(test_folder, 'Pleyel_Presto_I_step1.xml')
    expected_output = os.path.join(
        test_folder, 'Expected_Pleyel_Presto_I_step1.xml')
    yield input_file, output_file, expected_output
    # Teardown code to clean up after the test
    if os.path.exists(output_file):
        os.remove(output_file)


def test_cli(runner: CliRunner):
    """
    Test the command line interface (CLI) function 'purge'
    in the scanscore2lilypond module which is called when
    starting the program from the command line.

    This test checks if the CLI function 'purge' returns
    the expected exit code and output
    when no 'FILENAME' argument is provided.
    """
    result = runner.invoke(cli.purge, [])
    assert result.exit_code == 2
    assert "Error: Missing argument 'FILENAME'." in result.output


def test_cli_help(runner: CliRunner):
    result = runner.invoke(cli.purge, ["--help"])
    assert result.exit_code == 0
    assert " [OPTIONS] FILENAME" in result.output
    assert "purges input file" in result.output


def test_non_existent_file(runner: CliRunner):
    result = runner.invoke(cli.purge, ["non_existent.xml"])
    assert result.exit_code == 1
    assert "Traceback" not in result.output
    assert "Error: File 'non_existent.xml' not found." in result.output
    # Add more assertions here based on the expected behavior of your code


def test_append_step_to_filename():
    filepath = '/path/to/file.xml'
    step_name = '_step1'
    expected_result = '/path/to/file_step1.xml'

    result = cli.append_step_to_filename(filepath, step_name=step_name)

    assert result == expected_result


def test_purge(runner: CliRunner, test_files: tuple[str, str, str]):
    input_file, output_file, expected_output = test_files

    result = runner.invoke(cli.purge, ["-f", input_file])
    assert os.path.exists(output_file)
    content_output = cli.file_content(output_file)
    content_expected = cli.file_content(expected_output)
    assert content_output == content_expected
    assert result.exit_code == 2


# This test checks if the run_musicxml2ly function correctly calls the
# musicxml2ly command with the expected arguments. It uses the
# unittest.mock.patch to mock subprocess.check_call and verifies that it
# is called with the correct parameters.
# Within the with block, subprocess.check_call is replaced by
# mock_check_call. Then, the function run_musicxml2ly is called with the
# arguments 'input_file.xml' and 'output_file.ly'.
# This test ensures that run_musicxml2ly passes the correct command to
# subprocess.check_call to perform the conversion from input_file.xml to
# output_file.ly. If the function does not call subprocess.check_call with
# the expected arguments, the test will fail.
def test_run_musicxml2ly_available():
    with patch('subprocess.check_call') as mock_check_call:
        run_musicxml2ly('input_file.xml', 'output_file.ly')
        mock_check_call.assert_called_with(
            ['musicxml2ly', '-o', 'output_file.ly', 'input_file.xml'])


def test_run_musicxml2ly_not_available():
    with patch('subprocess.check_call') as mock_check_call:
        mock_check_call.side_effect = subprocess.CalledProcessError(1, 'which')
        run_musicxml2ly('input_file.xml', 'output_file.ly')
        mock_check_call.assert_called_with(['which', 'musicxml2ly'])


if __name__ == "__main__":
    pytest.main()
