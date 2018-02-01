# --*-- coding:utf8 --*--

from jsonrpcclient.http_client import HTTPClient


response = HTTPClient('http://127.0.0.1:5000/').request('User.open', "123")
print(response)

response = HTTPClient('http://127.0.0.1:5000/').request('Transfer.pullSAC', "123")
print(response)

response = HTTPClient('http://127.0.0.1:5000/').request('Transfer.transferSAC', "123")
print(response)

response = HTTPClient('http://127.0.0.1:5000/').request('Query.getSACBalance', "123")
print(response)