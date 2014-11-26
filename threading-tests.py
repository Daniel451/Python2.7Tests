__author__ = 'daniel'



from threading import Thread
import time



def sleeper(i):
    print("Thread " + str(i) + " schlaeft")
    time.sleep(3)
    print("Thread " + str(i) + " ist aufgewacht")


t1 = Thread(target=sleeper, args=(1,))
t1.start()
t2 = Thread(target=sleeper, args=(2,))
t2.start()
t3 = Thread(target=sleeper, args=(3,))
t3.start()
