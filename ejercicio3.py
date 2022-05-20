print("FUNCIÓN CALCULADORA")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))


if num2>num1:
    print("Ingrese un número menor que ",num1,": ")
    num2 = input("Ingrese el segundo número: ")

print("CALCULADORA DE SUMA, RESTA, MULTIPLICACIÓN, DIVISIÓN Y MOD")
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2
mod = num1 % num2

print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicación es: ",multi)
print("La división es: ",div)
print("El modulo es: ",mod)