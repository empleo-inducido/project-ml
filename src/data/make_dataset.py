import pandas as pd
import os
import re
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import sys
import random
import yaml


def prepare_data(input_file, output_dir, seed=None, split=0.2):
    
    if not os.path.exists(input_file):
        print(f"Error: El archivo {input_file} no existe.")
        sys.exit(1)
        
    if seed:
        random.seed(seed)
        
    # Lectura del archivo
    raw_df = pd.read_csv(input_file)

    # Seleccionar columnas irrelevantes
    columnas_irrelevantes = ['FECHA_ACTUALIZACION', 'ID_REGISTRO', 'HABLA_LENGUA_INDIG', 'INDIGENA','ENTIDAD_UM_NOTIF',
                'MUNICIPIO_UM_NOTIF', 'INSTITUCION_UM_NOTIF', 'DICTAMEN', 'TOMA_MUESTRA', 'ENTIDAD_ASIG', 'MUNICIPIO_ASIG'
                ]

    # Limpiamos
    df = raw_df.drop(columnas_irrelevantes, axis=1)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df['FECHA_SIGN_SINTOMAS'] = pd.to_datetime(df['FECHA_SIGN_SINTOMAS'])



    # Creamos nuevas caracteristicas

    ############################ PCA geograficas ##################################
    # Seleccionamos columnas geograficas
    columnas_a_codificar = ['ENTIDAD_RES', 'MUNICIPIO_RES']

    # Obtenemos las variables dummies
    df_codificado = pd.get_dummies(df, columns=columnas_a_codificar)

    # Seleccionamos las columnas dummies creadas
    columnas_geograficas = [col for col in df_codificado.columns if re.match(r'^(ENTIDAD_RES_|MUNICIPIO_RES_)', col)]

    # Inicializar PCA con todos los componentes
    pca1 = PCA()

    # Ajustar PCA a los datos
    pca1.fit(df_codificado[columnas_geograficas])

    # Calcular la varianza explicada acumulativa
    varianza_acumulativa = np.cumsum(pca1.explained_variance_ratio_)

    # Encontrar el número de componentes que superan el umbral de varianza
    n_componentes = np.argmax(varianza_acumulativa > 0.6)

    # Crear una nueva instancia de PCA con el número de componentes seleccionados
    pca = PCA(n_components=n_componentes)

    # Ajustamos el modelo PCA a los datos
    df_pca = pca.fit_transform(df_codificado[columnas_geograficas])

    # Nombres para las nuevas columnas PCA
    nombres_pca = [f'PCA_GEOGRAFICO_{i+1}' for i in range(n_componentes)] 

    # Creamos un DataFrame a partir de los componentes PCA
    df_pca = pd.DataFrame(df_pca, columns=nombres_pca)

    # Concatenamos el DataFrame original y el DataFrame con los componentes PCA
    df = pd.concat([df, df_pca], axis=1)



    ############################# PCA Comorbilidad ###################################
    # Seleccionamos columnas de comorbilidad
    columnas_comorbilidad = ['HEMORRAGICOS', 'DIABETES', 'HIPERTENSION', 'ENFERMEDAD_ULC_PEPTICA', 'ENFERMEDAD_RENAL', 'INMUNOSUPR', 'CIRROSIS_HEPATICA']

    # Inicializar PCA con todos los componentes
    pca1 = PCA()

    # Ajustar PCA a los datos
    pca1.fit(df_codificado[columnas_comorbilidad])

    # Calcular la varianza explicada acumulativa
    varianza_acumulativa = np.cumsum(pca1.explained_variance_ratio_)

    # Encontrar el número de componentes que superan el umbral de varianza
    n_componentes = np.argmax(varianza_acumulativa > 0.9)

    # Crear una nueva instancia de PCA con el número de componentes seleccionados
    pca = PCA(n_components=n_componentes)

    # Ajustamos el modelo PCA a los datos
    df_pca = pca.fit_transform(df_codificado[columnas_comorbilidad])

    # Nombres para las nuevas columnas PCA
    nombres_pca = [f'PCA_COMORBILIDAD_{i+1}' for i in range(n_componentes)]

    # Crea un DataFrame a partir de los componentes PCA
    df_pca = pd.DataFrame(df_pca, columns=nombres_pca)

    # Concatena el DataFrame original y el DataFrame con los componentes PCA
    df = pd.concat([df, df_pca], axis=1)



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
    split = params["split"]
    seed = params["seed"]

    # Obtener los argumentos de línea de comandos
    input_file = sys.argv[1]
    output_dir = 'data/processed/'
    # Llamar a la función para preparar los datos
    prepare_data(input_file, output_dir, seed, split)