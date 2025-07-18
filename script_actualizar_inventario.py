import pandas as pd

df = pd.read_excel('inventario.xlsx')

df.rename(columns={
    'Código': 'codigo',
    'Producto': 'producto',
    'Exist.': 'existencia',
    'Costo ($)': 'costo',
    'PVP ($)': 'pvp'
}, inplace=True)

df.to_json('inventario.json', orient='records', force_ascii=False, indent=2)

print('Archivo inventario.json generado correctamente.')
