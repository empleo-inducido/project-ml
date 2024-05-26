import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import yaml


def prepare_data(input_file, output_dir, seed=None, split=0.2):
    
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

    train, test = train_test_split(df, test_size=split, random_state=seed)
    
    os.makedirs(output_dir, exist_ok=True)
    train_dir = os.path.join(output_dir, 'train')
    test_dir = os.path.join(output_dir, 'test')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Guardamos
    save_data(train, os.path.join(train_dir, 'train-dengue.csv'))
    save_data(test, os.path.join(test_dir, 'test-dengue.csv'))

def save_data(data, path):
    data.to_csv(path, index=False)

if __name__ == "__main__":
    params = yaml.safe_load(open("/home/project/params.yaml"))["make_dataset"]
    seed = params["seed"]
    split = params["split"]

    # Obtener los argumentos de línea de comandos
    input_file = "/home/project/data/raw/dengue-raw.csv"
    output_dir = 'data/processed/'
    # Llamar a la función para preparar los datos
    prepare_data(input_file, output_dir, seed, split)