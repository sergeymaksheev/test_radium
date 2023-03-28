from os import listdir
from os.path import isfile
import asyncio
import hashlib
from git.repo.base import Repo

async def get_clone(workdir):
    """Get content from git repository in workdir."""
    return Repo.clone_from("https://gitea.radium.group/radium/project-configuration.git", workdir)


def get_hash(workdir):
    """Gets files hash."""
    if isfile(workdir):
        with open(workdir, 'rb') as f:
            res = hashlib.sha256(f.read()).hexdigest()
            print(res)
    else:
        for dirobject in listdir(workdir):
            if not dirobject.startswith("."):
                get_hash(workdir=f"{workdir}/{dirobject}")
        
        
def start():
    """Start module, controls another functions."""
    dir_lst = ["clone1", "clone2", "clone3"]
    clones = [
        asyncio.ensure_future(get_clone(dir_lst[0])),
        asyncio.ensure_future(get_clone(dir_lst[1])),
        asyncio.ensure_future(get_clone(dir_lst[2])),
    ]

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.gather(*clones))
    event_loop.close()

    for path in dir_lst:
        get_hash(path)  
        

if __name__ == '__main__':
    start()
