"""
mi_diccionario = {
    "Nombre": "Juan",
    "Edad": 25,
    "Ciudad": "Ciudad Ejemplo"
}

# Imprimir encabezado
print(f"{'Clave':<15} {'Valor':<15}")
print("-" * 30)

# Imprimir filas
for clave, valor in mi_diccionario.items():
    print(f"{clave:<15} {valor:<15}")
"""


a={1:"a",
   2:"b",
   3:"c"}
for b in a.items():
    print(b)