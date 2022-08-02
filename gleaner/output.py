from typing import Iterator


from .repo import Repo


class Output(object):
    def out_repos(self, repos: Iterator[Repo]):
        pass