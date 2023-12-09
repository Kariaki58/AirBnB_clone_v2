#!/usr/bin/python3
"""
modules for fabric and datetim
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Compress before sending
    """
    cmd = "mkdir -p versions"
    local(cmd)

    archive_name = "web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))

    output = local("tar -cvzf versions/{} web_static".format(archive_name))
    if output.succeeded:
        return "versions/{}".format(archive_name)
    return None


if __name__ == "__main__":
    """entry function"""
    do_pack()
