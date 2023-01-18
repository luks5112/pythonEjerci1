edad=int(input("ingrese la edad del cliente: "))

if edad<4 :
    print("el cliente ingresa gratis")
elif 4<= edad <= 18 :
    print("el cliente paga $1500 de entrada")
else: print("el cliente paga $2500 de entrada")