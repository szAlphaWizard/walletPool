# --*-- coding:utf8 --*--
from jsonrpcserver.aio import methods
from wallet import btc_rpc, eth_rpc


@methods.add
async def open(password):
    d = {
        1: btc_rpc.get_new_address(password),
        2: eth_rpc.get_new_address(password),
        3: eth_rpc.get_new_address(password)
    }
    return d

