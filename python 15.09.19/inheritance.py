class A:
    def m1(self):
        print("method 1")
    def m2(self):
        print("method 2")

class B(A): #B class acquires properties of A #single inh
    def m1(self): #mtd overriding
         print("called from B")
    def m3(self):
        print("method 3")
    def m4(self):
        return "method 4"

class C(B): #B class acquires properties of A #multilevel inh
    def __init__(self,a,b):
        print("dfsdf")
    def m5(self):
        print("method 5")

class D:
    def m6(self):
        print("mtd 6")
class E(A,D): #multiple inh
    
    def m7(self):
        print("mtd 7")
    


a=A()
a.m1()
print(a.m2()) 
#print(a.m3()) throws error 
b=B()
print(b.m3())
print(b.m4())
print(b.m1())  
c=C(5,10)
c.m5()
c.m1()
c.m3()
e=E()
e.m1()
e.m6()
print(issubclass(B,A))
print(isinstance(b,B))
print(issubclass(C,A))
print(issubclass(B, object)) #all user def classes are subclasses of object clas by default 
