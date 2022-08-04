import pathlib
from typing import List


class Repo(object):
    path: pathlib.Path
    name: str
    remotes: List[str]
    def __init__(self, path, name, remotes):
        self.path = path
        self.name = name
        self.remotes = remotes