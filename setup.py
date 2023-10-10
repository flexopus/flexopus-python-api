from setuptools import setup, find_packages
from subprocess import Popen, PIPE

def get_version_hash():
    """Talk to git and find out the tag/hash of our latest commit"""
    try:
        p = Popen(["git", "describe",
                   "--tags", "--dirty", "--always"],
                    stdout=PIPE)
    except EnvironmentError:
        print("Couldn't run git to get a version number for setup.py")
        return
    ver = p.communicate()[0]
    return ver.strip()

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="flexopus",
    version=get_version_hash(),
    author="Sebi Nemeth",
    author_email="sebezhetetlen98@gmail.com",
    description="Python package to interact with th Flexopus API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flexopus/flexopus-python-api",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp',
    ],
)