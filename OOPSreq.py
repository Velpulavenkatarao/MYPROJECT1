class Account:
    def __init__(self,balance):
        if balance<0:
            self.balance=0.0
            print('initial balance was invalid')
        else:
            self.balance=balance
    def Credit(self,camt):
        if camt<=0:
            print('camt should not be negaative')
            return False
        else:
            self.balance=self.balance+camt
            return True
    def debit(self,damt):
        if damt>self.balance:
            print('Debit amount exceeded account balance')
            return False
        else:
            self.balance=self.balance-damt
            return True
    def getBalance(self):
        return self.balance
class SavingsAccount(Account):
    def __init__(self,balance,roi):
        super().__init__(balance)
        self.roi=roi
    def CalculateInterest(self):
        interest=(self.balance*1*self.roi)/100
        return interest
class CheckingAccount(Account):
    def __init__(self,balance,tf):
        super().__init__(balance)
        self.tf=tf
    def Credit(self,camt):
        status=super().Credit(camt)
        if status:
            self.balance=self.balance-self.tf
    def debit(self,damt):
        status=super().debit(damt)
        if status:
            self.balance=self.balance-self.tf
class CurrentAccount(Account):
    def __init__(self,balance,od):
        super().__init__(balance)
        self.od=od
    def debit(self,damt):
        if self.balance>damt:
            self.balance=self.balance-damt
        else:
            tw=self.balance+self.od
            if tw>=damt:
                self.balance=self.balance-damt
            else:
                print('overdraft limit is exceeded')
ac1=Account(10000)
ac1.Credit(5000)
ac1.debit(7000)
print(ac1.getBalance())
ac2=Account(-10000)
ac2.Credit(5000)
ac2.debit(13000)
print(ac2.getBalance())
sa1=SavingsAccount(100000,12)
sa1.Credit(70000)
sa1.debit(20000)
print(sa1.getBalance())
print(sa1.CalculateInterest())
ca1=CheckingAccount(100000,25)
ca1.Credit(70000)
ca1.debit(20000)
print(ca1.getBalance())
cu1=CurrentAccount(100000,25000)
cu1.Credit(75000)
print(cu1.getBalance())
cu1.debit(210000)
print(cu1.getBalance())

