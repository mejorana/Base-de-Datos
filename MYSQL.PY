import pymysql

# 1. Conexión a MySQL
conexion = pymysql.connect(
    host="localhost",
    user="root",
    password="Marjolaine77.",
    database="alumnos_universidad"
)

# 2. Cursor
cursor = conexion.cursor()

# 3. Consulta
sql = "SELECT codigo, alumno, correo, carrera FROM alumnos"
cursor.execute(sql)

# 4. Obtener datos
resultados = cursor.fetchall()

# 5. Mostrar datos
print("\n--- LISTA DE ALUMNOS ---\n")

for fila in resultados:
    print(f"Código: {fila[0]} | Alumno: {fila[1]} | Correo: {fila[2]} | Carrera: {fila[3]}")

# 6. Cerrar conexión
conexion.close()