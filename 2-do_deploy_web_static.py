#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers using do_deploy
"""

from fabric.api import *
from os.path import exists
env.hosts = ['54.197.122.71', '34.207.61.76']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        archive_no_ext = archive_name.split(".")[0]
        path = "/data/web_static/releases/{}".format(archive_no_ext)

        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, path))

        run("rm /tmp/{}".format(archive_name))

        run("mv {}/web_static/* {}".format(path, path))

        run("rm -rf {}/web_static".format(path))

        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(path))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
