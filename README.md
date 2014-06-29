CentroInternet
==============

## Descripción

Sistema enfocado a administrar y facturar una pyme que ofrece un servicio mensual a sus clientes. En particular, se pretende llevar un registro de los clientes, historial de pago y los problemas que presenta el servicio durante el mes, con el fin de que al finalizar el mes, sea posible generar el estado de cuenta y este a su vez enviarlo a los clientes correspondientes.

### Instalación

* Descarga la herramienta de Heroku
`wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh`

* Luego instala PIP (suponiendo que tienes instalado Python 2.6 o 2.7)
`sudo apt-get install python-pip`

* Instala virtualenv 
`pip install virtualenv`

* Inicializa virtualenv
`virtualenv venv`

* Activar el virtualenv
`source venv/bin/activate`

* Añadir el proyecto
`git remote add origin https://github.com/GonzaloAfa/centrointernetv2.git`

* Hay una librería que cuesta instalar con PIP, así que instala esto:
`sudo apt-get install python-dev python-pip python-lxml libcairo2 libpango1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info`

* Instalar todas las librerías externas
`pip install -r requirements.txt`

* Para configurar la base de datos, se debe crear un archivo `.env` y situarlo en la raiz del proyecto (junto con el manager.py)
* Si se trata de una bd postgres, en archivo debe tener la siguiente información:
`DATABASE_URL=postgres://<user>:<pass>@<host>/<table>`
* En caso de usar sqlite:
`DATABASE_URL=sqlite:////home/<ruta_archivo>/<archivo>.db`

* Luego se debe crear la base de datos (Postgres o SQLite ) por medio de:
`foreman run python manager.py syncdb`

* Y para cargar algunos datos por defecto:
`python manage.py loaddata plan.json`

* Finalmente para correr el sistema, ejecuta
`foreman start`
