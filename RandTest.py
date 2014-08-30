'''
Created on 23.08.2014

@author: daniel
'''

import time
import random



class RandomTest():
    
    container = dict()
    count_execs = 0


    def __init__(self):
        for i in range(1, 101):
            self.container[i] = 0

    def doCalculate(self):
    
        self.count_execs += 1
        self.container[random.randint(1, 100)] += 1
    
        print("============================================================")
        print("Script Executions: " + str(self.count_execs))
        
        a = 1
        b = 11
        for x in range (1, 11):
            
            pufferstring = ""
            for i in range (a, b):
                if i < 10:
                    key = "0" + str(i)
                else:
                    key = str(i)
                pufferstring += "[" + key + "]:" + str(self.container[i]) + " | "
            print(pufferstring)
            a += 10
            b += 10


Rubby = RandomTest()

loopcounter = 0
while loopcounter < 1000000:
    Rubby.doCalculate()
#     time.sleep(0.01)
