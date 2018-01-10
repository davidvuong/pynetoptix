# -*- coding: utf-8 -*-
from pynetoptix.core import http


class SystemApi:
    def __init__(self, config):
        self.config = config

    def get_cameras_ex(self, camera_id=None):
        endpoint = f'{self.config.endpoint}/ec2/getCamerasEx'

        if camera_id is not None:
            endpoint = f'{endpoint}?id={camera_id}'
        return http.get(endpoint, headers=self.config.headers)
