# 疑似コード
# ループ開始前に 1 から 10 まですべてを確保
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#    print(i)

# 呼び出されるごとに値を生成
#for i in <ジェネレータ>:
#    print(i)

def func_sample():
    print('おはよう')
    print('こんにちは')
    print('こんばんは')
func_sample()
print()

def func_sample():
    yield('おはよう')
    yield('こんにちは')
    yield('こんばんは')
func_sample()
print()

for i in func_sample():
    print(i)
print()

f = func_sample()
print(next(f))
print(next(f))
print(next(f))
# print(f.next())
print()

gen_sample = (i for i in 'おはよう こんにちは こんばんは'.split())
print(gen_sample)
for i in gen_sample:
    print(i)
