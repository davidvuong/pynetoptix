# -*- coding: utf-8 -*-
import json
import urllib.parse
import urllib.request


def get(endpoint, headers=None):
    headers = headers or {}

    url_request = urllib.request.Request(endpoint)
    url_request.add_header('Content-Type', 'application/json; charset=utf-8')

    for key, value in headers.items():
        url_request.add_header(key, value)

    response = urllib.request.urlopen(url_request)
    data = response.read().decode(response.headers.get_content_charset() or 'utf-8')
    return json.loads(data)


def post(endpoint, payload=None, headers=None):
    payload = payload or {}
    headers = headers or {}

    data = json.dumps(payload)
    data = data.encode('utf-8')

    # Define default headers before allowing custom headers to override
    url_request = urllib.request.Request(endpoint, method='POST')
    url_request.add_header('Content-Type', 'application/json; charset=utf-8')
    url_request.add_header('Content-Length', len(data))

    for key, value in headers.items():
        url_request.add_header(key, value)

    response = urllib.request.urlopen(url_request, data)
    data = response.read().decode(response.headers.get_content_charset() or 'utf-8')
    return json.loads(data)


def parse_qs(**kwargs):
    return '&'.join([f'{k}={urllib.parse.quote(str(v))}' for k, v in kwargs.items() if v is not None])
