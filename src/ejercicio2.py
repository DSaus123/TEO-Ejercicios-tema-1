from ejercicio1 import *

def calcula_estado_nutricional(peso, estatura):
    imc = calcula_imc(peso, estatura)
    if imc < 18.5:
        return("Bajo peso")
    elif imc < 25:
        return("Normal")
    elif imc < 30:
        return("Sobrepeso")
    else:
        return("Obesidad")

if __name__ == "__main__":
    input_peso = float(input("Peso en kilogramos: ")) # Primero se ejecute el input y después el float
    input_estatura = float(input("Estatura en metros: "))
    estado = calcula_estado_nutricional(input_peso, input_estatura)
    print(f"Tu estado nutricional es: {estado}")

