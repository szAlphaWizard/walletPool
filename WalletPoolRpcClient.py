################################################################################
#  Function: TestRpc Client                                                    #
#                                                                              #
#                                                                              #
#                                                   WangYi 2018/1/31           #
#  pip install  jsonrpcclient[requests]                                                                          #
################################################################################

from jsonrpcclient.http_client import HTTPClient
response = HTTPClient('http://127.0.0.1:5000/').request('get_address','BTC')
print(response)
response = HTTPClient('http://127.0.0.1:5000/').request('get_balance','BTC','0x123456')
print(response)