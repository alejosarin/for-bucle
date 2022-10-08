

print("Ejercicio1")
for i in [1,2,3,4,5]:
    print(i)

print("\nEjercicio 2 ")
for i in (1,2,3,4,5):
    print(i)
    
print("\nEjercicio 3 ")
lista=[1,2,3,4,5]
for i in lista:
    print(i)

print("\nEjercicio 4 ")
for i in range(1,6):
    print(i)

print("\nEjercicio 5 ")
texto="Uis no es uno, somos todos"
for i in texto:
    print(i)

print("Suma de los 10 primeros numeros")
n=int(input("Digite el valor de n : "))
suma=0
for i in range(1,(n+1)):
    suma=suma+i
print(suma)
print("ejercico8")
frase=input("Digite una frace : ")
base = "aeiouAEIOU"
num_vocales= 0
for i in frase:
    if i in base:
        num_vocales=num_vocales+1
print("El numero de vocales es "+str(num_vocales))