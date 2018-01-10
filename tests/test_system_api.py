import pynetoptix
import uuid


class TestSystemApi:
    client = pynetoptix.create_client('demo', 'nxwitness', host='demo.networkoptix.com')

    def test_get_cameras_ex_responds_with_all_cameras(self):
        assert isinstance(self.client.system.get_cameras_ex(), list)

    def test_get_cameras_ex_with_missing_camera_id(self):
        camera_id = str(uuid.uuid4())
        assert len(self.client.system.get_cameras_ex(camera_id)) == 0
