def calcula_imc(peso, estatura):
    '''
    Recibe como parámetros el peso en kilogramos 
    y la estatura en metros y devuele el IMC
    '''
    res = peso / (estatura ** 2)
    return res

input_peso = float(input("Peso en kilogramos: "))
input_estatura = float(input("Estatura en metros: "))

print(calcula_imc(input_peso, input_estatura))


