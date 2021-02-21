import os
for env in os.environ:
    print(env)

print('----------------------------------')
print(os.environ.get('windir'))
