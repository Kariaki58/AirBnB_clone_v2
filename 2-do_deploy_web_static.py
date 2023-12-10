#!/usr/bin/python3
"""importing... modules"""
from fabric.api import run, put, env
from os.path import exists


env.hosts = ["100.25.179.45", "100.25.30.209"]

def do_deploy(archive_path):
    """do deploy"""
    check_file = exists(archive_path)
    if not check_file:
        return False
    put(archive_path, "/tmp/")

    archive_filename = archive_path.split("/")[-1]
    release_path = "/data/web_static/releases/{}".format(
            archive_filename[:-4]
            )
    print("here")
    run("mkdir -p {}".format(release_path))
    run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))

    run("rm /tmp/{}".format(archive_filename))

    run("mv {}/web_static/* {}".format(release_path, release_path))

    run("rm -rf {}/web_static".format(release_path))

    run("rm -rf /data/web_static/current")

    run("ln -s {} /data/web_static/current".format(release_path))

    print("New version deployed!")
    return True


if __name__ == "__main__":
    """entry point"""
    archive_path = "versions/web_static_20231209082910.tgz"

    private_key_path = "~/.ssh/id_rsa"
    username = "ubuntu"

    result = do_deploy(archive_path)

    if result:
        print("Deployment successful!")
    else:
        print("Deployment failed!") 

