# -*- coding: utf-8 -*-
from pynetoptix.core import http


class VideoApi:
    def __init__(self, config):
        self.config = config

    def get_rtsp_stream_url(self, camera_id, **kwargs):
        """http://demo.networkoptix.com:7001/static/index.html#/developers/api/%3CcameraId%3E"""
        endpoint = f'{self.config.endpoint}/{camera_id}'
        qs = http.parse_qs(**kwargs)
        return f'{endpoint}?{qs}' if qs else endpoint

    def get_direct_download_url(self, camera_id, container_format, **kwargs):
        """http://demo.networkoptix.com:7001/static/index.html#/developers/api/hls/%3CcameraId%3E.%3Cformat%3E"""
        endpoint = f'{self.config.endpoint}/hls/{camera_id}.{container_format}'
        qs = http.parse_qs(**kwargs)
        return f'{endpoint}?{qs}' if qs else endpoint
