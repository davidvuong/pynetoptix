# -*- coding: utf-8 -*-


class Client:
    def __init__(self, config, system_api, server_api, video_api):
        self.config = config
        self.system = system_api
        self.server = server_api
        self.video = video_api
