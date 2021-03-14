from datetime import datetime
from xmlrpc.client import ServerProxy

proxy = ServerProxy('http://localhost:8000/')

# 登録されているメソッド名を取得
print(proxy.system.listMethods())
# それぞれを取得
print(proxy.is_alive())
print(proxy.hello('World'))
nowtime = datetime.strptime(proxy.nowtime().value, '%Y%m%dT%H:%M:%S')
print(nowtime.strftime('%Y/%m/%d %H:%M:%S'))
