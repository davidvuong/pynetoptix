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
        return '{protocol}://{host}:{port}'.format(
            protocol=self.protocol,
            host=self.host,
            port=self.port,
        )

    @property
    def headers(self):
        auth = '{username}:{password}'.format(username=self.username, password=self.password).encode('utf-8')
        basic_auth = base64.b64encode(auth).decode('utf-8')
        return {
            'Authorization': 'Basic {basic_auth}'.format(basic_auth=basic_auth),
        }
