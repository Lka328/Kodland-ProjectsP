import random
Contra="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Contraa="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Longitud=int(input("Ingresa la longitud de la contrasena: "))
gener=""
genero=""
for i in range(Longitud):
    gener+=random.choice(Contra)
print(f"Esta es tu contrasena: {gener}")
print(f"Estas a gusto con esa contrasena?")
gusto=input("Responde con SI o NO:")
if gusto=="SI":
    print(f"Gracias por preferir usar nuestra contrasena")
else:
    print(f"Puede crear otra contrasena si lo desea")
    gustoo=input("Responde con SI o NO:")
    if gustoo=="SI":
            Longituud=int(input("Ingresa la longitud de la contrasena: "))
            for i in range(Longituud):
                genero+=random.choice(Contraa)
            print(f"Esta es tu segunda contrasena: {genero}")
    else:
        print(f"Bueno, esperamos que encuentre una contrasena mas factible...")
