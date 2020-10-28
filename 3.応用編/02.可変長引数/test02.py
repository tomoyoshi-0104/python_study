def test_func(*args):
    print(args)

test_func(1, 2, 3, 4, 5)
print()

def test_func(code, name, *countries):
    print(code, name)
    print(countries)
test_func(100, 'python-izm', 'JP', 'US')
print()

def test_func(**kwargs):
    print(kwargs)
test_func(code=100, name='python-izm')
print()

def test_func(code, name, kana, *args, **kwargs):
    print(code, name, kana)
    print(args)
    print(kwargs)
test_func(
    100, 'python-izm', u'パイソンイズム',
    'JP', 'US',
    email='xxxx', city='Tokyo'
)
