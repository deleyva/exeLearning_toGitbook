# 3. Instalación de PiNet

_**\*\(NOTA DEL AUTOR\): Recomiendo realizar todo el módulo sin entrar como root en nuestro servidor Ubuntu, ya que podríamos tener problemas con los permisos de las carpetas que crea PiNet al iniciar.**_

Una vez que tenemos un equipo con Ubuntu 16.04 o posterior podemos pasar  a instalar PiNet, el programa que actuará como servidor de nuestra aula de Informática de Pi´s.

Su instalación resulta bastante sencilla;

\*/ Comenzaremos por abrir nuestra terminal bien mediante el cuadro de buscar que aparece al pulsar en el botón de menú de Ubuntu o bien mediante el acceso directo a programas favoritos que aparecerá a la izquierda.

![](/assets/as.png) ![](/assets/zx.png)

Una vez abierto escribiremos el siguiente comando \(respetemos guiones y barras\):

**wget --content-disposition **[http://bit.ly/pinetbeta](http://bit.ly/pinetbeta)

![](/assets/vc.png)

Nos descargará el instalador en nuestro equipo

![](/assets/bv.png)

Deberemos ahora "arrancarlo", mediante el comando

**sudo bash pinet**

y comenzará la Instalación

![](/assets/vf.png) Marcamos SI

![](/assets/kjh.png)     Marcamos No, ya que no tenemos usuarios creados con anterioridad, si queremos reinstalar PiNet podremos recuperar nuestro servidor \(o incluso instalarlo en otro equipo pero con los mismos datos\).

En la siguiente ventana nos preguntará que tipo de "Canales" queremos utilizar, marcaremos la opción "Stable"

![](/assets/lo.png)

Nos pregunta después si queremos instalar algún software adicional, para este curso lo dejaremos en blanco para posteriormente mostrar como podemos instalar nuevos programas en nuestras raspberry Pi desde el servidor PiNet.

![](/assets/435.png)

Lo dejamos en blanco y pasamos ahora a finalizar nuestra configuración de la instalación.

![](/assets/lo4.png)

Cabe destacar que la duración dependerá tanto de la velocidad de internet como del número de paquetes que vayamos a instalar, si utilizamos VirtualBox aconsejamos subir la capacidad de Memoria RAM de nuestra máquina para acelerar el proceso, ya que puede llegar a durar hasta 3-4 horas.

Ahora toca esperar mientras el sistema trabaja.

![](/assets/mj.png)     Imagen del proceso de instalación.

Una vez terminado, deberemos decidir si queremos que nuestros alumnos tengan acceso como root \(sudo\) o no. Ambas opciones tienen sus ventajas y desventajas y en cualquier caso podremos cambiarlas desde el menú de usuarios una vez que el sistema este instalado tanto en Ubuntu como en las Rasbperry Pi. En principio y salvo que queramos enseñar a manejar sistemas GNU/Linux, recomendamos impedir a los alumnos usar esta opción,  por lo menos hasta que nuestro control del servidor sea suficientemente alto como para "deshacer" cambios indeseados.

![](/assets/sudo.png)

\*/ Si sólo tenemos una red en nuestro servidor, dejaremos la siguiente opción como sale por defecto. En caso de que vayamos a crear una red única de Aula con el servidor actuando como tal y los equipos de los alumnos como “terminales tontos”, entonces deberemos elegir en el siguiente menú la red que vayan a usar nuestros alumnos. En nuestro caso, lo dejamos como sale \(en Sí\) La configuración podrá cambiarse más adelante.

![](/assets/ip.png)

Configurada esta parte, pasaremos a ver un mensaje como el siguiente, nos acostumbraremos a ello, ya que aparecerá cada vez que cambiemos algo en PiNet.

![](/assets/creación iso.png)

Aceptamos los dos siguientes mensajes sobre Información Adicional.

Y por último dejamos en blanco las preguntas que aparecen al final de la instalación.

![](/assets/v.png)

Al aceptar nos arranca directamente el programa, aunque recomendamos quitarlo para pasar al módulo siguiente y configurar las SD para las Raspberry Pi.

![](/assets/e.png)

\*/ TODAS LAS IMÁGENES UTILIZADAS EN EL PRESENTE MÓDULO HAN SIDO ELABORADAS POR EL AUTOR DEL CURSO.

### Posibles problemas durante la instalación, por Ricardo Fuster Andújar

> Varios compañeros, entre los cuales me encuentro, reportamos hace días en el foro un problema que surgía a la hora de instalar PiNet en la Raspberry Pi, consistente en que, una vez instalado PiNet en Ubuntu y pasados los ficheros de la carpera Piboot a la SD card, se producía el siguiente fallo: 
>
> **/bin/sh: can't access tty; job control turned off \(intransfer\)**
>
> En la sección de "Dudas" del foro hay una entrada que incluye una captura de pantalla. Tras indagar todo el día de ayer en internet he conseguido solucionar el problema, al menos el que me afectaba a mi, por que según he podido leer el comando /bin/sh: can't access tty; job control turned off \(intransfer\) no se refiere a un único problema, sino que alude a varios. Por lo tanto, es posible que la solución que aquí expongo no sirva para todos aquellos afectados por esta situación.  
>   
> En mi caso, el problema estaba en la dirección IP establecida en el archivo cmdline.txt. Este archivo se genera durante la instalación de Pinet, queda alojado en la carpeta Piboot y es uno de los que debemos copiar en la SD card para iniciar Pinet en la raspberry. Una vez copiados todos los archivo de Piboot en la tarjeta SD, abrimos cmdline.txt con el editor de texto \(abrimos el archivo que hemos copiado en la SD, no el que está en la carpeta Piboot de Ubuntu\). Veremos lo siguiente:  
>   
> **dwc\_otg.lpm\_enable=0 console=serial0,115200 kgdboc=serial0,115200 console=tty1 init=/sbin/init-ltsp nbdroot=:/opt/ltsp/armhf root=/dev/nbd0 elevator=deadline rootwait**  
>   
> Después de nbdroot= debería aparecer nuestra dirección IP. Lo que debemos hacer es modificar el fichero manualmente introduciendo nuestra IP. Repito, la modificación debemos realizarla en el archivo cmdline.txt copiado en la SD card \(de hecho, el alojado en Piboot es un archivo solo de lectura y no permite introducir cambios\). Quedará así:  
>   
> **dwc\_otg.lpm\_enable=0 console=serial0,115200 kgdboc=serial0,115200 console=tty1 init=/sbin/init-ltsp nbdroot=192.168.1.137:/opt/ltsp/armhf root=/dev/nbd0 elevator=deadline rootwait**  
>   
> Por supuesto, la dirección IP que aparece aquí es la mía, de manera que debeís saber cual es la vuestra e introducirla. En ubuntu basta con abrir el terminal y teclear ifconfig. Después introduces la SD card en la raspberry y la enciendes. Si vuestro problema es el mismo debería resolverse. Espero que esta explicación os sirva de ayuda y podáis solucionar el problema.

  






