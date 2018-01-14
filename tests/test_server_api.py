import pynetoptix
import pytest


class TestServerApi:
    client = pynetoptix.create_client('demo', 'nxwitness', host='demo.networkoptix.com')

    def test_ping_responds_with_pong(self):
        assert self.client.server.ping()['error'] == '0'

    def test_create_event_denies_empty_args(self):
        with pytest.raises(ValueError):
            self.client.server.create_event()

    def test_create_event_allows_with_req_args(self):
        assert self.client.server.create_event(source='camera_id')['error'] == '0'

    def test_get_event_rules_responds_with_rules(self):
        assert isinstance(self.client.server.get_event_rules(), list)
