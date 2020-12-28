import os
filepath = 'C:/Users/tomoy/OneDrive/ドキュメント/GitHub/python_study/3.応用編/python'
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
tmpdir = 'C:/Users/tomoy/OneDrive/ドキュメント/GitHub/python_study/3.応用編/python/tmp'
os.mkdir(tmpdir)
os.makedirs('C:/Users/tomoy/OneDrive/ドキュメント/GitHub/python_study/3.応用編/python/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpdir)
os.rmdir('C:/Users/tomoy/OneDrive/ドキュメント/GitHub/python_study/3.応用編/python/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpdir)
# os.removedirs(tmpdir)
shutil.rmtree(tmpdir)

shutil.copy('C:/Users/tomoy/OneDrive/ドキュメント/GitHub/python_study/3.応用編/python/src.txt', 'C:/Users/tomoy/OneDrive/ドキュメント/GitHub/python_study/3.応用編/python/dest.txt')
shutil.copytree('C:/Users/tomoy/OneDrive/ドキュメント/GitHub/python_study/3.応用編/python', 'C:/Users/tomoy/OneDrive/ドキュメント/GitHub/python_study/3.応用編/python_backup')
