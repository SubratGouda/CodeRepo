a = int(input("enter ur first number: "))
b = int(input("enter ur second number: "))
o = input("Give your operator like[+,-,*,/,%]: ")

if o == '+':
    print("sum of 2 numbers: ",a + b)
elif o == '-':
    print("subtract of 2 numbers: ",a - b)
elif o == '*':
    print("multiply of 2 numbers: ",a * b)
elif o == '/':
    print("divison of 2 numbers: ",a / b)            
elif o == '%':
    print("Remainder of 2 numbers: ", a % b)    
# else:
#     print("You entered invalid operator")    
