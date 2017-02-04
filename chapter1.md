# Dando los primeros pasos:

Al igual que no necesitamos ser ingenieros de telecomunicaciones para usar un móvil, tampoco hace falta ser informáticos para sacarle mucho partido a nuestro aula. Además, si podemos "montar" la clase con nuestros alumnos, conseguiremos que se formen tanto en Hardware como en Software.

# ¿Por dónde podemos empezar?;

Pues está claro, conociendo físicamente nuestra Raspberry, sus partes y componentes fundamentales y porqué no, los multiples periféricos que le podemos añadir.

# A.- HARDWARE:

### Componentes principales de Raspberry Pi 3\*:

![](/assets/componentes.jpg)

**\(\* Elaboración propia\)**

# Periféricos necesarios para crear una aula de Informática:

Pues en realidad no demasiados aunque la elección entre unos u otros, puede facilitarnos mucho la tarea, nuestra Raspberry Pi \(a partir de ahora solo nos referiremos al modelo 3\) ya incluye elementos básicos como la toma  de alimentación.

![](/assets/cargador.jpg)\*

Para comenzar y si no es el caso que compremos una raspberry pi con el kit de inicio \(algo altamente recomendable por precio y comodidad\), necesitaremos:

**\*/Carcasa protectora:** Nos ayudará a proteger nuestra Raspberry Pi del polvo y de otros elementos.

![](/assets/carcasa.jpg)\*

**\*/ Disipadores de calor:** Ayudan a nuestra Raspberry a no sobrecalentarse, se pegan muy fácilmente sobre los chipset de la placa.

![](/assets/disipadores.jpg)\*

**\*/ Tarjeta MicroSD: **La mayoría ya vienen con adaptador para ordenador de sobremesa o portatil, lo recomendable para este proyecto, sería una capacidad de al menos 16 GB pero sobre todo una velocidad de escritura de 10. Esto último podemos saberlo si localizamos en la misma tarjeta el siguiente símbolo ![](/assets/simbolo sd.jpg)\*

![](/assets/sd.jpg)\*

**\*/ Cable HDMI: **Para nuestro proyecto, no es necesario tener uno para cada Raspberry, aunque si en recomendable hacerse con unos cuantos.

**\(\*Todas las imágenes extraídas de la Web de Amazon: www.amazon.es\)**

**\*/ Teclado y ratón: **Aunque podrían servir cualquiera con entrada usb, si queremos que el aula sea funcional, estaría bien que se usase tecnología bluetooth. Si bien para una primera configuración es recomendable conectarlos mediante los USB, para evitar problemas de compatibilidad.

**\*/ Touch Screen LCD:** Si la economía de nuestro centro nos lo permite, una buena solución que compagina los dispositivos de entrada y que resultará tremendamente cómodo y atractivo para nuestros alumnos es sin duda la "Touch screen" propia de Raspberry Pi. Compagina teclado y ratón y aunque ocupará dos conexiones de nuestra placa, a largo plazo sale rentable. Su precio va desde los 33 € a los 110 €.

![](/assets/touch screen)\*

Si exceptuamos esta última, los demás componentes si serán necesarios para montar nuestra aula de informática. A modo de sugerencia, Os imaginais un aula que mediante Wifi tenga los siguientes elementos para nuestros alumnos....

**Touch screen mas caja \(20€\) + \(Raspberry Pi3 B + Disipadores + Tarjeta SD + Alimentador + HDMI \)\(75 €\) = - de 100€/alumno**

\(precio aproximado\).

Qué más necesitamos para comenzar.... Pues un equipo de sobremesa que actuará a modo de servidor en nuestra aula. No es necesario que sea muy potente, de hecho cualquiera de los que tenemos en nuestros centros que ya no sirven para las Aulas convencionales puede servir.

**\*/ Otros accesorios: La propia natulareza del proyecto Raspberry Pi, hace que el número de componentes que podemos añadir a nuestra placa no pare de crecer. Podemos encontrar alguna de los principales en los siguientes enlaces.**

[https://www.raspberryshop.es/accesorios-raspberry-pi.php](https://www.raspberryshop.es/accesorios-raspberry-pi.php)

[https://hipertextual.com/archivo/2014/05/accesorios-raspberry-pi/](https://hipertextual.com/archivo/2014/05/accesorios-raspberry-pi/)

[http://www.raspipc.es/public/home/](http://www.raspipc.es/public/home/)

Hasta cierto punto impresionante ¿no?; Podemos ver miles y miles de proyectos que se han realizado con este mini ordenador, desde consolas retro hasta robots programables. Pero centremonos en nuestro objetivo, pasemos ahora a explicar brevemente el software que necesitaremos.

# B.- SOFTWARE:

Recopilemos hasta ahora lo que Necesitamos...

**Hardware necesario**

– Un equipo de sobremesa / portátil de edad para el servidor con un puerto Gigabit Ethernet.  
– Un conmutador de red \(requiere al menos un solo gigabit o 1000 puerto / 100 / 10mbit para el servidor\).  
– Un router \(para una red independiente\) o la conexión a la red de escuelas.  
– Algunos cables Ethernet.  
– Una Frambuesa Pi y tarjeta SD con un tamaño de al menos 128 MB \(así que sí, 2gb, 4gb, 8gb, etc tarjetas serán también trabajar



Y ahora pasemos a Recopilar el software que vamos a necesitar, esta parte nos saldrá mucho más barata... de hecho es software gratuito y libre, por lo que solo tiene ventajas.



