#!/usr/bin/python3
"""importing modules"""
from fabric.api import env, put, run
from os.path import exists


env.hosts = ["100.25.179.45", "100.25.30.209"]


def do_deploy(archive_path):
    """deploy function"""
    if not exists(archive_path):
        return False
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(
        name
        )).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(
        name
        )).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
        file_name, name
        )).failed is True:
        return False
    if run("rm /tmp/{}".format(
        file_name
        )).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
