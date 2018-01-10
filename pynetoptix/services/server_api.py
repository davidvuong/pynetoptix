# -*- coding: utf-8 -*-
from pynetoptix.core import http


class ServerApi:
    def __init__(self, config):
        self.config = config

    def ping(self):
        return http.get(f'{self.config.endpoint}/api/ping', headers=self.config.headers)

    def create_event(self, **kwargs):
        endpoint = f'{self.config.endpoint}/api/createEvent'

        if 'source' not in kwargs and 'caption' not in kwargs and 'description' not in kwargs:
            raise ValueError('Either source, caption, or description must be set')
        return http.get(endpoint, headers=self.config.headers)
