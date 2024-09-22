from datetime import date

def calcula_dia_semana(fecha):
    return date.weekday(fecha)

dia = int(input("Escriba el día: "))
mes = int(input("Escriba el mes: "))
año = int(input("Escriba el año: "))

fecha = date(año, mes, dia)
print(f"Fecha: {fecha}")

res = calcula_dia_semana(fecha)

if res == 0:
    sem = "Lunes"
elif res == 1:
    sem = "Martes"
elif res == 2:
    sem = "Miércoles"
elif res == 3:
    sem = "Jueves"
elif res == 4:
    sem = " Viernes"
elif res == 5:
    sem = "Sábado"
else:
    sem = "Domingo"

print(f"Día de la semana: {sem}")
