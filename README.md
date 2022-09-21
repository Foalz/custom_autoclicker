<h1 align="center">Autoclicker personalizado</h1>
<p align="center"><img src="https://www.devopsschool.com/blog/wp-content/uploads/2022/03/Python-01-2.png"/></p> 

## Tabla de contenidos:
---

- [Descripción y contexto](#descripción-y-contexto)
- [Guía de instalación](#guía-de-instalación)
- [Guía de usuario](#guía-de-usuario)
- [Cómo probarlo](#cómo-probarlo)
- [Mis redes](#mis-redes)

## Descripción y contexto
---
Autoclicker personalizado, dedicado a presionar varios botones en concreto y en realizar la funcion de escribir datos de usuario en una pantalla de login.

## Guía de instalación
---
<h2>Requerimientos para ejecutar el script</h2>

- Python: ![version](https://img.shields.io/badge/version->==3.10.4-blue)
- pip
- keyboard module: ![version](https://img.shields.io/badge/version-==0.13.5-blue)
- PyAutoGUI module: ![version](https://img.shields.io/badge/version-==0.9.53-brightgreen)
- pynput module: ![version](https://img.shields.io/badge/version-==1.7.6-orange)

<h2>Instalación de Python</h2>

<h3>Windows</h3>

   [Descarga desde la página oficial.](https://www.python.org/)
   
<h3>Linux</h3>

    sudo apt-get install python3

<h3>Verificar que se tiene pip instalado en command prompt (cmd) en Windows o en la terminal de Linux</h3>

<p>Para acceder al cmd, basta con presionar "windows + R" y escribir "cmd", o presionar Ctrl + Shift + T para abrir la terminal en Linux.</p>
<p>Luego escribir el siguiente comando:</p>

    pip --version
    
Debería mostrar un mensaje de este estilo: pip 22.2.2 from (directorio) (python 3.10)

<h3>Instalando dependencias</h3>

<p>Ejecutar el siguiente comando dentro de la carpeta donde se encuentra el archivo main.py</p>

    pip install -r requirements.txt
    
 <p>Automáticamente comenzará a instalar las dependencias del proyecto, y estará listo para su uso.</p>
 
## Guía de usuario
---
<h3>Ejecución</h3>

<p>Solamente ejecutar el archivo main.py mediante doble click o por el siguiente comando (tanto en cmd como en terminal):</p>

    python3 main.py

<p>El programa automaticamente comenzará a escanear la pantalla, intentando encontrar los botones deseados.</p>
<p><b>Importante: la terminal debe abrirse en el directorio del proyecto, de lo contrario no funcionará o ejecutará otro script con el mismo nombre en caso de haberlo.</b></p>

<h3>Datos del usuario para la pantalla de login</h3>

<p>Dentro de la carpeta config, se encontrará un archivo llamado: "config.json", el cual se puede abrir con cualquier editor de texto, el cual tendrá el siguiente formato:</p>

```yaml
{
 	"user_data":
   {
      "username": "pepito",
      "password": "mypassword"
   }
}
```

<p>Solamente se debe reemplazar la información que está dentro de las comillas sin remover las mismas, de lo contrario el archivo no podrá ser leído correctamente.</p>

## Cómo probarlo
---

<p>Para probar el bot para lo que fue programado, se puede utilizar como recurso el siguiente repositorio:</p>

[Autoclicker_test](https://github.com/Foalz/autoclicker_test)

<p>Abrir el archivo index.html y ejecutar el archivo main.py</p>

<p>También, se pueden reemplazar las imagenes contenidas en la carpeta assets y probar manualmente, pero <b>NO es recomendada esta opción</b>, ya que el código se ejecuta cada 0.1 segundos, y apenas el programa detecte la imagen, moverá el cursor hacia ella inmediatamente.</p>

## Mis redes
---

- Página web: https://www.foalz.dev
- Correo electrónico: pedrocontreras@foalz.dev
- LinkedIn: https://www.linkedin.com/in/pedro-contreras-ba707121b/
- Instagram: https://www.instagram.com/foalzdev/
