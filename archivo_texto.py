# Escritura en el archivo de texto
with open("my_notes.txt", "w") as file:
    file.write("Hola, soy Lisseth Troya.\n")
    file.write("Estoy aprendiendo a trabajar con archivos en Python.\n")
    file.write("Este conocimiento es muy util.\n")

print("Escritura completada. Ahora se mostrará el contenido del archivo:\n")

# Lectura del archivo línea por línea
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() elimina saltos de línea innecesarios

print("\nLectura finalizada. Archivo cerrado correctamente.")

