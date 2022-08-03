from typing import Iterator


from .repo import Repo


class Output(object):
    def out_repos(self, repos: Iterator[Repo]):
        name_padding = max(16, max(map(lambda r: len(r.name), repos)))
        for repo in repos:
            remotes = ", ".join(repo.remotes)
            print(f"{repo.name: <{name_padding}}: [{remotes}] {repo.path.absolute()}")