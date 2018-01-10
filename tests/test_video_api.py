import pynetoptix
import uuid


class TestVideoApi:
    vms_host = 'demo.networkoptix.com'

    client = pynetoptix.create_client('demo', 'nxwitness', host='demo.networkoptix.com')

    def test_get_rtsp_stream_url_allow_regular_camera_id(self):
        camera_id = uuid.uuid4()
        assert self.client.video.get_rtsp_stream_url(camera_id) == f'http://{self.vms_host}:7001/{camera_id}'
