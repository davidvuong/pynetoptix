# -*- coding: utf-8 -*-
from pynetoptix.core.config import Config
from pynetoptix.core.client import Client

from pynetoptix.services.system_api import SystemApi
from pynetoptix.services.server_api import ServerApi
from pynetoptix.services.video_api import VideoApi

__version_info__ = (0, 0, 5)
__version__ = '.'.join([str(i) for i in __version_info__])

__author__ = 'David Vuong'
__author_email__ = 'david.vuong256@gmail.com'


def create_client(username, password, host='localhost', port=7001, protocol='http'):
    config = Config(username, password, host, port, protocol)
    system_api = SystemApi(config)
    server_api = ServerApi(config)
    video_api = VideoApi(config)

    return Client(config, system_api, server_api, video_api)
