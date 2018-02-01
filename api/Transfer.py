# --*-- coding:utf --*--
from jsonrpcserver.aio import methods


@methods.add
def pullSAC(address):
    return True

@methods.add
def transferSAC(address):
    return True
