# --*-- coding:utf8 --*--
from jsonrpcserver.aio import methods


@methods.add
def getSACBalance(address):
    return 100.0
