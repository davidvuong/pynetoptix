import pynetoptix
import uuid


class TestVideoApi:
    vms_host = 'demo.networkoptix.com'
    vms_port = 7001
    client = pynetoptix.create_client('demo', 'nxwitness', host=vms_host, port=vms_port)

    def test_get_rtsp_stream_url_allow_empty_args(self):
        camera_id = uuid.uuid4()
        url = f'http://{self.vms_host}:{self.vms_port}/{camera_id}'
        assert self.client.video.get_rtsp_stream_url(camera_id) == url

    def test_get_direct_download_url_allow_empty_args(self):
        camera_id = uuid.uuid4()
        container_format = 'mkv'
        url = f'http://{self.vms_host}:{self.vms_port}/hls/{camera_id}.{container_format}'
        assert self.client.video.get_direct_download_url(camera_id, container_format) == url

    def test_get_direct_download_url_encodes_qs(self):
        camera_id = uuid.uuid4()
        container_format = 'mkv'
        duration = 10

        url = f'http://{self.vms_host}:{self.vms_port}/hls/{camera_id}.{container_format}?duration={duration}'
        assert self.client.video.get_direct_download_url(camera_id, container_format, duration=duration) == url
