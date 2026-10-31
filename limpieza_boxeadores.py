import pandas as pd

# 1. Leer el archivo
df = pd.read_excel("boxeadores_pro_dirty.xlsx")

# 2. Nombres: mayúsculas/minúsculas uniformes y nombre faltante
df["nombre"] = df["nombre"].str.title()
df["nombre"] = df["nombre"].fillna("Desconocido")

# 3. Categoría de peso: uniforme y "UNKNOWN" como dato faltante
df["categoria_peso"] = df["categoria_peso"].str.title()
df["categoria_peso"] = df["categoria_peso"].replace("Unknown", None)

# 4. País: nombres completos y consistentes
df["pais_origen"] = df["pais_origen"].replace({
    "Mex": "México",
    "JPN": "Japón",
    "RUS": "Rusia",
    "UK": "Reino Unido",
    "USA": "Estados Unidos"
})

# 5. Guardia: todo en minúsculas
df["guardia"] = df["guardia"].str.lower()

# 6. Valores imposibles -> dato faltante (NaN)
df.loc[df["victorias"] < 0, "victorias"] = None
df.loc[df["peso_kg"] < 0, "peso_kg"] = None
df.loc[df["peso_kg"] > 200, "peso_kg"] = None

# 7. Estatura: convertir a número (lo que no sea número queda NaN)
df["estatura_cm"] = pd.to_numeric(df["estatura_cm"], errors="coerce")

# 8. Fecha de debut: convertir a fecha (lo que no se pueda queda NaT)
df["fecha_debut"] = pd.to_datetime(df["fecha_debut"], format="mixed", errors="coerce")

# 9. Ganancias: quitar $ y comas, convertir a número
df["ganancias_usd"] = df["ganancias_usd"].str.replace("$", "", regex=False)
df["ganancias_usd"] = df["ganancias_usd"].str.replace(",", "", regex=False)
df["ganancias_usd"] = pd.to_numeric(df["ganancias_usd"])
df.loc[df["ganancias_usd"] < 0, "ganancias_usd"] = None

# 10. Eliminar duplicados (mismo boxeador repetido con otro id)
columnas = ["nombre", "categoria_peso", "pais_origen", "victorias",
            "derrotas", "empates", "peso_kg", "estatura_cm", "fecha_debut"]
df = df.drop_duplicates(subset=columnas)

# 11. Guardar
df.to_excel("boxeadores_pro_clean.xlsx", index=False)
print(df.shape)
print(df.isna().sum())
