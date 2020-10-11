print('python')
print('-')
print('izm')
print('com')
print()

#改行しない
print('python', end=' ')
print('-', end=' ')
print('izm', end=' ')
print('com')
print()

#出力先の変更
f_obj = open('./21.print/test.txt', 'w')
print('python-izm.com', file=f_obj)
print()

#フォーマット出力
print('Pythonの学習サイト：%s' % 'python-izm.com')
print('Pythonの学習サイト：%s-%s.%s' % ('python', 'izm', 'com'))
test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 %d 日目！ %s' % (test_int, test_str))
print()

print('Pythonの学習サイト：{}'.format('python-izm.com'))
print('Pythonの学習サイト：{0}-{1}.{2}'.format('python', 'izm', 'com'))
test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 {1} 日目！ {0}'.format(test_str, test_int))
