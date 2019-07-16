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

        
    
if __name__ =='__main__':  #checks if other modules uses this class,if so blocks them
    print(__name__)
    
    e1=Emp("aaa",100000)
    e2=Emp("nnn",30000)
    print(e1) 
    print(e1.getSal())
    print(e2.getSal())
    print(Emp.getSal(e1)) #using class name to access instance mtd
    print(Emp.bonus)
    Emp.setBonus(1000)
    print(e1.bonus)
    print(e2.bonus)
    print(e1.applyHike())
    print(e2.applyHike())
    print(Emp.isworkingDay())
    print(e1)
    print(e2)
    print(e1+e2) #adds the instance var because it is built in func #polymorphism #does not throw error of adding obj

else:
    print("other")



