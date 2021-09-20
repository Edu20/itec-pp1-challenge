from challenge import numero_to_letras

pregunta = "si"

while pregunta == "si":
    numeroIngresado = int(input("Ingrese el número que desea convertir: "))
    numero_to_letras(numeroIngresado)
    pregunta = input("Desea ingresar otro número: si/no: ")