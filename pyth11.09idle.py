Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.path
['', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\idlelib', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32\\lib', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages']
>>> sys.path.append(r'C:\Users\Trainee\Desktop\pythonruby')
>>> sys.path
['', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\idlelib', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32\\lib', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32', 'C:\\Users\\Trainee\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages', 'C:\\Users\\Trainee\\Desktop\\pythonruby']
>>> import pkg.pkg1.calc
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import pkg.pkg1.calc
ModuleNotFoundError: No module named 'pkg'
>>> import pkg.pkg1.calc.add
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    import pkg.pkg1.calc.add
ModuleNotFoundError: No module named 'pkg'
>>> sys.path.append(r'C:\Users\Trainee\Desktop')
>>> import pkg.pkg1.calc
>>> pkg.pkg1.calc.add(10,20)
30
>>> 
