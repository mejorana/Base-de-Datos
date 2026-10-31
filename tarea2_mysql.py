import pymysql

conexion = None

try:
    # 1. Conexión
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="Marjolaine77.",
        database="alumnos_universidad"
    )

    # 2. Cursor
    cursor = conexion.cursor()

    # 3. Consulta SQL
    consulta = """
    INSERT INTO alumnos (codigo, alumno, correo, carrera)
    VALUES (%s, %s, %s, %s)
    """

    # 4. Datos del nuevo alumno (tupla)
    datos = (
        "22245006",
        "Jorge Ivan Gómez",
        "ivanGomez@alumnos.udg.mx",
        "Licenciatura en Ciencia de Datos"
    )

    # 5. Ejecutar
    cursor.execute(consulta, datos)

    # 6. Guardar cambios
    conexion.commit()

    print("✅ Alumno guardado correctamente")

except Exception as e:
    print(f" Ocurrió un error: {e}")

finally:
    if conexion and conexion.open:
        conexion.close()
        print("🔒 Conexión cerrada")