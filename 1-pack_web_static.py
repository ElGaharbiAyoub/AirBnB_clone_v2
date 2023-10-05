#!/usr/bin/python3
import os
from fabric.api import *
from datetime import datetime


def do_pack():
    try:
        local('mkdir -p versions')
        name = "web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S")
        )
        local("tar -cvzf versions/{}.tgz {}".format(
            name, "web_static/"))
        return "versions/{}".format(name)
    except Exception as e:
        return None
