from multiprocessing import Process
from time import sleep



class Blubb(object):

    def __init__(self):
        self.text = "bla"
        p = Process(target=self.worker)
        p.start()
        sleep(3)
        self.text = "bla2"
        sleep(10)
        print("reading self.text", self.text)
    
    def worker(self):
        for i in xrange(20):
            if i == 10:
                self.text = "worker_bla!"
            print("[it:{:0>2}] msg: {}".format(i, self.text))
            sleep(1)

b = Blubb()
