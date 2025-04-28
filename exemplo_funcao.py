# #tabuado do 7
# print("tabuada do 7:")
# for i in range(1, 11):
#     print("7 x", 1, "=", 7 * 1)

# #tabuada do 8
# print("tabuada do 8")
# for i in range(1, 11):
#     print("8 x" 1, "=", 8 * 1)

# #tabuada do 9
# print("tabuada do 9:")
# for i in range(1, 11):
#     print("9 x", 1, "=", 9 * 1)


#codigo em python para exibir as tabuadas de 7, 8 e 9
# def tabuada(numero):
#     print(f"Tabuada do {numero}:")
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * 1}")

# #exibindo as tabuadas
# tabuada(7)
# tabuada(8)
# tabuada(9)

#tabuada escalavel em python
# def tabuada(numero):
#     print(f"Tabuada do {numero}:")
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * 1}")
#     print() #espaço extra para as tabuadas

# #gerar tabuadas de 1 a 100
# for i in range(1, 101):
#     tabuada(i)

#tabuada personalizada em python
def tabuada_personalizada(base, inicio, fim):
    print(f"tabuada do {base} de {inicio} a {fim}:")
    for j in range(inicio, fim + 1):
        print(f"(base) x (j) = (base * j)")

#uso
tabuada_personalizada(7, 1, 10)
tabuada_personalizada(5, 5, 15)