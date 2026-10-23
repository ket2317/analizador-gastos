totales = {}
print(totales)            # {}

totales["comida"] = 850   # no existe → la crea
print(totales)            # {'comida': 850}

totales["salud"] = 320    # no existe → la crea
print(totales)            # {'comida': 850, 'salud': 320}

totales["comida"] = 999   # ya existe → la reemplaza
print(totales)            # {'comida': 999, 'salud': 320}

totales["comida"] += 1    # ya existe → le suma
print(totales)            # {'comida': 1000, 'salud': 320}