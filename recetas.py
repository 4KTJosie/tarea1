import sqlite3

# Conexión y creación de tabla en SQLite
def conectar():
    conexion = sqlite3.connect('libro_de_recetas.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            ingredientes TEXT NOT NULL,
            pasos TEXT NOT NULL
        )
    ''')
    conexion.commit()
    return conexion, cursor

# Agregar nueva receta
def agregar_receta(conexion, cursor):
    nombre = input("Nombre de la receta: ")
    ingredientes = input("Ingredientes (separados por comas): ")
    pasos = input("Pasos: ")
    cursor.execute('''
        INSERT INTO recetas (nombre, ingredientes, pasos)
        VALUES (?, ?, ?)
    ''', (nombre, ingredientes, pasos))
    conexion.commit()
    print("Receta agregada con éxito.")

# Actualizar receta existente
def actualizar_receta(conexion, cursor):
    ver_recetas(cursor)
    receta_id = input("ID de la receta a actualizar: ")
    nombre = input("Nuevo nombre de la receta (dejar en blanco para mantener actual): ")
    ingredientes = input("Nuevos ingredientes (dejar en blanco para mantener actual): ")
    pasos = input("Nuevos pasos (dejar en blanco para mantener actual): ")
    
    if nombre:
        cursor.execute('UPDATE recetas SET nombre = ? WHERE id = ?', (nombre, receta_id))
    if ingredientes:
        cursor.execute('UPDATE recetas SET ingredientes = ? WHERE id = ?', (ingredientes, receta_id))
    if pasos:
        cursor.execute('UPDATE recetas SET pasos = ? WHERE id = ?', (pasos, receta_id))
    conexion.commit()
    print("Receta actualizada con éxito.")

# Eliminar receta existente
def eliminar_receta(conexion, cursor):
    ver_recetas(cursor)
    receta_id = input("ID de la receta a eliminar: ")
    cursor.execute('DELETE FROM recetas WHERE id = ?', (receta_id,))
    conexion.commit()
    print("Receta eliminada con éxito.")

# Ver listado de recetas
def ver_recetas(cursor):
    cursor.execute('SELECT id, nombre FROM recetas')
    recetas = cursor.fetchall()
    print("\nListado de recetas:")
    for receta in recetas:
        print(f"ID: {receta[0]}, Nombre: {receta[1]}")
    print()

# Buscar ingredientes y pasos de una receta
def buscar_receta(cursor):
    nombre = input("Nombre de la receta a buscar: ")
    cursor.execute('SELECT ingredientes, pasos FROM recetas WHERE nombre = ?', (nombre,))
    receta = cursor.fetchone()
    if receta:
        print("\nIngredientes:", receta[0])
        print("Pasos:", receta[1])
    else:
        print("Receta no encontrada.")

# Menú principal
def menu():
    conexion, cursor = conectar()
    while True:
        print("\n--- Libro de Recetas ---")
        print("1. Agregar nueva receta")
        print("2. Actualizar receta existente")
        print("3. Eliminar receta existente")
        print("4. Ver listado de recetas")
        print("5. Buscar ingredientes y pasos de receta")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_receta(conexion, cursor)
        elif opcion == '2':
            actualizar_receta(conexion, cursor)
        elif opcion == '3':
            eliminar_receta(conexion, cursor)
        elif opcion == '4':
            ver_recetas(cursor)
        elif opcion == '5':
            buscar_receta(cursor)
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    
    conexion.close()

# Ejecución del programa
if __name__ == "__main__":
    menu()