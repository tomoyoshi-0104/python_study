# これを www.python-izm.com としたい
elem = ['www', 'python-izm', 'com']
host_name = ''
for val in elem:
    # host_name += val + '.'
    if val != 'com':
        host_name += val + '.'
    else:
        host_name += val
print(host_name)
print()

print('.'.join(elem))
print()

print('\n'.join(elem))
print(','.join(elem))
print(' '.join('1234567890'))
print('+'.join(('1', '2', '3')))
