# DataLake_ProyectoFinal

# Proyecto Final Análisis de datos

Diseñar una arquitectura de Data Lake en la cual tenga el insumo de datos de al menos las siguientes fuentes:

3 bases de datos SQL

3 bases de datos NoSQL


Estas fuentes deben tener a su vez como insumo fuentes de Internet (facebook, twitter, webscrapping, tiktok, linkedin) y además archivos estáticos de kaggle, INEC, etc.

Como concentrador de datos debe utilizar elasticsearch y con datos actualizados, realizar un caso de estudio para cada una de las siguientes temáticas:


* Pulso político en 20 ciudades principales de Ecuador, listas y candidatos, presidenciales y diputados.

* Pulso político por provincias en Ecuador, listas y candidatos, presidenciales y diputados.

* Juegos en línea por países.

* Tema definido por el estudiante.

* Eventos o noticias mundiales.


La recopilación de información se puede realizar con geolocalización o con filtro de palabras. Si se utiliza geolocalización se recomienda subdividir la región. Si se utiliza filtro de palabras se recomienda usar varias palabras por script.
Se debe crear la indexación en al menos 2 nodos. (debe crear un clúster)

Para las visualizaciones en tiempo real se usará Kibana, para los dashboards estáticos se utilizará cualquier otra herramienta.
Cada caso de estudio debe tener su propio dashboard y de todo el proyecto al menos una visualización debe tener geolocalización.

# SCRIPTS -- BD SQL

* SQL LITE --- TIKTOK

![image](https://user-images.githubusercontent.com/58041699/133362509-725d8840-3013-4a63-9685-f35397f7c9bc.png)

* SQL LITE --- KAGGLE(CSV)

En la pagina de KAGGLE podemos contar con dataset's de una gran variedad de temas, para esta practica haremos uso de un dataset sobre las variantes del covid.

![image](https://user-images.githubusercontent.com/58041699/133369877-feda218e-6ad1-4a29-a8a2-a99693efabf7.png)

![image](https://user-images.githubusercontent.com/58041699/133370546-0acecbed-11a7-417e-860b-0d9d7809d17f.png)


Ese dataset que adquirimos podemos trasladarlo a un gestor base de datos como sql lite, de esta manera esos datos seran registros de una tabla relacional.

![image](https://user-images.githubusercontent.com/58041699/133370797-5cbec501-f64b-4007-96e5-fc4495ed9c21.png)

Una vez importada la data, ya hemos conseguido una BD SQL donde podemos observar las dominios de cada columnas.
![image](https://user-images.githubusercontent.com/58041699/133370878-3eba2c9e-861e-493c-aef6-9ab3f1534a2a.png)

* MYSQL-(PHPMYADMIN) --- INEC

Dentro de la pagina oficial del Instituto Nacional de Estadística y Censos, podemos encontrar informacion a nivel demografico, educacional, salud y bienestar, economia, agricultura, ambiental y entre otros acerca de estado de nuestro Pais.
![image](https://user-images.githubusercontent.com/58041699/133373411-6fd4e9fa-8cc9-485c-84e9-246b14631f83.png)

De esta manera usaremos datos del INCE para realizar la practica. El tema trata del Índice de Nivel de Actividad Registrada (INA-R) donde extreremos el desempeño económico-fiscal de los sectores productivos de la economía nacional entre el año 2016

![image](https://user-images.githubusercontent.com/58041699/133374678-c8d94add-8d02-4330-8312-3e8125817327.png)







# SCRIPTS -- BD NOSQL




# ELASTICSEARCH -- CONCENTRADOR DE DATOS
