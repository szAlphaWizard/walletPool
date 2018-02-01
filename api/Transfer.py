# --*-- coding:utf --*--
from jsonrpcserver.aio import methods


@methods.add
async def pullSAC(address):
    return True

@methods.add
async def transferSAC(address):
    return True
