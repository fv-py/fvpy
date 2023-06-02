"""Some docstring"""

__all__ = ["__version__"]

import importlib.metadata

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    pass
