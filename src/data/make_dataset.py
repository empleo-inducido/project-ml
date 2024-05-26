import pandas as pd
import os
import re
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import random
import yaml

def prepare_data(input_file, output_dir, seed=None, split=0.2, stratify_col=None):
    if not os.path.exists(input_file):
        print(f"Error: El archivo {input_file} no existe.")
        sys.exit(1)
        
    if seed:
        np.random.seed(seed)
        
    # Lectura del archivo
    raw_df = pd.read_csv(input_file)

    # Seleccionar columnas irrelevantes
    columnas_irrelevantes = ['FECHA_ACTUALIZACION', 'ID_REGISTRO', 'HABLA_LENGUA_INDIG', 'INDIGENA', 'ENTIDAD_UM_NOTIF',
                             'MUNICIPIO_UM_NOTIF', 'INSTITUCION_UM_NOTIF', 'DICTAMEN', 'TOMA_MUESTRA', 'ENTIDAD_ASIG', 'MUNICIPIO_ASIG']

    # Limpiamos
    df = raw_df.drop(columnas_irrelevantes, axis=1)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df['FECHA_SIGN_SINTOMAS'] = pd.to_datetime(df['FECHA_SIGN_SINTOMAS'])

    ########################## Variables de fecha ###################################
    # Extraemos año, mes, día y semana
    df['ANO_SIGN_SINTOMAS'] = df['FECHA_SIGN_SINTOMAS'].dt.year
    df['MES_SIGN_SINTOMAS'] = df['FECHA_SIGN_SINTOMAS'].dt.month
    df['DIA_SIGN_SINTOMAS'] = df['FECHA_SIGN_SINTOMAS'].dt.day
    df['SEMANA_SIGN_SINTOMAS'] = df['FECHA_SIGN_SINTOMAS'].dt.isocalendar().week
    df.drop('FECHA_SIGN_SINTOMAS', axis=1, inplace=True)

    if stratify_col and stratify_col in df.columns:
        stratify_values = df[stratify_col]
    else:
        stratify_values = None

    # Dividir los datos usando el split
    train, test = train_test_split(df, test_size=split, random_state=seed, stratify=stratify_values)
    
    os.makedirs(output_dir, exist_ok=True)
    train_dir = os.path.join(output_dir, 'train')
    test_dir = os.path.join(output_dir, 'test')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Guardamos
    save_data(train, os.path.join(train_dir, 'train-dengue.csv'))
    save_data(test, os.path.join(test_dir, 'test-dengue.csv'))

    # Verificar la estratificación y la proporción del split
    if stratify_col:
        print("Distribución de la columna de estratificación en el conjunto de entrenamiento:")
        print(train[stratify_col].value_counts(normalize=True))
        print("Distribución de la columna de estratificación en el conjunto de prueba:")
        print(test[stratify_col].value_counts(normalize=True))
    
    # Verificar la proporción del split
    total_rows = df.shape[0]
    train_rows = train.shape[0]
    test_rows = test.shape[0]
    print(f"Total de filas: {total_rows}")
    print(f"Filas en el conjunto de entrenamiento: {train_rows} ({train_rows / total_rows:.2%})")
    print(f"Filas en el conjunto de prueba: {test_rows} ({test_rows / total_rows:.2%})")

def save_data(data, path):
    data.to_csv(path, index=False)

if __name__ == "__main__":
    params = yaml.safe_load(open("/home/project/params.yaml"))["make_dataset"]
    split = params["split"]
    seed = params["seed"]

    # Obtener los argumentos de línea de comandos
    input_file = sys.argv[1]
    output_dir = 'data/processed/'
    # Llamar a la función para preparar los datos
    prepare_data(input_file, output_dir, seed, split, stratify_col='ESTATUS_CASO')


