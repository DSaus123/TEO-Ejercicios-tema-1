from datetime import date

def calcula_dia_semana(fecha):
    nombres_dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    dia_semana = fecha.weekday()
    return nombres_dias_semana[dia_semana]

if __name__ == "__main__":
    dia = int(input("Escriba el día: "))
    mes = int(input("Escriba el mes: "))
    año = int(input("Escriba el año: "))
    fecha = date(año, mes, dia)
    print(f"Fecha: {fecha}")
    res = calcula_dia_semana(fecha)
    print(f"Día de la semana: {res}")
