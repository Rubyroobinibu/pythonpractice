from oops import Emp

e3=Emp("ff",3000)
print(e3.isworkingDay())
print(e3)
Emp.setBonus(4000)
print(e3.bonus) #this change would not affect the original class var. it just imports it
