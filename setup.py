"""Setup script for ``binarymap``."""

import re
import sys

from setuptools import setup


if not (sys.version_info[0] == 3 and sys.version_info[1] >= 8):
    raise RuntimeError(
        "binarymap requires Python >=3.8.\n"
        f"You are using {sys.version_info[0]}.{sys.version_info[1]}."
    )

# get metadata from package `__init__.py` file as here:
# https://packaging.python.org/guides/single-sourcing-package-version/
metadata = {}
init_file = "binarymap/__init__.py"
with open(init_file) as f:
    init_text = f.read()
for dataname in ["version", "author", "email", "url"]:
    matches = re.findall("__" + dataname + r'__\s+=\s+[\'"]([^\'"]+)[\'"]', init_text)
    if len(matches) != 1:
        raise ValueError(
            f"found {len(matches)} matches for {dataname} " f"in {init_file}"
        )
    else:
        metadata[dataname] = matches[0]

with open("README.rst") as f:
    readme = f.read()

# main setup command
setup(
    name="binarymap",
    version=metadata["version"],
    author=metadata["author"],
    author_email=metadata["email"],
    url=metadata["url"],
    download_url="https://github.com/jbloomlab/binarymap/tarball/"
    + metadata["version"],  # tagged version on GitHub
    description="Binary representation of protein or nucleotide sequences.",
    long_description=readme,
    license="GPLv3",
    install_requires=[
        "natsort>=0.8",
        "pandas>=1.2",
        "scipy>=1.1",
    ],
    platforms="Linux and Mac OS X.",
    packages=["binarymap"],
    package_dir={"binarymap": "binarymap"},
)
