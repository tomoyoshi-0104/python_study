import os
filepath = 'C:/python'
if os.path.exists(filepath):
    print('指定のファイル、またはディレクトリが存在しています。')
    if os.path.isfile(filepath):
        print('指定のパスはファイルです。')
    if os.path.isdir(filepath):
        print('指定のパスはディレクトリです。')
else:
    print('指定のファイル、またはディレクトリが存在していません。')

import shutil
def show_dir(path):
    print('====================================')
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))
tmpdir = 'C:/python/tmp'
os.mkdir(tmpdir)
os.makedirs('C:/python/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpdir)
os.rmdir('C:/python/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpdir)
# os.removedirs(tmpdir)
shutil.rmtree(tmpdir)

shutil.copy('C:/python/src.txt', 'C:/python/dest.txt')
shutil.copytree('C:/python', 'C:/python_backup')
