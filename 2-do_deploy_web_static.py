#!/usr/bin/python3
"""Fabric script to deploy web_static"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['54.197.122.71', '34.207.61.76']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy web_static to web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/
        filename = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/{}".format(
            filename.split(".")[0])
        run("sudo mkdir -p {}".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C {}".format(filename, folder_name))

        # Delete the archive from the web server
        run("sudo rm /tmp/{}".format(filename))

        # Move contents to the proper location
        run("sudo mv {}/web_static/* {}".format(folder_name, folder_name))

        # Remove the web_static directory
        run("sudo rm -rf {}/web_static".format(folder_name))

        # Remove the current symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("sudo ln -s {} /data/web_static/current".format(folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
