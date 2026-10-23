gastos = [
    {"concepto": "Super", "categoria": "comida", "monto": 850},
    {"concepto": "Gasolina", "categoria": "transporte", "monto": 600},
    {"concepto": "Tacos", "categoria": "comida", "monto": 180},
    {"concepto": "Netflix", "categoria": "suscripciones", "monto": 219},
    {"concepto": "Uber", "categoria": "transporte", "monto": 145},
    {"concepto": "Farmacia", "categoria": "salud", "monto": 320},
]

def total (data):
    total = 0
    for gasto in data:
        total+= gasto["monto"]

    return total

def mas_caro (data):
    caro = data[0]
    for gasto in data:
        if  gasto["monto"] > caro["monto"]:
            caro = gasto


    return caro

def total_por_categoria(data):
    totales = {}

    for gasto in data:
        categoria = gasto["categoria"]
        if categoria not in totales:
            totales[categoria] = gasto["monto"]
        else:
            totales[categoria] += gasto["monto"]



    return totales


print ("total de gasto: ",total(gastos))
caro = mas_caro(gastos)
print(caro["concepto"],caro["monto"])
print (total_por_categoria(gastos))
