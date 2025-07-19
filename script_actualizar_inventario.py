import pandas as pd
import json

df = pd.read_excel('inventario.xlsx')

df_renombrado = df.rename(columns={
    'codigo': 'Código',
    'producto': 'Producto',
    'Existencia': 'Existencia',
    'costo': 'Costo ($)',
    'pvp': 'PVP ($)'
})

datos = df_renombrado.to_dict(orient='records')

with open('inventario.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, ensure_ascii=False, indent=4)

print('✅ inventario.json generado correctamente.')
