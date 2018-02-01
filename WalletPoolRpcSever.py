################################################################################
#  Function: TestRpc Server                                                    #
#                                                                              #
#                                                                              #
#                                                   WangYi 2018/1/31           #
# pip install  jsonrpcserver                                                   #
################################################################################
from jsonrpcserver import methods

methods.debug = True

@methods.add
def get_balance(name,address):
 if name == "BTC" :
      balance = 100
 elif name == "ETH" :
      balance = 200
 elif name == "SAC" :
      balance = 300
 else :
      balance = 0
 return balance

@methods.add
def get_address(name):
 if name == "BTC" :
      address = "BTC-0x1234567890abcdef123456"
 elif name == "ETH" :
      address = 'ETH-0x1234567890abcdef123456'
 elif name == "SAC" :
      address = 'SAC-0x1234567890abcdef123456'
 else :
      address = ''
 return address


if __name__ == '__main__':
    methods.serve_forever()
    