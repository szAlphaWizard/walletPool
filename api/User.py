# --*-- coding:utf8 --*--
from jsonrpcserver.aio import methods


@methods.add
async def open(password):
    d = {
        1: "0x3ae88fe370c39384fc16da2c9e768cf5d2495b48",
        2: "0x81063419f13cab5ac090cd8329d8fff9feead4a0",
        3: "0xca9f427df31a1f5862968fad1fe98c0a9ee068c4"
    }
    return d

