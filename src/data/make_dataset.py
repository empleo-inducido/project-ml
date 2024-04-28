import pandas as pd
import os

# Lectura del archivo
raw_df = pd.read_csv('/home/project/data/raw/dengue-raw.csv')

# Seleccionar columnas irrelevantes
columnas_irrelevantes = ['FECHA_ACTUALIZACION', 'ID_REGISTRO', 'HABLA_LENGUA_INDIG', 'INDIGENA','ENTIDAD_UM_NOTIF',
            'MUNICIPIO_UM_NOTIF', 'INSTITUCION_UM_NOTIF', 'DICTAMEN', 'TOMA_MUESTRA', 'ENTIDAD_ASIG', 'MUNICIPIO_ASIG'
            ]

# Limpiamos
df = raw_df.drop(columnas_irrelevantes, axis=1)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df['FECHA_SIGN_SINTOMAS'] = pd.to_datetime(df['FECHA_SIGN_SINTOMAS'])

# Guardamos
if not os.path.exists('/home/project/data/processed/'):
    os.makedirs('/home/project/data/processed/')
df.to_csv('/home/project/data/processed/dengue-processed.csv', index=False)