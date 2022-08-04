import os
import pathlib
from typing import List


class Config(object):
    """Gleaner configuration.
    
    Attributes:
        includes    list of glob patterns to search git repositories.
        root        path to use to interpret configuration relative paths.
    """
    includes: List[str]
    root: pathlib.Path
    def __init__(self, includes: List[str]):
        self.includes = list(includes)
        self.root = pathlib.Path(os.getenv("HOME", "/"))