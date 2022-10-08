pares=0
impares=0

for i in range (1,101):
    n=int(input("\n\nDigite los numeros: "))

    if(n%2==0):
        pares=pares+1
    else:
        impares=impares+1
    
print("La cantidad de numeros pares es: "+str(pares))
print("La cantidad de numeros impares es: "+str(impares))

