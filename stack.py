class data_structure:
    def __init__(self):
        self.b=[]
    def push(self,p):
        if p not in self.b:
            self.b.append(p)
            print("Push Element:  ",self.b)
        else:
            print("No Element is Push")
    def pop(self):
        if self.b!=[] :
            self.b.pop()
            print("Element is Poped")
        else:
            print("Stack is Empty")
    def display(self):
        print("Display: ",self.b)

z=data_structure()
while True:
    n=int(input('1.Push\n2.Pop\n3.Display\n4.Exit\nEnter: '))
    if n==1:
        p=int(input("Push: "))
        z.push(p)
    elif n==2:
        z.pop()
    elif n==3:
        z.display()
    else:
        print("Thank You")
        break
