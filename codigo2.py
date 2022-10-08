nueve=0
siete=0

for i in range (1000,5001):
    if(i%9==0):
        nueve=nueve+1
    if(i%7==0):
        siete=siete+1
    
print("La cantidad de numeros multiplos de 7 son : "+str(siete))
print("La cantidad de numeros multiplos de 9  es: "+str(nueve))
