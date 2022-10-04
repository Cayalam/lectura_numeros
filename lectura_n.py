print("/////////////////////////")
print("////Lectura///numero/////")
print("/////////////////////////")

# Input
N=int(input("Ingresa un numero: "))
pert_pares=0
pert_impares=0
while (N!=0) and N>0:
    N=int(input("Ingresa un numero: "))
    if (N%2==0):
        pert_pares+=1
    else:
       pert_impares += 1
print("cantidad de pares: " + str(pert_pares))
print("cantidad de impares: " + str(pert_impares))

   
    



