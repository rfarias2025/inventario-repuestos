import pandas as pd
import json

# Lee el archivo Excel (debe estar en la misma carpeta)
df = pd.read_excel('inventario.xlsx')

# Renombra las columnas para que coincidan con el index.html
df_renombrado = df.rename(columns={
    'codigo': 'Código',
    'producto': 'Producto',
    'Existencia': 'Existencia',
    'costo': 'Costo ($)',
    'pvp': 'PVP ($)'
})

# Convierte a lista de diccionarios
datos = df_renombrado.to_dict(orient='records')

# Guarda en JSON con indentación bonita
with open('inventario.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, ensure_ascii=False, indent=4)

print('✅ inventario.json generado correctamente.')
