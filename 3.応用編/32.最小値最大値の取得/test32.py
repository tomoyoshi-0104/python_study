print(min([10, 20, 30, 20, 5, 3]))
print(min('Z', 'A', 'J', 'W'))
print(max([10, 20, 30, 20, 5, 3]))
print(max('Z', 'A', 'J', 'W'))
print()

def key_func(n):
    return int(n)
l = [2, 3, 4, '111']
print(min(l, key=key_func))
print(max(l, key=key_func))

def key_func(n):
    return str(n)
print(min(l, key=key_func))
print(max(l, key=key_func))

print(min(l, key=int))
print(max(l, key=int))
print(min(l, key=str))
print(max(l, key=str))
print()

def key_func(n):
    return n[2]

# code / name / score
l = [(1, 'Python', 100), (2, 'Ruby', 80), (3, 'Perl', 40)]

print(min(l, key=key_func))
print(max(l, key=key_func))
print()

def key_func(n):
    return n.score

class TestClass:
    def __init__(self, code, name, score):
        self.code = code
        self.name = name
        self.score = score

    def __str__(self):
        return '({}, {}, {})'.format(self.code, self.name, self.score)

l = [
    TestClass(1, 'Python', 100),
    TestClass(2, 'Ruby', 80),
    TestClass(3, 'Perl', 40)
]

print(min(l, key=key_func))
print(max(l, key=key_func))
