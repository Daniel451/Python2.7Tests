



class DA(object):

    def __init__(self, number=1, increment=1):
        self.number = number 
        self.increment = increment

    def calc(self):
        self.number += self.increment 
        return self.number

