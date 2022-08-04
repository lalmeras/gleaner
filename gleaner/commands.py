import pathlib
from typing import List

import git

from .config import Config
from .repo import Repo


class RepoCommand(object):
    def __init__(self, config: Config):
        self.config = config


    def scan(self) -> List[Repo]:
        repos: List[Repo] = []
        for pattern in self.config.includes:
            git_pattern = pattern + "/.git"
            candidates = self.config.root.glob(git_pattern)
            for candidate in candidates:
                rpath = candidate.parent
                grepo = git.Repo(rpath)
                name = rpath.name
                try:
                    if not "Unnamed repository" in grepo.description:
                        name = grepo.description
                except Exception:
                    pass
                remotes = list(map(lambda r: r.name, grepo.remotes))
                repos.append(Repo(rpath, name, remotes))
        return repos