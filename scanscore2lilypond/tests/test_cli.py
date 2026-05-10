import pytest
import os
import shutil
from click.testing import CliRunner
from scanscore2lilypond import cli
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
    output_file_step1 = os.path.join(test_folder, 'Pleyel_Presto_I_step1.xml')
    expected_output_step1 = os.path.join(
        test_folder, 'Expected_Pleyel_Presto_I_step1.xml')
    output_file_step2 = os.path.join(test_folder, 'Pleyel_Presto_I_step2.ly')
    expected_output_step2 = os.path.join(
        test_folder, 'Expected_Pleyel_Presto_I_step2.ly')
    output_file_step3 = os.path.join(test_folder, 'Pleyel_Presto_I_step3.ly')
    expected_output_step3 = os.path.join(
        test_folder, 'Expected_Pleyel_Presto_I_step3.ly')
    yield (input_file,
           output_file_step1, expected_output_step1,
           output_file_step2, expected_output_step2,
           output_file_step3, expected_output_step3)
    # Teardown code to clean up after the test
    if os.path.exists(output_file_step1):
        os.remove(output_file_step1)
    if os.path.exists(output_file_step2):
        os.remove(output_file_step2)
    if os.path.exists(output_file_step3):
        os.remove(output_file_step3)
    if os.path.exists(cli.change_step_and_extension(
            output_file_step2, old_step='_step2', new_step='_step2',
            new_extension='.ly~')):
        os.remove(cli.change_step_and_extension(
            output_file_step2, old_step='_step2', new_step='_step2',
            new_extension='.ly~'))
    if os.path.exists(cli.change_step_and_extension(
            output_file_step3, old_step='_step3', new_step='_step3',
            new_extension='.ly~')):
        os.remove(cli.change_step_and_extension(
            output_file_step3, old_step='_step3', new_step='_step3',
            new_extension='.ly~'))


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


def test_change_step_and_extension():
    filepath = '/path/to/file_step1.xml'
    expected_result = '/path/to/file_step2.ly'

    result = cli.change_step_and_extension(filepath)

    assert (result == expected_result)


def test_purge(runner: CliRunner, test_files: tuple[str, str, str]):
    (input_file,
     output_file_step1, expected_output_step1,
     output_file_step2, expected_output_step2,
     output_file_step3, expected_output_step3
     ) = test_files

    def fake_run_musicxml2ly(input_file, output_file):
        shutil.copyfile(expected_output_step2, output_file)
        return True

    with patch('scanscore2lilypond.cli.run_musicxml2ly',
               side_effect=fake_run_musicxml2ly):
        result = runner.invoke(cli.purge, ["-f", input_file])
    assert os.path.exists(output_file_step1)
    content_output_step1 = cli.file_content(output_file_step1)
    content_expected_step1 = cli.file_content(expected_output_step1)
    assert content_output_step1 == content_expected_step1
    assert os.path.exists(output_file_step2)
    content_output_step2 = cli.file_content(output_file_step2)
    content_expected_step2 = cli.file_content(expected_output_step2)
    assert content_output_step2 == content_expected_step2
    content_output_step3 = cli.file_content(output_file_step3)
    content_expected_step3 = cli.file_content(expected_output_step3)
    assert content_output_step3 == content_expected_step3
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
    with patch('os.path.isfile', return_value=False), \
            patch('shutil.which', return_value='musicxml2ly'), \
            patch('subprocess.check_call') as mock_check_call:
        assert run_musicxml2ly('input_file.xml', 'output_file.ly') is True
        mock_check_call.assert_called_with(
            ['musicxml2ly', '-o', 'output_file.ly', 'input_file.xml'])


def test_run_musicxml2ly_not_available():
    with patch('os.path.isfile', return_value=False), \
            patch('shutil.which', return_value=None), \
            patch('subprocess.check_call') as mock_check_call:
        assert run_musicxml2ly('input_file.xml', 'output_file.ly') is False
        mock_check_call.assert_not_called()


if __name__ == "__main__":
    pytest.main()
