class Mobile:
    def __init__(self):
#         self.__maxPrice=897
          self.maxPrice=897
        
mob=Mobile()
print(mob.maxPrice)


class Mobile:
    def __init__(self):
        self.__maxPrice=897          
    def getPrice(self):
        print(self.__maxPrice)
    def setPrice(self,price):
        self.__maxPrice=price
        
mob=Mobile()
# print(mob.maxPrice)
mob.getPrice()
mob.setPrice(688990)
mob.getPrice()
