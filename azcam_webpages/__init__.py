"""
azcam-webpages is an azcam extension which adds certain web pages to the default azcam web server.
"""

import typing
from typing import List, Dict
from importlib import metadata

__version__ = metadata.version(__package__)
__version_info__ = tuple(int(i) for i in __version__.split(".") if i.isdigit())
