a = int(input("enter a : "))
b = int(input("enter b : "))
ch = input("+ or -: ")
while ch != '-' and ch != '+':
    print('re-enter')
    ch = input("+ or -: ")
if ch == '-':
    print(f"{a} - {b} = {a-b}")
elif ch == '+':
    print(f"{a} + {b} = {a+b}")
