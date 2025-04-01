
# Employees Globant Challenge

El presente proyecto incluye un REST API que permite añadir registros a una base de datos. Se puede añadir información a tres tablas:

* employees
* departments
* jobs

Se debe realizar una llamada con método POST con los siguientes datos:

* params: {'table': table_name}; en donde table_name puede ser employees, departments o jobs.
* body: {'file': file}; en donde file es el archivo en formato .csv. Esto se envía como form-data.

La base de datos se llama challenge_db y esta no es necesario crearla previamente. El método POST ya lo realiza si es que no existe. Las columnas de los csv deben enviarse en el mismo orden en el que se enviaron los archivos de muestra.

Se adjunta adicionalmente el Dockerfile para poder desplegar su respectiva imagen en un contenedor.

