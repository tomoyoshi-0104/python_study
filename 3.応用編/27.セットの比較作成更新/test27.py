test_set_1 = set({'python', '-', 'izm', '.', 'com'})

print(test_set_1.isdisjoint({'python', 'izm'}))
print(test_set_1.isdisjoint({1, 2, 3}))
print('----------------------------')
print(test_set_1.issubset({'python', 'izm'}))
print(test_set_1.issubset({'www', 'python', '-', 'izm', '.', 'com'}))
print(test_set_1 <= {'python', 'izm'})
print(test_set_1 <= {'www', 'python', '-', 'izm', '.', 'com'})
print('----------------------------')
print(test_set_1.issuperset({'python', 'izm'}))
print(test_set_1.issuperset({'www', 'python', '-', 'izm', '.', 'com'}))
print(test_set_1 >= {'python', 'izm'})
print(test_set_1 >= {'www', 'python', '-', 'izm', '.', 'com'})
print()

test_set_1 = {'python', 'izm', 'com'}

print(test_set_1.union({'python', 'www'}))
print(test_set_1.intersection({'python', 'www'}))
print(test_set_1.difference({'python', 'www'}))
print(test_set_1.symmetric_difference({'python', 'www'}))
print(test_set_1 | {'python', 'www'})
print(test_set_1 & {'python', 'www'})
print(test_set_1 - {'python', 'www'})
print(test_set_1 ^ {'python', 'www'})
print()

test_set_1 = {'python', 'izm', 'com'}
test_set_1.intersection_update({'python', 'www'})
print(test_set_1)
test_set_1 = {'python', 'izm', 'com'}
test_set_1 &= {'python', 'www'}
print(test_set_1)
print()

test_set_1 = {'python', 'izm', 'com'}
test_set_1.difference_update({'python', 'www'})
print(test_set_1)
test_set_1 = {'python', 'izm', 'com'}
test_set_1 -= {'python', 'www'}
print(test_set_1)
print()

test_set_1 = {'python', 'izm', 'com'}
test_set_1.symmetric_difference_update({'python', 'www'})
print(test_set_1)
test_set_1 = {'python', 'izm', 'com'}
test_set_1 ^= {'python', 'www'}
print(test_set_1)
