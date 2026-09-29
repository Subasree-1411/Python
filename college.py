class college:
    def admin(self,a):
            print("Admission Going:  ",a)
    def fees(self,f):
        if f <= 0 :
            print("Fees amount is zero")
        else:
            print("Successfully paid the fees")
    def confirm(self):
        print("Seat is Confirmed")

z=college()
while True:
    n=int(input('1.Admission\n2.Fees\n3.Confirmation\n4.Exit\nEnter: '))
    if n==1:
        a=int(input("Application Fee: "))
        z.admin(a)
    elif n==2:
        f=int(input("Fees: "))
        z.fees(f)
    elif n==3:
        z.confirm()
    else:
        print("Thank You")
        break
