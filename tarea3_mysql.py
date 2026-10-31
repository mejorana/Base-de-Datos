import pymysql

# Datos para actualizar
nuevo_correo = "alexa.santana_nueva@alumnos.udg.mx"
codigo_alumno = "22245002"

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

    # 3. Consulta UPDATE
    sql = "UPDATE alumnos SET correo = %s WHERE codigo = %s"

    # 4. Valores
    valores = (nuevo_correo, codigo_alumno)

    # 5. Ejecutar
    cursor.execute(sql, valores)

    # 6. Guardar cambios
    conexion.commit()

    # 7. Verificar filas afectadas
    print(f"Se actualizaron {cursor.rowcount} registro(s).")

except Exception as e:
    print(f"Error: {e}")

finally:
    if conexion and conexion.open:
        conexion.close()
        print("Conexión cerrada")