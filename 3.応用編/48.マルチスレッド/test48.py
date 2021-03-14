import threading
import time
import datetime

class TestThread(threading.Thread):

    def run(self):
        print('  === start sub thread ===')
        for i in range(5):
            time.sleep(5)
            print('  sub thread : ' + str(datetime.datetime.today()))
        print('  === end sub thread ===')

th = TestThread()
th.daemon = True
# th.daemon = False
th.start()
time.sleep(1)

print('=== start main thread ===')
for i in range(5):
    time.sleep(10)
    print('main thread : ' + str(datetime.datetime.today()))
print('=== end main thread ===')
