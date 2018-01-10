# -*- coding: utf-8 -*-
import urllib.parse


class VideoApi:
    def __init__(self, config):
        self.config = config

    def get_rtsp_stream_url(self, camera_id, **kwargs):
        endpoint = f'{self.config.endpoint}/{camera_id}'
        qs = {k: v for k, v in kwargs.items() if v is not None}
        qs = urllib.parse.urlencode(qs)

        return f'{endpoint}?{qs}' if qs else endpoint
