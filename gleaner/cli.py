import sys

import click

from .output import Output
from .commands import RepoCommand
from .config import Config
from .cliutil import make_pass_decorator


pass_config = make_pass_decorator(Config)
pass_repo_command = make_pass_decorator(RepoCommand)
pass_output = make_pass_decorator(Output)


@click.group(name = "gleaner")
@click.pass_context
def main(ctx):
    ctx.ensure_object(dict)
    ctx.obj[Config] = Config()
    ctx.obj[Output] = Output()


@main.group(name = "repo")
@pass_config
@click.pass_context
def repo(ctx, config):
    ctx.obj[RepoCommand] = RepoCommand(config)


@repo.command(name = "list")
@pass_output
@pass_repo_command
@click.pass_context
def repo_list(ctx, repo_command, output):
    """List repositories from configuration."""
    repos = repo_command.scan()
    output.out_repos(repos)
    

if __name__ == "__main__":
    main()