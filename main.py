import openpyxl

# Crear diccionario para almacenar estudiantes y notas
estudiantes = {}

# Pedir 3 nombres y notas
for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    estudiantes[nombre] = nota

# Crear archivo Excel
libro = openpyxl.Workbook()
hoja = libro.active

# Escribir encabezados
hoja["A1"] = "Estudiante"
hoja["B1"] = "Nota"

# Escribir datos en el Excel
fila = 2
for nombre, nota in estudiantes.items():
    hoja[f"A{fila}"] = nombre
    hoja[f"B{fila}"] = nota
    fila += 1

# Guardar el archivo
libro.save("ejercicio1.xlsx")
print("¡Ejercicio guardado en ejercicio1.xlsx!")
