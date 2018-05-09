#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import requests


class Session(requests.Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super(Session, self).__init__()

    def request(self, method, url, **kwargs):
        url = urljoin(self.base_url, url)
        return super(Session, self).request(method, url, **kwargs)


class HttpClient(object):
    def __init__(self, base_url):
        self.session = Session(base_url)

    def get(self, url, **kwargs):
        return self._execute(method="GET", url=url, **kwargs)

    def post(self, url, **kwargs):
        return self._execute(method="POST", url=url, **kwargs)

    def delete(self, url, **kwargs):
        return self._execute(method="DELETE", url=url, **kwargs)

    def put(self, url, **kwargs):
        return self._execute(method="PUT", url=url, **kwargs)

    def _execute(self, method, url, **kwargs):
        try:
            res = self.session.request(method, url, **kwargs)
            res.raise_for_status()

            return res.json()
        except requests.HTTPError as e:
            raise e
        except Exception as e:
            raise e
