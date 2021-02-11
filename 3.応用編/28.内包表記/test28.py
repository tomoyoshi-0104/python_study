comp_list = [i for i in range(10)]
print(comp_list)
# 上の処理と下の処理が同じ
comp_list = []
for i in range(10):
    comp_list.append(i)
print(comp_list)

comp_list = [str(i * i) for i in range(10)]
print(comp_list)
print()

comp_dict = {str(i): i * i for i in range(10)}
print(comp_dict)
# 上の処理と下の処理が同じ
comp_dict = {}
for i in range(10):
    comp_dict[str(i)] = i * i
print(comp_dict)
print()

comp_set = {str(i * i) for i in range(10)}
print(comp_set)
# 上の処理と下の処理が同じ
comp_set = set()
for i in range(10):
    comp_set.add(str(i * i))
print(comp_set)
print()

comp_list = [i * ii for i in range(1,10) for ii in range(1,10)]
print(comp_list)
# 上の処理と下の処理が同じ
comp_list = []
for i in range(1,10):
    for ii in range(1,10):
        comp_list.append(i * ii)
print(comp_list)
print()

comp_list = [i for i in range(10) if i % 2 == 1]
print(comp_list)
# 上の処理と下の処理が同じ
comp_list = []
for i in range(10):
    if i % 2 == 1:
        comp_list.append(i)
print(comp_list)
print()

gen = (i for i in range(10))
print(gen)
