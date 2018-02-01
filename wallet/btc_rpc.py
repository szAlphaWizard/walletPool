################################################################################
#  Function: BitCoinRpc Client                                                 #
#                                                                              #
#                                                                              #
#                                                   WangYi 2018/1/31           #
#                                                                              #
#  pip install python-bitcoinrpc
################################################################################

from conf.env_conf import CONF

rpc_connection = CONF['btc_client']


def get_new_address(password):
    return rpc_connection.getnewaddress()
