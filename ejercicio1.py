print("EJERCICIO 1 - INGRESO DE DATOS")

nombre = input("Escriba su nombre completo: ")
apellido = input("Escriba sus dos apellidos: ")
edad = input("¿Cuántos años tiene?: ")
if edad < 18 and edad > 65:
    edad = (input("Ingrese nuevamente su edad: ")

dni = input("Ingrese su número de DNI: ")
sexo = input("Masculino (M)   -     Femenino (F): ")
if sexo == "M":
    print("El usuario es varón.")
    print("Bienvenido ",nombre," ",apellido)

elif sexo == "F":
    print("El usuario es mujer.")
    print("Bienvenida ",nombre," ",apellido)





