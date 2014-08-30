'''
Created on 23.05.2014

@author: daniel
'''

if __name__ == '__main__':
   pass

# Kommentar...
print("Hallo Welt")
print("Test2")

a = 0
b = 2

print("a + b = " + str(a + b))

if a > b:
   print("a > b")
elif a < b:
   print ("a < b")
else :
   print ("a = b")
    
    
def someFunction():
   print("eine Funktion")
    
someFunction()

for i in range(1, 3):
   print(i)


def someFunction2(a, b):
   print(a + b)

someFunction2(5, 10)


w = 0
while w < 10:
   print(w)
   w += 1
   
# Stringtests
str1 = "EinString"

print(type(str1))

print("str1[:]: " + str1[:])

print("str1[1:5]: " + str1[1:5])

print("str1[0:-1]: " + str1[0:-1])

# Python3?! -> print("str[:-1]: " + str[:-1])


# Listentest
sampleList = ["Eine", "Test", "Liste"];

for a in sampleList:
   print(a)



# Classes in Python
class testClass1(object):
   
   def __init__(self):
      self.var1 = 0
   
   def add(self, amount):
      self.var1 += amount
   
   def ret(self):
      return self.var1

test1 = testClass1()
test1.add(50)
print(test1.ret())
   
