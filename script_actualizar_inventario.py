import pandas as pd
import json

# Lee el Excel con las columnas originales
df = pd.read_excel('inventario.xlsx')

# Renombrar las columnas al formato correcto del index.html
df_renombrado = df.rename(columns={
    'codigo': 'Código',
    'producto': 'Producto',
    'Existencia': 'Existencia',
    'costo': 'Costo ($)',
    'pvp': 'PVP ($)'
})

# Convertir a lista de diccionarios
datos = df_renombrado.to_dict(orient='records')

# Guardar en inventario.json con codificación UTF-8
with open('inventario.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, ensure_ascii=False, indent=4)

print('✅ Archivo inventario.json generado correctamente.')
