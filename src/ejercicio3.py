from ejercicio1 import *
from ejercicio2 import *

personas = [
    (60.0, 1.6),
    (75.4, 1.75),
    (87.9, 1.69),
    (45.1, 1.65)
]

if __name__ == "__main__":
    for p in personas:
        print(f"El IMC de la persona {personas.index(p) + 1} es {calcula_imc(p[0], p[1])} y su estado nutricional es {calcula_estado_nutricional(p[0], p[1])}.")