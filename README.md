CentroInternet
==============

Descripción
-------------------------

Sistema enfocado a administrar y facturar una pyme que ofrece un servicio mensual a sus clientes. En particular, se pretende llevar un registro de los clientes, historial de pago y los problemas que presenta el servicio durante el mes, con el fin de que al finalizar el mes, sea posible generar el estado de cuenta y este a su vez enviarlo a los clientes correspondientes.

Instalación
-------------------------

Corre en tu terminal
`wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh`

Luego instala PIP (suponiendo que tienes instalado Python 2.6 o 2.7)
`easy_install pip`

Instala virtualenv 
`pip install virtualenv`

Inicializa virtualenv
`virtualenv venv`

Activar el virtualenv
`source venv/bin/activate`

Instalar todas las librerías externas
`pip install -r requirements.txt`

Luego se debe crear la base de datos (SQLite) por medio de:
`python manager.py syncdb`

Y para cargar algunos datos por defecto:
`python manage.py loaddata plan.json`

Y finalmente para correr el sistema:
`foreman start`
