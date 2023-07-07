#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
