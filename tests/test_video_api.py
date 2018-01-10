import pynetoptix
import uuid


class TestVideoApi:
    vms_host = 'demo.networkoptix.com'
    vms_port = 7001
    client = pynetoptix.create_client('demo', 'nxwitness', host=vms_host, port=vms_port)

    def test_get_rtsp_stream_url_allow_regular_camera_id(self):
        camera_id = uuid.uuid4()
        assert self.client.video.get_rtsp_stream_url(camera_id) == f'http://{self.vms_host}:{self.vms_port}/{camera_id}'
