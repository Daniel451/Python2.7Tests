'''
Created on 23.08.2014

@author: daniel
'''

import time
import random
import numpy



class RandomTest():
    
    container = dict()
    count_execs = 0


    def __init__(self):
        
        print "Starting execution...\n"
        for i in range(1, 101):
            self.container[i] = 0
        

    def doCalculate(self):
    
        self.count_execs += 1
        randomInteger = random.randint(1, 100)
        self.container[randomInteger] += 1   
        
    
    def endCalculation(self):
        
        optimalFillNumber = self.count_execs / 100
        
        print "100% ready"
        print("============================================================")
        print("Script Executions: " + self.strFormat(self.count_execs) + " | Every container from 01 to 100 should have"
        + " about " + self.strFormat(optimalFillNumber) + " fills\n")
        
        
        print("10 smallest containers:")
        underfilled_container = []
        for key, value in sorted(self.container.copy().iteritems(), key=lambda (k, v): (v, k)):
            underfilled_container.append((key, value))
            
        
        for uitem in range(0, 9):
            print("[" + str(underfilled_container[uitem][0]) + "]:" + str(underfilled_container[uitem][1])
                  + " | ( " + 
                  str((float(100) / float(optimalFillNumber) * float(underfilled_container[uitem][1])) - 100)
                  + "% deviation from " + self.strFormat(optimalFillNumber) + ")")
        
        
        print("")
        
        
        print("10 biggest containers:")
        underfilled_container = []
        for key, value in sorted(self.container.copy().iteritems(), key=lambda (k, v): (v, k)):
            underfilled_container.insert(0 , (key, value))
        
        
#         underfilled_container = underfilled_container.reverse()
        
        for uitem in range(0, 9):
            print("[" + str(underfilled_container[uitem][0]) + "]:" + str(underfilled_container[uitem][1])
                  + " | ( " + 
                  str((float(100) / float(optimalFillNumber) * float(underfilled_container[uitem][1])) - 100)
                  + "% deviation from " + self.strFormat(optimalFillNumber) + ")")
            
        
        print("")
        
        print("All containers:")
        
        
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
            
    def strFormat(self, string):
        
        scontainer = str(string)
        sready = ""
        
        i = len(scontainer) - 1
        
        while i >= 0:
            sready = scontainer[i] + sready
            if len(sready.replace(".", "")) % 3 == 0 and i > 0:
                sready = "." + sready
            i -= 1
            
        return sready            
            

Rubby = RandomTest()


loopcounter = 0
loopmax = 100000
loopgoal = 5  # Prozent der Kalkulationen, die fertig sind

while loopcounter < loopmax:

    Rubby.doCalculate()
    
    if loopcounter > loopmax / 100 * loopgoal:
        print(str(loopgoal) + "% ready")
        loopgoal += 5
        
    loopcounter += 1

Rubby.endCalculation()
        

#     time.sleep(0.01)
