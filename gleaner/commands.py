from .config import Config
from .repo import Repo


class RepoCommand(object):
    def __init__(self, config: Config):
        self.config = config


    def scan(self) -> list[Repo]:
        pass