# MODULO III: Instalación de PiNet

_**\*\(NOTA DEL AUTOR\): Recomiendo realizar todo el módulo sin entrar como root en nuestro servidor Ubuntu, ya que podríamos tener problemas con los permisos de las carpetas que crea PiNet al iniciar.**_

Una vez que tenemos un equipo con Ubuntu 16.04 o posterior podemos pasar  a instalar PiNet, el programa que actuará como servidor de nuestra aula de Informática de Pi´s.

Su instalación resulta bastante sencilla;

\*/ Comenzaremos por abrir nuestra terminal bien mediante el cuadro de buscar que aparece al pulsar en el botón de menú de Ubuntu o bien mediante el acceso directo a programas favoritos que aparecerá a la izquierda.

![](/assets/as) ![](/assets/zx)

Una vez abierto escribiremos el siguiente comando \(respetemos guiones y barras\):

**wget --content-disposition **[http://bit.ly/pinetbeta](http://bit.ly/pinetbeta)

![](/assets/vc)

Nos descargará el instalador en nuestro equipo

![](/assets/bv)

Deberemos ahora "arrancarlo", mediante el comando

**sudo bash pinet**

y comenzará la Instalación

![](/assets/vf) Marcamos SI

![](/assets/kjh)            Marcamos No, ya que no tenemos usuarios creados con anterioridad, si queremos reinstalar PiNet podremos recuperar nuestro servidor \(o incluso instalarlo en otro equipo pero con los mismos datos\).

En la siguiente ventana nos preguntará que tipo de "Canales" queremos utilizar, marcaremos la opción "Stable"

![](/assets/lo)

Nos pregunta después si queremos instalar algún software adicional, para este curso lo dejaremos en blanco para posteriormente mostrar como podemos instalar nuevos programas en nuestras raspberry Pi desde el servidor PiNet.

![](/assets/435)

Lo dejamos en blanco y pasamos ahora a finalizar nuestra configuración de la instalación.

![](/assets/lo4)

Cabe destacar que la duración dependerá tanto de la velocidad de internet como del número de paquetes que vayamos a instalar, si utilizamos VirtualBox aconsejamos subir la capacidad de Memoria RAM de nuestra máquina para acelerar el proceso, ya que puede llegar a durar hasta 3-4 horas.

Ahora toca esperar mientras el sistema trabaja.

![](/assets/mj)     Imagen del proceso de instalación.

Una vez terminado, deberemos decidir si queremos que nuestros alumnos tengan acceso como root \(sudo\) o no. Ambas opciones tienen sus ventajas y desventajas y en cualquier caso podremos cambiarlas desde el menú de usuarios una vez que el sistema este instalado tanto en Ubuntu como en las Rasbperry Pi. En principio y salvo que queramos enseñar a manejar sistemas GNU/Linux, recomendamos impedir a los alumnos usar esta opción,  por lo menos hasta que nuestro control del servidor sea suficientemente alto como para "deshacer" cambios indeseados.

![](/assets/sudo)

\*/ Si sólo tenemos una red en nuestro servidor, dejaremos la siguiente opción como sale por defecto. En caso de que vayamos a crear una red única de Aula con el servidor actuando como tal y los equipos de los alumnos como “terminales tontos”, entonces deberemos elegir en el siguiente menú la red que vayan a usar nuestros alumnos. En nuestro caso, lo dejamos como sale \(en Sí\) La configuración podrá cambiarse más adelante.

![](/assets/ip)

Configurada esta parte, pasaremos a ver un mensaje como el siguiente, nos acostumbraremos a ello, ya que aparecerá cada vez que cambiemos algo en PiNet.

![](/assets/creación iso)

Aceptamos los dos siguientes mensajes sobre Información Adicional.

Y por último dejamos en blanco las preguntas que aparecen al final de la instalación.

![](/assets/v)

Al aceptar nos arranca directamente el programa, aunque recomendamos quitarlo para pasar al módulo siguiente y configurar las SD para las Raspberry Pi.

![](/assets/e)

\*/ TODAS LAS IMÁGENES UTILIZADAS EN EL PRESENTE MÓDULO HAN SIDO ELABORADAS POR EL AUTOR DEL CURSO.

