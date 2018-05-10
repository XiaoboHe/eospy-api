#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import urljoin

from core.http_client import HttpClient


class API:
    def __init__(self, base_url, version):
        if version not in ['v1']:
            raise ValueError('api version is not be supported.')

        self._client = HttpClient(urljoin(base_url, '{}/'.format(version)))
