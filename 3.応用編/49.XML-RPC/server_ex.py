from datetime import datetime
from xmlrpc.client import DateTime
from xmlrpc.server import SimpleXMLRPCServer

# 単純な文字列を返す
def is_alive():
    return 'alive!'

# 引数を利用する
def hello(message):
    return 'Hello {}.'.format(message)

# 現在時刻を返す
def nowtime():
    return DateTime(datetime.now())

server = SimpleXMLRPCServer(('localhost', 8000))
print('Start Server')

# 関数を登録
server.register_function(is_alive, 'is_alive')
server.register_function(hello, 'hello')
server.register_function(nowtime, 'nowtime')

# system.listMethods で参照できるように登録
server.register_introspection_functions()

# XML-RPCサーバーの起動
server.serve_forever()
