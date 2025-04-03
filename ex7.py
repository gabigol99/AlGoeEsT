#escreva um programa que receba dois números e uma operação (adição, subtração, multiplicação ou divisão) 
#if para realizar a operação correta com a base na esclha do usuário.
print("digigite dois numeros")
num1 = int(input("insira o primeiro numero"))
num2 = int(input("insira o segundo numero"))
op = input("insira a operacao")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("operacao invalida")