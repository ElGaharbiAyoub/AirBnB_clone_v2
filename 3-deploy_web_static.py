#!/usr/bin/python3
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['54.146.56.232', '34.207.58.85']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


@runs_once
def do_pack():
    """
    generates a .tgz archive from the
    contents of the web_static folder
    """
    try:
        local('mkdir -p versions')
        name = "web_static_{}".format(
            datetime.now().strftime("%Y%m%d%H%M%S")
        )
        local("tar -cvzf versions/{}.tgz {}".format(
            name, "web_static/"))
        size = os.path.getsize("./versions/{}.tgz".format(name))
        print("web_static packed: versions/{}.tgz -> {}Bytes".format(
            name, size))
        return "versions/{}.tgz".format(name)
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Connect to the remote server
    """
    file_d = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/{}'.format(file_d))
        run('mkdir -p /data/web_static/releases/{}'.format(file_d))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            file_d, file_d))
        run('rm /tmp/{}'.format(file_d))
        run('mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/'.format(file_d, file_d))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            file_d))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
        /data/web_static/current'.format(file_d))
        print("New version deployed!")
        return True
    except Exception:
        print("New version not deployed!!!!!")
        return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    store_path = do_pack()
    if store_path is None:
        return False
    return do_deploy(store_path)
