def calcula_imc(peso, estatura):
    '''
    Recibe como parámetros el peso en kilogramos 
    y la estatura en metros y devuele el IMC
    '''
    res = peso / (estatura ** 2)
    return res

if __name__ == "__main__":
    input_peso = float(input("Peso en kilogramos: "))
    input_estatura = float(input("Estatura en metros: "))
    imc = calcula_imc(input_peso, input_estatura)
    print(f"Tu IMC es: {imc}")
    


