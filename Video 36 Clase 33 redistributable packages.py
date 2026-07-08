# ====================================================================================
# REDISTRIBUTABLE PACKAGES
# ====================================================================================
#
# Como crear paquetes distribuibles en Python?
#
# Primero hay que crear un paquete
#
# Segundo hay que instalarlo.
# ====================================================================================
#
# Para crear un distribuibles Packaes en Python
#
# Primero hay que crear un package puede tener sub packaes 
#
# Y tambiern debe contener modulos
# ====================================================================================
#
# Que pasa si muevo el archivo donde estoy usando los modulos y package? por ejemplo Uso Modulos Pakcets.py
#
# Pues no nos dejaria usarlo.
#
# Distribuir un paquete los que no hara poder usar nuestro package sub packages o modulos desde cualquier sitio sin importar la ruta
# ====================================================================================
# Par hacer esto debemos crear un archivo llamado setup.py
#
# Luego de tener nuestro archivo setup.py
#
# En la primera linea debemos colocar lo siguiente:
#
# from setuptools import setup
#
# Esto es para decirle a python que estamos creando un setup y queremos usar esa herramienta\
#
# Luego se usa la funcion setup() y dentro de los parentesis o en los argumentos es donde se incluyen los datos de configuracion
#
# Por ejemplo el nombre del paquete
#
# Para eso utilizaremos Name = "nombre del paquete" + ,
#
# leuegoo se debe especificar la version con version en caso de que queramos se actualizarlo en un futuro
#
# Luego uan descripcion con description para esxplicar brevemente el paquete
#
# Luego el autor con la propeidad author para especificar el autor
#
# y tambien tenemos la propiedad author_email que especifica el email del autor
#
# Tambien se puede especificar una URL con url
#
# y tambien se pueden agregar mas propiedades pero la mas importante es packages, aqui especificaremos donde se encuentra el paquete o subpaquete que vayamos a usar
# para esto usamos package + = + [] dentro de los corchetes debe ir la ruta por ejemplo packages = ["Calculus","Calculus.redondeo_potencia"] el primero es la carpeta raiz luego de escribir la dcarpeta raiz la separamos por , y luego abrimos "" dentro de los "" va el sub paquete que eremos importar en este caso se haria de la siguiente manera Calculus.redondeo_potencia en pocas palabras debe ir el nombre de la carpeta raiz + . + nombre del sub paquete
#
# Mas o menos se veria asi
#
# setup(
#        name = "paquete calculos",
#        version = "1.0",
#        description = "Paquete de redondeo y potencia"
#        author = "Henger",
#        author_email = "Hengertg@gmail.com",
#        url = "www.Urlexample.com",
#        packages = ["Calculus","Calculus.redonde_potencia"]
#
#
#
#        )
#
# Una vez hecho todo eso debemos buscar o copiar la ruta donde se encuentra el setup.py desde la consola para acceder a la carpeta donde se encuentra el setup.py
#
# Luego en la consola escribimos python setup.py sdist
#
# Explicacion: python + el nombre del setup.py + sdist
#
# Tambien se puede usar py
#
# Ejemplo:
#
# py setup.py sdist
#
# Explicacion: py + nombre del setup.py + sdist
# 
# sdist es para crear el paquete distribuible
#
# Si todo ha ido bien deberiamos tener 2 carpetas en la ruta del archivo setup.py
#
# Que serian paquetecalculos.egg-info y dist
#
# si abrimos la carpeta dist en su interior habra un archivo .tar.gz
#
# es un acrhivo compromido en linux .tar.gz es el archivo de compreso default
#
# En windows se abriria con winrar or zip o calquier compresor de archivos
#
# Bueno para instalar el paquete que hemos creado o que hemos descargado o que nos han pasado
#
# Debemos en la consolar con CD acceder a la ruta donde esta el archivo .tar.gz el dist
#
# y usariamos el siguiente comando que seria pip3 install nombre del paquete
#
# Ejemplo seria: pip3 install paquetecalculos-1.0.tar.gz
#
# En la consola de windows si ponemos las 2 primeras letra y luego presionamos tab nos completara el nombre del archivo automaticamente
#
# En Visual Studio Code es mas faicl ya que Visual Studio Code tiene una consola predeterminada y podemos usar esa en vez  de abrir la consola de windows
#
# Una vez instalado solo deberiamos importarlo en el archivo que usaremos para trabajar yg que seria de la siguiente manera
#
# from Calculus.basics.Operaciones_Basicas import *
#
# Explicacion mas detallada: from + Nombre del paquete + . + nombre del sub paqute + nombre del modulo + import + especifacmos la funcion a la que queremos acceder
#
# Para desisntalar un paquete es tan facil y sencillo como usar pip3 uninstall nombre del paquete
#
# Explicacion mas detalalda: pip3 + uninstall + nombre del paquete