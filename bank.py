class bank:
    def __init__(self):
        self.b=1000
    def deposits(self,s):
        if s>=0:
            self.b+=s
            print("Deposits: ",self.b)
        else:
            print("No cash will Deposit")
    def withdrawals(self,k):
        if k>self.b:
            print("No Withdrawals")
        else:
            self.b-=k
            print("Withdrawals: ",self.b)
    def check_balance(self):
        print("CheckBalance: ",self.b)

x=bank()
while True:
    n=int(input('1.Deposit\n2.Withdrawals\n3.CheckBalance\n4.Exit\nEnter: '))
    if n==1:
        s=int(input("Deposit: "))
        x.deposits(s)
    elif n==2:
        k=int(input("WithDrawals: "))
        x.withdrawals(k)
    elif n==3:
        x.check_balance()
    else:
        print("Thank You")
        break
