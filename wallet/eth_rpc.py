# --*-- coding:utf8 --*--

from conf.env_conf import CONF

rpc_connection = CONF['eth_client']


def get_new_address(password):
    return rpc_connection.personal.newAccount(password)


def get_balance(address):
    return rpc_connection.getBalance(address)
