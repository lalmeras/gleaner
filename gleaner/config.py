import os
import pathlib


class Config(object):
    """Gleaner configuration.
    
    Attributes:
        includes    list of glob patterns to search git repositories.
        root        path to use to interpret configuration relative paths.
    """
    includes: list[str]
    root: pathlib.Path
    def __init__(self, includes: list[str]):
        self.includes = list(includes)
        self.root = pathlib.Path(os.getenv("HOME", "/"))