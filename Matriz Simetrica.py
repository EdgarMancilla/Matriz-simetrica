arreglo1=[0,0,0,0,0,0]
arreglo2=[0,0,0,0,0,0]
arreglo3=[0,0,0,0,0,0]
arreglo4=[0,0,0,0,0,0]
arreglo5=[0,0,0,0,0,0]
arreglo6=[0,0,0,0,0,0]
for i in range (1,7):
    arreglo1[i - 1] = float(input("Este es tu primer arreglo, dame el número {}: ".format(i)))
for i in range (1,7):
    arreglo2[i - 1] = float(input("Este es tu segundo arreglo, dame el número {}: ".format(i)))
for i in range (1,7):
    arreglo3[i - 1] = float(input("Este es tu tercer arreglo, dame el número {}: ".format(i)))
for i in range (1,7):
    arreglo4[i - 1] = float(input("Este es tu cuarto arreglo, dame el número {}: ".format(i)))
for i in range (1,7):
    arreglo5[i - 1] = float(input("Este es tu quinto arreglo, dame el número {}: ".format(i)))
for i in range (1,7):
    arreglo6[i - 1] = float(input("Este es tu sexto arreglo, dame el número {}: ".format(i)))
print(arreglo1)
print(arreglo2)
print(arreglo3)
print(arreglo4)
print(arreglo5)
print(arreglo6)
if (arreglo1[0])==(arreglo1[0]) and (arreglo1[1])==(arreglo2[0]) and (arreglo1[2])==(arreglo3[0]) and (arreglo1[3])==(arreglo4[0]) and (arreglo1[4])==(arreglo5[0]) and (arreglo1[5])==(arreglo6[0]):
    print("Tu matriz es simetrica, ¡Felicidades!")
else:
    print("Tu matriz no es simetrica, lo siento :(")