# -*- coding: utf-8 -*-
import base64


class Config:
    def __init__(self, username, password, host, port, protocol):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.protocol = protocol

    @property
    def endpoint(self):
        return f'{self.protocol}://{self.host}:{self.port}'

    @property
    def headers(self):
        basic_auth = base64.b64encode(f'{self.username}:{self.password}'.encode('utf-8')).decode('utf-8')
        return {
            'Authorization': f'Basic {basic_auth}',
        }
