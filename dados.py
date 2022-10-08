import random
contador1=""
contador2=""
contador3=""
contador4=""
contador5=""
contador6=""
n=int(input("Digite el numero de dados que quiere lanzar: "))

for i in range(1,n+1):
    b= random.randint(1, 6)
    print("resultados")
    if b==1:
        contador1=(contador1+"*")
    if b==2:
        contador2=(contador2+"*")
    if b==3:
        contador3=(contador3+"*")
    if b==4:
        contador4=(contador4+"*")
    if b==5:
        contador5=(contador5+"*")
    if b==6:
        contador6=(contador6+"*")
print("EL numero de veces que cayo 1 : "+str(contador1))
print("EL numero de veces que cayo 2 : "+str(contador2))
print("EL numero de veces que cayo 3 : "+str(contador3))
print("EL numero de veces que cayo 4 : "+str(contador4))
print("EL numero de veces que cayo 5 : "+str(contador5))
print("EL numero de veces que cayo 6 : "+str(contador6))