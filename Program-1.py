#I have used Python language to solve this calculator problem
class cal():
    def __init__(self,f,s):
        self.f=f
        self.s=s
    def add(self):
        return self.f+self.s
    def mul(self):
        return self.f*self.s
    def div(self):
        return self.f/self.s
    def sub(self):
        return self.f-self.s
print("")
f=int(input("Enter first number: "))
s=int(input("Enter second number: "))

obj=cal(f,s)

print("ADDITION")
print("SUBTRACTION")
print("MULTIPLICATION")
print("DIVISION")
choice = str(input("Enter your type of operation:"))
if choice == 'ADDITION':
  print(obj.add())
elif choice == "SUBTRACTION":
  print(obj.sub())
elif choice == "MULTIPLICATION":
  print(obj.mul())
elif choice == "DIVISION":
  print(obj.div())
else:
  print("Enter the type of operation in correct format(input is case sensitive). Please try agian")