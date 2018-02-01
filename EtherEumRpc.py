################################################################################
#  Function: EtherEum Client                                                  #
#                                                                              #
#                                                                              #
#                                                   WangYi 2018/1/31           #
#                                                                              #
################################################################################

from ethjsonrpc import EthJsonRpc
rpc_connection = EthJsonRpc('127.0.0.1', 8545)

print(rpc_connection.net_version()£©
print(rpc_connection.web3_clientVersion()£©
print(rpc_connection.eth_gasPrice()£©
print(rpc_connection.eth_blockNumber()£©
    