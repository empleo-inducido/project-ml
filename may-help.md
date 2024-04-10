### Clona el repositorio.
Dentro de la carpeta que contiene el proyecto ejecuta
```
docker compose up
```
Se creara la imagen basada en el Dockerfile y un contenedor.

Posiblemente tengas problemas con las versiones de las dependencias, la terminal te dirá que dependencias y las versiones que debes usar. 
Puede generar nuevos conflictos pero eventualmente se resoleran. Aún no soluciono eso.

Si el contenedor es creado pero se cierra inmediatamente tras iniciar, borra el contenedor y la imagen (no sé si borrar la imagen sea necesario, puedes intentarlo sin borrarla y verificarlo,
y contribuir a este archivo corrigiendolo). Posteriormente ejecuta este comando
```
docker compose up -d
```
Permite la ejecución de contenedores en segundo plano.

Aquí ya todo debería ir bien.
### VSCO
Para trabajar en el contenedor usando vsco haz clic en el icono azul de la esquina inferior izquierda. Asegurate de que el contendor este corriendo.

![image](https://github.com/empleo-inducido/project-ml/assets/78995026/25f025f0-6feb-43bd-b47d-77070275aa08)

Despues haz clic en "Attach to Running Container ..."

![image](https://github.com/empleo-inducido/project-ml/assets/78995026/db47ee0e-b6d6-4333-854b-577b2c27c89f)

Te pedirá elegir un contenedor de los que estan corriendo.

Finalmente, tendrás el proyecto abierto en vsco y ejecudandose dentro del contenedor.

### Package
Cada que instales una package actualiza el requeriments.txt

```
pip freeze > requeriments.txt
```

Se sobreescribira el archivo y ahora incluira las nuevas librerias.

Cada que retomes el proyecto asegurate de tener los paquetes al día haciendo
```
pip install -r requeriments.txt
```
