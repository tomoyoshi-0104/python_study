item_list = ['desktop', 'laptop', 'tablet', 'smartphone']
stock_list = [12, 83, 55, 0]
for item_list, stock_list in zip(item_list, stock_list):
    print('{} / {}'.format(item_list, stock_list))
print()

item_list = ['desktop', 'laptop', 'tablet', 'smartphone']
stock_list = [12, 83, 55]
for item_list, stock_list in zip(item_list, stock_list):
    print('{} / {}'.format(item_list, stock_list))
print()

from itertools import zip_longest
item_list = ['desktop', 'laptop', 'tablet', 'smartphone']
stock_list = [12, 83, 55]
for item_list, stock_list in zip_longest(item_list, stock_list):
    print('{} / {}'.format(item_list, stock_list))
print()

item_list = ['desktop', 'laptop', 'tablet', 'smartphone']
stock_list = [12, 83, 55]
for item_list, stock_list in zip_longest(item_list, stock_list, fillvalue='no stock'):
    print('{} / {}'.format(item_list, stock_list))
