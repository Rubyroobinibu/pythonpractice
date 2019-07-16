from datetime import datetime
class Emp:
    bonus=100 #class var
    def __init__(self,name,sal): #instance mtd
        self.name=name
        self.sal=sal
        
    def getSal(self):
        return self.sal
    
    def applyHike(self):
        self.sal=self.sal*2.00
        return int(self.sal)

    @classmethod  #decorator #class mtd
    def setBonus(cls,amt):
        cls.bonus=amt

    @staticmethod
    def isworkingDay():
        day=datetime.now().strftime('%w')
        if day == '0' or day == '1':
            return False
        else:
            return True

    '''def __str__(self): #returns name instead of memory location if typed print(e1)
        return self.name'''
    def __repr__(self): #works only if __str__ is not there. if __str__ is there, __repr__ is not executed
        return str(self.sal)
    def __add__(self, other):
        #return self.sal+other.sal
        return self.name+other.name

class Developer(Emp):
    def __init__(self,name,sal,stack):#__  __ is dunder or magical fn
        self.stack=stack
       
        super().__init__(name,sal)

    def getStack(self):
        return self.stack


        
    
if __name__ =='__main__':  #checks if other modules uses this class,if so blocks them
    print(__name__)
    dev=Developer("fdsfSD",70000,"python")
    print(dev.getStack())
    print(dev.getSal())
    print(getattr(dev, 'sal'))
    setattr(dev,'sal', 209000)
    print(getattr(dev, 'sal'))
    delattr(dev, 'sal')
    print(dev.__dict__)
    print(hasattr(dev,'name'))
#else:
 #   print("other")
