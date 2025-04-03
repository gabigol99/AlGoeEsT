#peça ao usúario uma temperatura e use if para determinar se esta "frio"("<20"), "morno"(>20  <26) ou "quente"(>27) com base em intervalos de valores.
temperatura = float(input("insira a temperatura"))

if temperatura <=20:
    print("temperatura: frio")
elif temperatura >=20 and temperatura <=26:
    print("temperatura: morno")
elif temperatura >=27:
    print("temperatura: quente")
 




