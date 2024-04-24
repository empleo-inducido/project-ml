# Proyecto: Clasificación de Pacientes para Detectar Dengue: Un Enfoque de Aprendizaje Automáticox
El dengue es una enfermedad causada por un virus y se transmite a las personas por la picadura del mosquito portador de la enfermedad. Actualmente no hay una vacuna para combatirlo y
es una enfermedad común en regiones tropicales y subtropicales como Centroamérica, Sudamérica y lugares donde se estanca el agua. De acuerdo con la Secretaría de Salud, en su último informe de
[Semana Epidemiológica 15](https://www.gob.mx/salud/documentos/informes-semanales-para-la-vigilancia-epidemiologica-de-dengue-2024), se menciona que, en lo que va del 2024 se han notificado 179
defunciones por probable dengue, las cuales 14 están confirmadas, 146 se encuentran en estudio y 19 se han descartado; defunciones que corresponden a diferentes estados de la república mexicana. 

## 1. Problema a resolver
El objetivo de este proyecto es poder tener un modelo de detección temprana de dengue en pacientes; saber si un paciente es probable de tener o no, esta enfermedad. Esto para poder atacar la 
enfermedad en su etapa más temprana posible.

## 2. Importancia
Como se mencionó antes, el dengue es una enfermedad de la cual aún no hay vacuna y ha sido causa de muerte, poder tener una detección temprana puede salvar la vida de una persona. Además de eso,
podría ayudar a hacer un filtrado de los pacientes y así atender más rápido a los que sean más propensos a tener dicha enfermedad, adminisitrando mejor los tiempos y recursos de los doctores y hospitales.

## 3. Métricas para medir el impacto
Dado que estamos tratando un tema de salud, preferimos que nuestro modelo detecte más casos de dengue de los que realmente hay (aunque sean falsos) que perder alguno. Por eso, nos enfocamos en maximizar 
la Sensibilidad del modelo, que mide qué tan bien atrapa los casos de dengue reales. Queremos asegurarnos de que el modelo capture la mayoría de los casos positivos, incluso si eso significa que a veces 
se equivoque y diga que alguien tiene dengue cuando no lo tiene.

## 4. Técnicas de aprendizaje 
Nuestro enfoque principal será utilizar una red neuronal artificial para abordar la clasificación de los pacientes en tres categorías distintas: "Sí", "No", y "Probable". Estas clases fueron escogidas
debido a la naturaleza de nuestros datos.

## 5. Métricas que miden la calidad del modelo de aprendizaje
Para evaluar la efectividad y la precisión de nuestro modelo, nos centraremos en la curva ROC. Esta métrica nos proporciona una visión detallada de cómo se comporta nuestro modelo en términos de
sensibilidad y especificidad en diferentes puntos de corte. Además, nos permite ajustar los umbrales de decisión para optimizar el equilibrio entre la tasa de verdaderos positivos y la tasa de falsos
positivos, lo que es crucial para garantizar una detección precisa y oportuna del dengue en los pacientes.

## 6. 


