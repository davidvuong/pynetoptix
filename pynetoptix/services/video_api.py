# -*- coding: utf-8 -*-
from pynetoptix.core import http


class VideoApi:
    def __init__(self, config):
        self.config = config

    def _get_url(self, endpoint, **kwargs):
        qs = http.parse_qs(**kwargs)
        return '{endpoint}?{qs}'.format(endpoint=endpoint, qs=qs) if qs else endpoint

    def get_rtsp_stream_url(self, camera_id, **kwargs):
        """http://demo.networkoptix.com:7001/static/index.html#/developers/api/%3CcameraId%3E"""
        username = self.config.username
        password = self.config.password
        host = self.config.host
        port = self.config.port

        endpoint = 'rtsp://{username}:{password}@{host}:{port}/{camera_id}'.format(
            username=username,
            password=password,
            host=host,
            port=port,
            camera_id=camera_id,
        )
        return self._get_url(endpoint, **kwargs)

    def get_direct_download_url(self, camera_id, container_format, **kwargs):
        """http://demo.networkoptix.com:7001/static/index.html#/developers/api/hls/%3CcameraId%3E.%3Cformat%3E"""
        endpoint = '{endpoint}/hls/{camera_id}.{container_format}'.format(
            endpoint=self.config.endpoint,
            camera_id=camera_id,
            container_format=container_format,
        )
        return self._get_url(endpoint, **kwargs)

    def get_hls_stream_url(self, camera_id, **kwargs):
        """http://demo.networkoptix.com:7001/static/index.html#/developers/api/hls/%3CcameraId%3E.m3u"""
        endpoint = '{endpoint}/hls/{camera_id}.m3u'.format(endpoint=self.config.endpoint, camera_id=camera_id)
        return self._get_url(endpoint, **kwargs)

    def get_http_stream_url(self, camera_id, **kwargs):
        """http://demo.networkoptix.com:7001/static/index.html#/developers/api/media/%3CcameraId%3E.%3Cformat%3E"""
        endpoint = '{endpoint}/media/{camera_id}.webm'.format(endpoint=self.config.endpoint, camera_id=camera_id)
        return self._get_url(endpoint, **kwargs)
