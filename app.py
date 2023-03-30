"""App test_radium module."""
import asyncio
import hashlib
import json
import tempfile
from os import listdir
from os.path import isfile

from decouple import config
from git.repo.base import Repo

list_hash = []


async def run_clone(path_to_repo: str) -> None:
    """Get content from path_to_repo in temporary dir.
    
    Args:
        path_to_repo: str

    """
    with tempfile.TemporaryDirectory() as dir_temp:
        Repo.clone_from(path_to_repo, dir_temp)
        generate_hash(dir_temp)


def generate_hash(dir_temp: str) -> None:
    """Write list with file's name add hash in json from dir_temp.
    
    Args:
        dir_temp: str
 
    """
    if isfile(dir_temp):
        with open(dir_temp, "rb") as f_o:
            file_hash = hashlib.sha256(f_o.read()).hexdigest()
            list_hash.append((dir_temp, file_hash))

    else:
        for dirobject in listdir(dir_temp):
            if not dirobject.startswith("."):
                generate_hash(
                    dir_temp="{path1}/{path2}".format(
                        path1=dir_temp,
                        path2=dirobject,
                    ),
                )


async def start():
    """Start module, controls another functions."""
    repo_url = config("GIT_REPO_URL")

    await asyncio.gather(
        run_clone(repo_url),
        run_clone(repo_url),
        run_clone(repo_url),
    )

    with open("output.json", "w") as f_o:
        json.dump(list_hash, f_o)


if __name__ == "__main__":
    asyncio.run(start())
