import configparser

inifile = configparser.ConfigParser()
inifile.read('C:/Users/tomoy/OneDrive/ドキュメント/GitHub/python_study/3.応用編/19.設定ファイル/config.ini', 'UTF-8')
# inifile.read('./config.ini', 'UTF-8')

print(inifile.get('settings', 'host'))
print(inifile.get('settings', 'port'))

print(inifile.get('system', 'os'))
print(inifile.get('system', 'version'))
print(inifile.get('system', 'path'))

print(inifile.get('user', 'name'))
print(inifile.get('user', 'password'))
print(inifile.get('user', 'mail'))
