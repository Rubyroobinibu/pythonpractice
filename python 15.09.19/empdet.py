class Account:

    def __init__(self,name,accno,currbal):
        self.name=name
        self.accno=accno
        self.currbal=currbal
    

    def withdraw(self,amt):
        self.amt=amt
       # self.currbal=currbal
        if self.currbal>=5000:
            if amt%50==0 and amt%100==0:
                self.currbal-=amt
                return self.currbal
    
        

    def deposit(self,amt):
       # self.currbal=currbal
        self.amt=amt
        if self.currbal>=5000:   
            if self.amt%100==0:
                self.currbal=self.currbal+self.amt
                return  self.currbal
            else:
                return "enter amt in multiples of 100"
         

    def balance(self):
        return self.currbal

acc1=Account("aaa",39298598592,10000)
print(acc1.deposit(1000))
print(acc1.withdraw(500))
print(acc1.balance())


