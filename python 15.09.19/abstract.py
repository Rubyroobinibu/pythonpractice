from abc import ABC, abstractmethod #ABC is predef abstract class
import math

class Shape(ABC): #abstract class - cannot be implemented but can be inherited
    @abstractmethod
    def getArea():
        pass

class Circle(Shape): 
    def getArea(self): #definition of abstract mtd
        return math.pi*3*3

shape=Shape()  #cant create obj for abstract class 

circle=Circle()
print(circle.getArea())
