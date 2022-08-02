import sys

from click.testing import CliRunner

from pytest import fixture
from unittest.mock import call, patch, sentinel


@fixture()
def cli_runner():
    return CliRunner()


@fixture()
def repo_command():
    with patch("gleaner.commands.RepoCommand") as p:
        yield p


@fixture()
def output():
    with patch("gleaner.output.Output") as p:
        yield p


def test_repo_list(cli_runner, repo_command, output):
    from gleaner.cli import main
    result = cli_runner.invoke(main, ["repo", "list"])
    repo_command().scan.assert_called_once()
    output().out_repos.assert_called_once_with(repo_command().scan())

