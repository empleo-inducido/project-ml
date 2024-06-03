# Proyecto: Clasificación de Pacientes para Detectar Dengue: Un Enfoque de Aprendizaje Automático

El dengue es una infección vírica que se transmite de los mosquitos infectados a las personas. Es más frecuente en las regiones de climas tropicales y subtropicales como Centroamérica, Sudamérica y lugares donde se estanca el agua.

La mayoría de las personas que contraen dengue no tienen síntomas. Cuando estos aparecen, suelen ser fiebre alta, dolor de cabeza y en otras partes del cuerpo, náuseas y erupciones en la piel. En la mayoría de los casos se mejora en una o dos semanas. Algunas personas desarrollan dengue grave y necesitan atención hospitalaria. En los casos graves, el dengue puede ser mortal. 

El riesgo de contraer dengue se puede reducir protegiéndose de las picaduras de los mosquitos, sobre todo durante el día.

Aunque el dengue se trata con medicamentos que alivian el dolor, por el momento no hay ningún tratamiento específico ni una vacuna para combatirlo. De acuerdo con la Secretaría de Salud, en su último informe de [Semana Epidemiológica 15](https://www.gob.mx/salud/documentos/informes-semanales-para-la-vigilancia-epidemiologica-de-dengue-2024), se menciona que, en lo que va del 2024 se han notificado 179 defunciones por probable dengue, las cuales 14 están confirmadas, 146 se encuentran en estudio y 19 se han descartado; defunciones que corresponden a diferentes estados de la república mexicana. 

## 1. Problema a resolver
El proyecto tiene como objetivo fundamental desarrollar un modelo de detección temprana del tipo de paciente de dengue, permitiendo determinar si un individuo deberá tratrse de manera hospitalaria u ambulatoria. Esta iniciativa se enfoca en identificar los signos y características de los pacientes de manejo hospitalario, lo que posibilita una intervención médica efectiva. Al detectar la enfermedad en sus primeras fases, se pueden implementar estrategias de tratamiento y prevención de manera oportuna, reduciendo así el riesgo de complicaciones graves y contribuyendo a un mejor pronóstico para los pacientes afectados.

## 2. Importancia
El proyecto tiene una importancia crítica debido a la grave amenaza que representa el dengue para la salud pública. Dada la ausencia de una vacuna efectiva contra esta enfermedad y su historial como causa de numerosas muertes, la detección temprana adquiere un papel crucial. Identificar rápidamente a los pacientes que deben hospitalizarse permite iniciar un tratamiento oportuno, lo que puede marcar la diferencia entre la vida y la muerte para aquellos afectados.

Además de su impacto en la mortalidad, la detección temprana ofrece beneficios significativos en la gestión de recursos médicos y la eficiencia del sistema de atención sanitaria. Al implementar un sistema de detección precoz, se puede realizar un filtrado efectivo de pacientes, priorizando la atención médica hacia aquellos que presentan una mayor probabilidad de sufrir complicaciones. Esta estrategia optimiza los recursos hospitalarios y el tiempo de los profesionales de la salud, garantizando una respuesta rápida y adecuada a las necesidades de los pacientes en riesgo. De esta manera, se mejora la capacidad de los hospitales para hacer frente a brotes de dengue y se reduce la carga sobre el sistema de salud en general..

## 3. Métricas para medir el impacto del modelo de aprendizaje

Además de las métricas tradicionales de calidad del modelo, es importante considerar el impacto clínico y operativo del modelo. Aquí se presentan algunas métricas específicas para evaluar dicho impacto:

### 1. Tasa de Hospitalización Correcta
Esta métrica mide el porcentaje de pacientes que realmente necesitan hospitalización y que son correctamente identificados por el modelo.

\[ \text{Tasa de Hospitalización Correcta} = \frac{\text{Pacientes Hospitalizados Correctamente Identificados}}{\text{Total de Pacientes que Requieren Hospitalización}} \]

### 2. Tasa de Manejo Ambulatorio Correcto
Mide el porcentaje de pacientes que pueden ser manejados ambulatoriamente y que son correctamente identificados por el modelo.

\[ \text{Tasa de Manejo Ambulatorio Correcto} = \frac{\text{Pacientes Ambulatorios Correctamente Identificados}}{\text{Total de Pacientes que Pueden Ser Ambulatorios}} \]

### 3. Costo de Falsos Positivos (CFP)
Evalúa el costo asociado con clasificar incorrectamente a un paciente como hospitalario cuando no lo necesita, lo que puede resultar en recursos hospitalarios desperdiciados.

\[ \text{CFP} = \text{Costo por Falso Positivo} \times \text{Número de Falsos Positivos} \]

### 4. Costo de Falsos Negativos (CFN)
Evalúa el costo asociado con clasificar incorrectamente a un paciente como ambulatorio cuando realmente necesita hospitalización, lo que puede llevar a complicaciones de salud y costos de tratamiento adicionales.

\[ \text{CFN} = \text{Costo por Falso Negativo} \times \text{Número de Falsos Negativos} \]

### 5. Ahorro en Recursos Hospitalarios
Calcula el ahorro en recursos hospitalarios (como camas, personal médico y medicación) debido a la correcta identificación de pacientes ambulatorios.

\[ \text{Ahorro en Recursos Hospitalarios} = \text{Recursos Ahorrados por Manejo Ambulatorio Correcto} \times \text{Número de Pacientes Ambulatorios Correctamente Identificados} \]

### 6. Mejora en la Capacidad Hospitalaria
Mide el aumento en la capacidad del hospital para manejar casos graves debido a una mejor clasificación de pacientes ambulatorios.

\[ \text{Mejora en la Capacidad Hospitalaria} = \frac{\text{Número de Pacientes Ambulatorios Correctamente Identificados}}{\text{Capacidad Total del Hospital}} \]

### 7. Tiempo de Respuesta Médica
Evalúa la reducción en el tiempo de respuesta médica debido a la correcta clasificación de pacientes, permitiendo un tratamiento más rápido y eficiente.

\[ \text{Reducción en el Tiempo de Respuesta} = \text{Tiempo Promedio de Respuesta Antes del Modelo} - \text{Tiempo Promedio de Respuesta Después del Modelo} \]


## 4. Técnicas de aprendizaje 
El problema de aprendizaje que estamos abordando implica la clasificación de pacientes en tres categorías distintas: "Confirmado", "Descartado" y "Sospechoso". En este contexto, estamos utilizando una red neuronal artificial como enfoque principal para realizar esta clasificación. Las clases "Confirmado" y "Descartado" representan la presencia o ausencia confirmada de dengue en los pacientes, respectivamente, mientras que la clase "Sospechoso" indica una incertidumbre o un estado intermedio en la detección de la enfermedad. Estas clases fueron seleccionadas teniendo en cuenta la naturaleza de nuestros datos y la necesidad de abordar diferentes escenarios de diagnóstico para el dengue.

## 5. Métricas que miden la calidad del modelo de aprendizaje

- **Curva ROC**

Para evaluar la efectividad y precisión de nuestro modelo, nos centraremos en la curva ROC. Esta métrica nos proporciona una visión detallada de cómo se comporta nuestro modelo en términos de sensibilidad y especificidad en diferentes puntos de corte. La curva ROC es especialmente útil porque nos permite ajustar los umbrales de decisión para optimizar el equilibrio entre la tasa de verdaderos positivos y la tasa de falsos positivos, lo que es crucial para garantizar una detección precisa y oportuna del dengue en los pacientes.

Para evaluar la calidad de un modelo de identificación de pacientes hospitalarios vs ambulatorios para el dengue, es crucial utilizar una variedad de métricas que proporcionen una visión completa del desempeño del modelo. A continuación, se describen algunas de las métricas más relevantes:

### 1. Exactitud (Accuracy)
La exactitud mide el porcentaje de predicciones correctas sobre el total de predicciones. Es una métrica general que puede ser útil, pero no siempre es adecuada en casos de desbalance de clases.

\[ \text{Exactitud} = \frac{TP + TN}{TP + TN + FP + FN} \]

### 2. Precisión (Precision)
La precisión, también conocida como valor predictivo positivo, mide la proporción de verdaderos positivos sobre el total de predicciones positivas. Es especialmente importante cuando el costo de una falsa alarma es alto.

\[ \text{Precisión} = \frac{TP}{TP + FP} \]

### 3. Sensibilidad o Recall
La sensibilidad, también conocida como recall o tasa de verdaderos positivos, mide la proporción de verdaderos positivos sobre el total de positivos reales. Es crucial para asegurarse de que los casos de pacientes hospitalarios se identifican correctamente.

\[ \text{Sensibilidad} = \frac{TP}{TP + FN} \]

### 4. Especificidad
La especificidad mide la proporción de verdaderos negativos sobre el total de negativos reales. Es útil para evaluar cómo el modelo maneja los pacientes ambulatorios.

\[ \text{Especificidad} = \frac{TN}{TN + FP} \]

### 5. Valor Predictivo Negativo (NPV)
El valor predictivo negativo mide la proporción de verdaderos negativos sobre el total de predicciones negativas.

\[ \text{NPV} = \frac{TN}{TN + FN} \]

### 6. F1-Score
El F1-Score es la media armónica de la precisión y la sensibilidad, proporcionando una métrica balanceada que considera tanto falsos positivos como falsos negativos.

\[ \text{F1-Score} = 2 \cdot \frac{\text{Precisión} \cdot \text{Sensibilidad}}{\text{Precisión} + \text{Sensibilidad}} \]

### 7. Área Bajo la Curva ROC (AUC-ROC)
El AUC-ROC mide la capacidad del modelo para distinguir entre las clases. Un valor de AUC cercano a 1 indica un modelo excelente, mientras que un valor cercano a 0.5 indica un modelo que no tiene capacidad discriminativa.

### 8. Matriz de Confusión
Una matriz de confusión proporciona una visualización detallada de las predicciones del modelo, mostrando los verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos. Esto ayuda a entender mejor los errores del modelo.

### 9. Curva de Precisión-Recall (PRC)
La curva de precisión-recall es especialmente útil en situaciones de desbalance de clases. Mide la relación entre la precisión y el recall en diferentes umbrales de probabilidad.


## 6. ¿Como están alineadas las métricas de la calidad del modelo con las métricas de impacto de la solución?

Las métricas de calidad del modelo y las métricas de impacto de la solución están intrínsecamente relacionadas, ya que la calidad del modelo afecta directamente el impacto que la solución tiene en el problema que se está abordando. Aquí hay algunas formas en que estas métricas pueden estar alineadas y cómo se relacionan:

### 1. Exactitud (Accuracy)
**Calidad del Modelo:**
- Mide el porcentaje de predicciones correctas sobre el total de predicciones.

**Impacto de la Solución:**
- Una alta exactitud indica que el modelo hace un buen trabajo general identificando correctamente tanto a pacientes hospitalarios como ambulatorios, lo que puede llevar a una distribución eficiente de recursos hospitalarios.

### 2. Precisión (Precision)
**Calidad del Modelo:**
- Mide la proporción de verdaderos positivos sobre el total de predicciones positivas.

**Impacto de la Solución:**
- Alta precisión significa menos falsos positivos, lo que reduce la asignación innecesaria de recursos hospitalarios para pacientes que no lo necesitan, disminuyendo el Costo de Falsos Positivos (CFP).

### 3. Sensibilidad o Recall
**Calidad del Modelo:**
- Mide la proporción de verdaderos positivos sobre el total de positivos reales.

**Impacto de la Solución:**
- Alta sensibilidad asegura que los pacientes que realmente necesitan hospitalización sean identificados correctamente, reduciendo el Costo de Falsos Negativos (CFN) y mejorando la Tasa de Hospitalización Correcta.

### 4. Especificidad
**Calidad del Modelo:**
- Mide la proporción de verdaderos negativos sobre el total de negativos reales.

**Impacto de la Solución:**
- Alta especificidad significa que el modelo identifica correctamente a los pacientes que no necesitan hospitalización, mejorando la Tasa de Manejo Ambulatorio Correcto y optimizando la utilización de recursos ambulatorios.

### 5. F1-Score
**Calidad del Modelo:**
- Combina precisión y sensibilidad en una métrica única y balanceada.

**Impacto de la Solución:**
- Un F1-Score alto indica un buen equilibrio entre precisión y sensibilidad, lo cual es crucial para minimizar tanto los CFP como los CFN, y asegurar un impacto positivo general en el manejo de pacientes.

### 6. AUC-ROC
**Calidad del Modelo:**
- Mide la capacidad del modelo para distinguir entre las clases en diferentes umbrales.

**Impacto de la Solución:**
- Un alto AUC-ROC indica una capacidad robusta para diferenciar entre pacientes hospitalarios y ambulatorios, lo que facilita una mejor planificación y asignación de recursos médicos.

### 7. Matriz de Confusión
**Calidad del Modelo:**
- Proporciona una visión detallada de las predicciones correctas e incorrectas.

**Impacto de la Solución:**
- Analizar la matriz de confusión ayuda a identificar específicamente dónde el modelo falla (falsos positivos y falsos negativos), permitiendo ajustes que pueden reducir costos y mejorar la capacidad hospitalaria.

### 8. Curva de Precisión-Recall (PRC)
**Calidad del Modelo:**
- Mide la relación entre la precisión y el recall en diferentes umbrales.

**Impacto de la Solución:**
- Una buena relación precisión-recall asegura que se mantenga un balance adecuado entre la identificación de pacientes hospitalarios y ambulatorios, optimizando los recursos y minimizando el impacto negativo de errores de clasificación.



science project template</a>. #cookiecutterdatascience</small></p>
