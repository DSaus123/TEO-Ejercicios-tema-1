def lee_numeros(cantidad, num):
    lista = []
    i = 0
    while cantidad != 0:
        lista.append(num[i])
        i += 1
        cantidad -= 1
    return lista

res = lee_numeros(6, [1, 32, 12, 8, 0, 23])
print(f"Lista: {res}\n")

# Mayor número de la lista
if(len(res) != 0):
    print(f"Mayor número de la lista: {max(res)}")
else:
    print("No es posible calcular el máximo.")

#Media de los números de la lista
if(len(res) != 0):
    media = sum(res) / len(res)
    print(f"Media de los números de la lista: {media}")
else:
    print("No es posible calcular la media.")

# Número de elementos pares en la lista
counter = 0
for i in res:
    if i % 2 == 0:
        counter += 1
print(f"Número de elementos pares en la lista: {counter}")

# Nueva lista con aquellos elementos de la lista leída que sean mayores a 10
nueva_lista = []
for i in res:
    if i > 10:
        nueva_lista.append(i)
print(f"Nueva lista con aquellos elementos de la lista leída que sean mayores a 10: {nueva_lista}")
