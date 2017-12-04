import threading

class MyMessenger(threading.Thread):
    def run(self):
        for _ in range(200):
            print(threading.currentThread().getName())

x = MyMessenger(name='Send out messages')
y = MyMessenger(name='Receive messages')

x.start()
y.start()