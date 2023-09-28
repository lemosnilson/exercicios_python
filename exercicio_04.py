num1= input("insira o primeiro numero inteiro: ")
num2 = input("insira o segundo numero inteiro: ")
num3 = input("insira o primeiro número decimal: ")

int1 = float(num1)
int2 = float(num2)
float1 = float(num3)

a = round((2*int1)*(int2/2),2)
b = round((3*int1)+float1,2)
c = round(float1**3,2)

print(a, b, c)
