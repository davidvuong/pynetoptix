import pynetoptix
import uuid


class TestVideoApi:
    vms_host = 'demo.networkoptix.com'
    vms_port = 7001
    username = 'demo'
    password = 'port'
    client = pynetoptix.create_client(username, password, host=vms_host, port=vms_port)

    def test_get_rtsp_stream_url_allow_empty_args(self):
        camera_id = uuid.uuid4()
        host = self.vms_host
        port = self.vms_port
        username = self.username
        password = self.password

        url = 'rtsp://{username}:{password}@{host}:{port}/{camera_id}'.format(
            username=username,
            password=password,
            host=host,
            port=port,
            camera_id=camera_id,
        )
        assert self.client.video.get_rtsp_stream_url(camera_id) == url

    def test_get_direct_download_url_allow_empty_args(self):
        camera_id = uuid.uuid4()
        container_format = 'mkv'
        url = 'http://{vms_host}:{vms_port}/hls/{camera_id}.{container_format}'.format(
            vms_host=self.vms_host,
            vms_port=self.vms_port,
            camera_id=camera_id,
            container_format=container_format,
        )
        assert self.client.video.get_direct_download_url(camera_id, container_format) == url

    def test_get_direct_download_url_encodes_qs(self):
        camera_id = uuid.uuid4()
        container_format = 'mkv'
        duration = 10

        url = 'http://{vms_host}:{vms_port}/hls/{camera_id}.{container_format}?duration={duration}'.format(
            vms_host=self.vms_host,
            vms_port=self.vms_port,
            camera_id=camera_id,
            container_format=container_format,
            duration=duration,
        )
        assert self.client.video.get_direct_download_url(camera_id, container_format, duration=duration) == url

    def test_get_hls_stream_url_allow_empty_args(self):
        camera_id = uuid.uuid4()
        url = 'http://{vms_host}:{vms_port}/hls/{camera_id}.m3u'.format(
            vms_host=self.vms_host,
            vms_port=self.vms_port,
            camera_id=camera_id,
        )
        assert self.client.video.get_hls_stream_url(camera_id) == url

    def test_get_http_stream_url_allow_empty_args(self):
        camera_id = uuid.uuid4()
        url = 'http://{vms_host}:{vms_port}/media/{camera_id}.webm'.format(
            vms_host=self.vms_host,
            vms_port=self.vms_port,
            camera_id=camera_id,
        )
        assert self.client.video.get_http_stream_url(camera_id) == url
