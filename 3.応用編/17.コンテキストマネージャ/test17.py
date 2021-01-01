class ContextManagerText:
    def __enter__(self):
        print('__enter__')
        return 'as obj'
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')
        print(exc_type)
        print(exc_value)
        print(traceback)
        return True

# with ContextManagerText():
with ContextManagerText() as as_obj:
    # print('with')
    # val = int('abc')
    print(as_obj)
print()

from contextlib import contextmanager
@contextmanager
def context_manager_test():
    print('enter')
    yield 'as obj'
    print('exit')
# with context_manager_test():
with context_manager_test() as as_obj:
    # print('with')
    print(as_obj)
