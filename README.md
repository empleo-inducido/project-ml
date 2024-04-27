# Proyecto: Clasificación de Pacientes para Detectar Dengue: Un Enfoque de Aprendizaje Automático

El dengue es una infección vírica que se transmite de los mosquitos infectados a las personas. Es más frecuente en las regiones de climas tropicales y subtropicales como Centroamérica, Sudamérica y lugares donde se estanca el agua.

La mayoría de las personas que contraen dengue no tienen síntomas. Cuando estos aparecen, suelen ser fiebre alta, dolor de cabeza y en otras partes del cuerpo, náuseas y erupciones en la piel. En la mayoría de los casos se mejora en una o dos semanas. Algunas personas desarrollan dengue grave y necesitan atención hospitalaria. En los casos graves, el dengue puede ser mortal. 

El riesgo de contraer dengue se puede reducir protegiéndose de las picaduras de los mosquitos, sobre todo durante el día.

Aunque el dengue se trata con medicamentos que alivian el dolor, por el momento no hay ningún tratamiento específico ni una vacuna para combatirlo. De acuerdo con la Secretaría de Salud, en su último informe de [Semana Epidemiológica 15](https://www.gob.mx/salud/documentos/informes-semanales-para-la-vigilancia-epidemiologica-de-dengue-2024), se menciona que, en lo que va del 2024 se han notificado 179 defunciones por probable dengue, las cuales 14 están confirmadas, 146 se encuentran en estudio y 19 se han descartado; defunciones que corresponden a diferentes estados de la república mexicana. 

## 1. Problema a resolver
El proyecto tiene como objetivo fundamental desarrollar un modelo de detección temprana de dengue en pacientes, permitiendo determinar si un individuo es susceptible de estar infectado con la enfermedad o no. Esta iniciativa se enfoca en identificar los signos y síntomas característicos del dengue en etapas incipientes, lo que posibilita una intervención médica precoz y efectiva. Al detectar la enfermedad en sus primeras fases, se pueden implementar estrategias de tratamiento y prevención de manera oportuna, reduciendo así el riesgo de complicaciones graves y contribuyendo a un mejor pronóstico para los pacientes afectados.

## 2. Importancia
El proyecto tiene una importancia crítica debido a la grave amenaza que representa el dengue para la salud pública. Dada la ausencia de una vacuna efectiva contra esta enfermedad y su historial como causa de numerosas muertes, la detección temprana adquiere un papel crucial. Identificar rápidamente a los pacientes con dengue permite iniciar un tratamiento oportuno, lo que puede marcar la diferencia entre la vida y la muerte para aquellos afectados.

Además de su impacto en la mortalidad, la detección temprana ofrece beneficios significativos en la gestión de recursos médicos y la eficiencia del sistema de atención sanitaria. Al implementar un sistema de detección precoz, se puede realizar un filtrado efectivo de pacientes, priorizando la atención médica hacia aquellos que presentan una mayor probabilidad de estar infectados con dengue. Esta estrategia optimiza los recursos hospitalarios y el tiempo de los profesionales de la salud, garantizando una respuesta rápida y adecuada a las necesidades de los pacientes en riesgo. De esta manera, se mejora la capacidad de los hospitales para hacer frente a brotes de dengue y se reduce la carga sobre el sistema de salud en general..

## 3. Métricas para medir el impacto del modelo de aprendizaje

- **Reducción de la Mortalidad:** Medir la disminución en el número de muertes causadas por el dengue como resultado de la detección temprana y el tratamiento oportuno proporcionado por el modelo.

- **Reducción de la Morbilidad:** Medir la disminución en la gravedad de los síntomas y complicaciones asociadas con el dengue entre los pacientes identificados tempranamente por el modelo, lo que podría traducirse en menos hospitalizaciones y una recuperación más rápida.

- **Prevención de Brotes:** Medir la capacidad del modelo para prevenir la propagación del dengue al identificar y aislar rápidamente a los pacientes infectados, lo que podría reducir la incidencia de brotes epidémicos en la comunidad.

- **ficiencia en la Utilización de Recursos:** Medir la optimización de los recursos médicos y financieros al evitar diagnósticos erróneos y tratamientos innecesarios mediante una detección más precisa y temprana del dengue.

- **Reducción de Costos de Salud:** Medir el ahorro en los costos asociados con el tratamiento y manejo de casos graves de dengue al identificar y tratar los casos de manera temprana, lo que podría reducir la necesidad de intervenciones médicas costosas y prolongadas.


## 4. Técnicas de aprendizaje 
El problema de aprendizaje que estamos abordando implica la clasificación de pacientes en tres categorías distintas: "Confirmado", "Descartado" y "Sospechoso". En este contexto, estamos utilizando una red neuronal artificial como enfoque principal para realizar esta clasificación. Las clases "Confirmado" y "Descartado" representan la presencia o ausencia confirmada de dengue en los pacientes, respectivamente, mientras que la clase "Sospechoso" indica una incertidumbre o un estado intermedio en la detección de la enfermedad. Estas clases fueron seleccionadas teniendo en cuenta la naturaleza de nuestros datos y la necesidad de abordar diferentes escenarios de diagnóstico para el dengue.

## 5. Métricas que miden la calidad del modelo de aprendizaje

- **Curva ROC**

Para evaluar la efectividad y precisión de nuestro modelo, nos centraremos en la curva ROC. Esta métrica nos proporciona una visión detallada de cómo se comporta nuestro modelo en términos de sensibilidad y especificidad en diferentes puntos de corte. La curva ROC es especialmente útil porque nos permite ajustar los umbrales de decisión para optimizar el equilibrio entre la tasa de verdaderos positivos y la tasa de falsos positivos, lo que es crucial para garantizar una detección precisa y oportuna del dengue en los pacientes.

- **Sensibilidad (Recall):** Dada la naturaleza delicada del tema de salud que abordamos, es esencial elegir cuidadosamente las métricas para evaluar el impacto y la efectividad de nuestro modelo de detección temprana de dengue. En este contexto, la sensibilidad del modelo representa una métrica fundamental. La sensibilidad, también conocida como la tasa de verdaderos positivos, nos indica qué tan bien el modelo identifica correctamente los casos de dengue reales entre todos los casos positivos.

Al maximizar la sensibilidad, nos aseguramos de capturar la mayoría de los casos de dengue reales. Esto es crucial para garantizar una detección temprana y un tratamiento oportuno, lo que contribuye a reducir la propagación de la enfermedad y minimizar su impacto en la salud pública.

En un contexto de salud, es preferible errar en el lado de la precaución. Es decir, es mejor tener algunos falsos positivos (personas diagnosticadas incorrectamente como portadoras de dengue) que correr el riesgo de pasar por alto un caso real de la enfermedad. Maximizar la sensibilidad del modelo garantiza que seamos diligentes en la identificación y atención de los pacientes que podrían estar en riesgo.

**Especificidad:**  La especificidad del modelo mide la proporción de casos negativos reales que son correctamente identificados como negativos por el modelo. Una alta especificidad es importante para evitar diagnósticos incorrectos y minimizar los falsos positivos, lo que garantiza una gestión eficiente de los recursos médicos.

**Accuracy (Exactitud):** El accuracy nos brinda una medida general de la precisión del modelo al clasificar tanto los casos positivos como los negativos. Aunque la curva ROC nos proporciona información detallada sobre el rendimiento del modelo en diferentes umbrales de decisión, el accuracy sigue siendo una métrica relevante para evaluar la efectividad global del modelo en comparación con un modelo de referencia simple como la predicción aleatoria.


## 6. ¿Como están alineadas las métricas de la calidad del modelo con las métricas de impacto de la solución?
Las métricas de calidad del modelo y las métricas de impacto de la solución están intrínsecamente relacionadas, ya que la calidad del modelo afecta directamente el impacto que la solución tiene en el problema que se está abordando. Aquí hay algunas formas en que estas métricas pueden estar alineadas y cómo se relacionan:

**Sensibilidad y detección temprana:** La sensibilidad del modelo es una métrica clave que mide la capacidad del modelo para detectar correctamente los casos positivos. En el contexto de la detección temprana de dengue, una alta sensibilidad significa que el modelo puede identificar la mayoría de los casos de dengue reales, lo que contribuye directamente a una detección más temprana de la enfermedad en los pacientes. Cuanto mayor sea la sensibilidad, mayor será el impacto en la detección temprana y en la aplicación de tratamientos oportunos.

**Especificidad y reducción de falsos positivos:** Si bien la sensibilidad es crucial, también es importante minimizar los falsos positivos para evitar diagnósticos erróneos y el uso inadecuado de recursos médicos. La especificidad del modelo mide la capacidad para identificar correctamente los casos negativos. Reducir los falsos positivos contribuye a una mejor gestión de recursos y a una atención más efectiva de los pacientes. Cuanto mayor sea la especificidad, menor será el número de casos erróneamente diagnosticados como positivos, lo que aumenta la eficiencia y eficacia de la solución.

**Accuracy y confianza en el modelo:** El accuracy del modelo proporciona una medida general de su precisión al clasificar tanto casos positivos como negativos. Un alto accuracy indica una mayor confianza en las predicciones del modelo. Esta confianza es fundamental para que los profesionales de la salud y los responsables de la toma de decisiones confíen en la solución y la implementen de manera efectiva en entornos clínicos. Cuanto mayor sea el accuracy, mayor será la confianza en la solución y, por lo tanto, su impacto en la detección y tratamiento de la enfermedad.

science project template</a>. #cookiecutterdatascience</small></p>
