num1 = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))
num3 = int(input("Insira um número: "))

if num1 > num2 and num1 > num3:    
    print(f"{num1} é maior")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é maior")
else:
    print(f"{num3} é maior")        

if num1 < num2 and num1 < num3:
    print(f"{num1} é menor")
elif num2 < num1 and num2 < num3:
    print(f"{num2} é menor")
else:
    print(f"{num3} é menor")
