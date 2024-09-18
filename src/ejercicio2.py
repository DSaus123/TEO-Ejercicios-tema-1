from ejercicio1 import *

def calcula_estado_nutricional(peso, estatura):
    if calcula_imc(peso, estatura) < 18.5:
        return("Bajo peso")
    elif 18.5 <= calcula_imc(peso, estatura) < 25:
        return("Normal")
    elif 25 <= calcula_imc(peso, estatura) < 30:
        return("Sobrepeso")
    else:
        return("Obesidad")

input_peso = float(input("Peso en kilogramos: "))
input_estatura = float(input("Estatura en metros: "))

calcula_estado_nutricional(input_peso, input_estatura)

