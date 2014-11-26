'''
Created on 23.08.2014

@author: daniel
'''

import random


testing = False

for i in range (1, 11):
    
    bufferstring = ""
    for x in range (1, 11):
        randomStrInt = random.randint(0, 99)
        if randomStrInt < 10:
            randomStrInt = "0" + str(randomStrInt)
        else:
            randomStrInt = str(randomStrInt)
        bufferstring += randomStrInt + " "
    
    print(bufferstring)
