#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from urllib.parse import urljoin

from core.http_client import HttpClient


class ChainAPI:
    def __init__(self, base_url, version):
        self.client = HttpClient(urljoin(base_url, '{}/'.format(version)))

    def get_info(self):
        return self.client.get(url='chain/get_info')

    def get_block(self, block_num_or_id):
        return self.client.post(url='chain/get_block', json=dict(block_num_or_id=block_num_or_id))

    def get_account(self, account_name):
        return self.client.post(url='chain/get_account', json=dict(account_name=account_name))

    def get_code(self, account_name):
        return self.client.post(url='chain/get_code', json=dict(account_name=account_name))

    def get_table_rows(self, scope, code, table, json=True, lower_bound=None, upper_bound=None, limit=None):
        return self.client.post(url='chain/get_table_rows',
                                json=dict(scope=scope, code=code, table=table,
                                          json=json, lower_bound=lower_bound, upper_bound=upper_bound, limit=limit))

    def abi_json_to_bin(self, code, action, args):
        self.client.post(url='chain/abi_json_to_bin', json=dict(code=code, action=action, args=json.dumps(args)))

    def abi_bin_to_json(self, code, action, binargs):
        return self.client.post(url='chain/abi_bin_to_json', json=dict(code=code, action=action, binargs=binargs))
