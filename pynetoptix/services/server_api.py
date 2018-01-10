# -*- coding: utf-8 -*-
from pynetoptix.core import http
import urllib.parse


class ServerApi:
    def __init__(self, config):
        self.config = config

    def ping(self):
        return http.get(f'{self.config.endpoint}/api/ping', headers=self.config.headers)

    def create_event(self, **kwargs):
        endpoint = f'{self.config.endpoint}/api/createEvent'

        if 'source' not in kwargs and 'caption' not in kwargs and 'description' not in kwargs:
            raise ValueError('Either source, caption, or description must be set')

        qs = {k: v for k, v in kwargs.items() if v is not None}
        qs = urllib.parse.urlencode(qs)
        endpoint = f'{endpoint}?{qs}' if qs else endpoint

        return http.get(endpoint, headers=self.config.headers)
