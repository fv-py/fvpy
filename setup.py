#!/usr/bin/env python

import os
from extension_helpers import get_extensions
from setuptools import setup

VERSION_TEMPLATE = """
# Note : hard-coding version to '0.1.dev' if setuptools_scm does not find a version.
# TODO : Try to make setuptools_scm to work !
try:
    from setuptools_scm import get_version
    version = get_version(root="..", relative_to=__file__)
except Exception:
    version = '{version}'
""".lstrip()

setup(
    use_scm_version={
        "write_to": os.path.join("fvpy", "version.py"),
        "write_to_template": VERSION_TEMPLATE,
    },
    ext_modules=get_extensions(),
)
