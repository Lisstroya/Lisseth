# Creación de diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Maria Cedeño Morales",
    "edad": 25,
    "ciudad": "Guayaquil",
    "profesion": "Ingeniera en sistemas"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Loja"

# Agregar una nueva clave-valor para la profesión (Se cambia por una diferente)
informacion_personal["profesion"] = "Analista de datos"

# Verificar si la clave "telefono" existe, si no, la agregamos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987693225"

# Eliminamos la clave "edad" del diccionario
informacion_personal.pop ("edad")

# Imprimimos el diccionario final
print("Diccionario final después de las operaciones:")
print(informacion_personal)