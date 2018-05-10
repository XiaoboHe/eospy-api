#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json as jsonpickle

from .api import API


class ChainAPI(API):
    def __init__(self, base_url, version):
        super(ChainAPI, self).__init__(base_url, version)

    def get_info(self):
        return self._client.get(url='chain/get_info')

    def get_block(self, block_num_or_id):
        return self._client.post(url='chain/get_block', json=dict(block_num_or_id=block_num_or_id))

    def get_account(self, account_name):
        return self._client.post(url='chain/get_account', json=dict(account_name=account_name))

    def get_code(self, account_name):
        return self._client.post(url='chain/get_code', json=dict(account_name=account_name))

    def get_table_rows(self, scope, code, table, json=True, lower_bound=None, upper_bound=None, limit=None):
        return self._client.post(url='chain/get_table_rows',
                                 json=dict(scope=scope, code=code, table=table,
                                           json=json, lower_bound=lower_bound, upper_bound=upper_bound, limit=limit))

    def abi_json_to_bin(self, code, action, args):
        self._client.post(url='chain/abi_json_to_bin', json=dict(code=code, action=action, args=jsonpickle.dumps(args)))

    def abi_bin_to_json(self, code, action, binargs):
        return self._client.post(url='chain/abi_bin_to_json', json=dict(code=code, action=action, binargs=binargs))

    def push_transaction(self, transactions: list):
        return self._client.post(url='chain/push_transactions', data=transactions)

    def get_required_keys(self, transaction: dict, available_keys: list):
        data = {
            'transaction': transaction,
            'available_keys': available_keys
        }
        return self._client.post(url='chain/get_required_keys', json=data)
