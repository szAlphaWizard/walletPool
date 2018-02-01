# --*-- coding:utf8 --*--
from jsonrpcserver.aio import methods


@methods.add
async def getSACBalance(address):
    return 100.0
