#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .api import API


class WalletAPI(API):
    def __init__(self, base_url, version):
        super(WalletAPI, self).__init__(base_url, version)

    def create(self, wallet_name: str):
        return self._client.post(url='wallet/create', data=wallet_name)

    def open(self, wallet_name: str):
        return self._client.post(url='wallet/open', data=wallet_name)

    def lock(self, wallet_name: str):
        return self._client.post(url='wallet/lock', data=wallet_name)

    def lock_all(self):
        return self._client.get(url="wallet/lock_all")

    def unlock(self, wallet_name: str, password: str):
        return self._client.post(url='wallet/unlock', data=[wallet_name, password])

    def import_key(self, wallet_name: str, password: str):
        return self._client.post(url='wallet/import_key', data=[wallet_name, password])

    def list_wallets(self):
        return self._client.get(url='wallet/list_wallets')

    def list_keys(self):
        return self._client.get(url='wallet/list_keys')

    def get_public_keys(self):
        return self._client.get(url='wallet/get_public_keys')

    def set_timeout(self, timeout: int):
        return self._client.post(url='wallet/set_timeout', data=timeout)

    def sign_trx(self, transactions: list):
        raise NotImplemented('sign_trx is not implemented')
