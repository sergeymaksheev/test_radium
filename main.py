from os import listdir
from os.path import isfile
import tempfile
import asyncio
import hashlib
from git.repo.base import Repo
from decouple import config


async def get_clone():
    """Get content from git repository in temporary dir."""
    with tempfile.TemporaryDirectory() as dir_temp:
        Repo.clone_from(config('GIT_REPO_URL'), dir_temp)
        get_hash(dir_temp)


def get_hash(dir_temp: str):
    """Gets files hash."""
    if isfile(dir_temp):
        with open(dir_temp, 'rb') as file:
            file_hash = hashlib.sha256(file.read()).hexdigest()
            print(file_hash) 
    else:
        for dirobject in listdir(dir_temp):
            if not dirobject.startswith("."):
                get_hash(dir_temp=f"{dir_temp}/{dirobject}")
        
        
def start():
    """Start module, controls another functions."""
    clones = [
        asyncio.ensure_future(get_clone()),
        asyncio.ensure_future(get_clone()),
        asyncio.ensure_future(get_clone()),
    ]

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.gather(*clones))
    event_loop.close()


if __name__ == '__main__':
    start()
