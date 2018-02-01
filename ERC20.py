################################################################################
#  Function: BitCoinRpc Client                                                 #
#                                                                              #
#                                                                              #
#                                                   WangYi 2018/1/31           #
#                                                                              #
#  pip install python-bitcoinrpc
################################################################################

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
#import logging

#logging.basicConfig()
#logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)

rpc_connection = AuthServiceProxy("http://test:123456@127.0.0.1:19010")

print("getinfo:")
print(rpc_connection.getinfo())

print("getnewaddress:")
print(rpc_connection.getnewaddress())