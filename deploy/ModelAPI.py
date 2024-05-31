from fastapi import FastAPI, HTTPException
import uvicorn
import numpy as np
import mlflow
import mlflow.pyfunc

mlflow.set_tracking_uri("https://dagshub.com/empleo-inducido/project-ml.mlflow")

model_name = "testing-model"
model_version = 1

model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")

# Crear una instancia de FastAPI
app = FastAPI()

@app.post("/predict/")
def predict(data: dict):
    try:
        # Extraer los datos de entrada del diccionario usando la clave 'data'
        X = np.array(data['data'])
        # Realizar la predicción utilizando el modelo cargado
        prediction = model.predict(X)
        return {"prediction": prediction.tolist()}  # Convertir la predicción a una lista para serializarla como JSON
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Ejecutar el servidor con Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
