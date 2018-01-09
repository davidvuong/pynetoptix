# -*- coding: utf-8 -*-


class Config:
    def __init__(self, username, password, host, port, protocol):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.protocol = protocol

    @property
    def endpoint(self):
        return f'{self.protocol}://{self.username}:{self.password}@{self.host}:{self.port}'
