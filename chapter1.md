# Un poco de Historia:

En 2011se desarrolló la Raspberry Pi como ordenador de bajo coste para facilitar la enseñanza de la informática en los colegios, pero hasta 2012 no comenzó a fabricarse. La fundación recibe apoyos del laboratorio de informática de la Universidad de Cambridge y de Broadcom.

Ahora los jóvenes tienen contacto con la informática pero, aunque parezca paradójico, es muy raro que realmente se facilite el desarrollo de aplicaciones o de programas como en los primeros ordenadores personales, especialmente a los más pequeños. Los ordenadores que tenemos están orientados a tareas informáticas o de ocio, pero no vienen preparados con conexiones que posibiliten **“pequeños proyectos de hardware”** o con herramientas para aprender a programar o un lenguaje de programación. Este es el nicho que cubre \(perfectamente\) la Raspberry Pi.

Como vemos no hay ningún secreto en su precio, ya que fuediseñada con el fin de ser lo más barato posible y llegar al máximo número de usuarios. Desde este año es posible comprar las Raspberry Pi, aunque la fabricación se hace por lotes y a veces hay que esperar varios meses para que haya unidades disponibles dada su altísima demanda.

 Son varios los modelos que han aparecido hasta ahora y sin entrar en mucho detalle de cada uno de ellos, mostramos a continuación una tabla resumen con las características de cada uno de ellos.

**TABLA COMPARATIVA DE LAS DIFERENTES VERSIONES DE RASPBERRY \***

|  |  | **Raspberry Pi 1 Modelo A** | **Raspberry Pi 1 Modelo B** | **Raspberry Pi 1 Modelo B+** | **Raspberry Pi 2 Modelo B** | **Raspberry Pi 3 Modelo B** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | [SoC](https://es.wikipedia.org/wiki/System_on_a_chip)\(Chip\) | [Broadcom](https://es.wikipedia.org/wiki/Broadcom)BCM2835 \([CPU](https://es.wikipedia.org/wiki/CPU)+[GPU](https://es.wikipedia.org/wiki/GPU)+[DSP](https://es.wikipedia.org/wiki/Procesamiento_digital_de_se%C3%B1ales)+[SDRAM](https://es.wikipedia.org/wiki/SDRAM)+ puerto[USB](https://es.wikipedia.org/wiki/USB)\)[3](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-Broadcom-BCM2835-Website-3) | Broadcom BCM2836 \(CPU + GPU + DSP + SDRAM + Puerto USB\) | Broadcom BCM2837 \(CPU + GPU + DSP + SDRAM + Puerto USB |
|  |  |  | CPU: | [ARM](https://es.wikipedia.org/wiki/Arquitectura_ARM)1176JZF-S a 700MHz \(familia ARM11\)[3](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-Broadcom-BCM2835-Website-3) | 900 MHz quad-core ARM Cortex A7 | 1.2GHz 64-bit quad-core ARMv8 |
|  |  |  |  |  | Juego de instrucciones: | RISC de 32 bits |
|  |  |  |  |  | GPU \(Gráfica\) | Broadcom[VideoCore](https://es.wikipedia.org/w/index.php?title=VideoCore&action=edit&redlink=1)IV,,[61](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-hq-qa-61)OpenGL ES 2.0, MPEG-2 y VC-1 \(con licencia\),[59](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-rpi-codec-59)1080p30[H.264/MPEG-4 AVC](https://es.wikipedia.org/wiki/H.264/MPEG-4_AVC)[3](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-Broadcom-BCM2835-Website-3) |
|  |  |  | Memoria \(SDRAM\): | 256[MiB](https://es.wikipedia.org/wiki/MiB)\(compartidos con la GPU\) | 512 MiB \(compartidos con la GPU\)[4](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-512MB-4)desde el 15 de octubre de 2012 | 1[GB](https://es.wikipedia.org/wiki/Gigabyte)\(compartidos con la GPU\) |
|  |  |  | Puertos[USB](https://es.wikipedia.org/wiki/USB)2.0: | 1 | 2 \(vía[hub USB](https://es.wikipedia.org/wiki/Hub_USB)integrado\)[54](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-SMSC-LAN9512-Website-54) | 4 |
|  |  |  |  |  | Entradas de vídeo: | Conector[MIPI](https://es.wikipedia.org/w/index.php?title=MIPI&action=edit&redlink=1)[CSI](https://es.wikipedia.org/w/index.php?title=CSI_(interfaz)&action=edit&redlink=1)que permite instalar un módulo de cámara desarrollado por la RPF |
|  |  |  |  |  | Salidas de vídeo: | [Conector RCA](https://es.wikipedia.org/wiki/Conector_RCA)\(PAL y NTSC\),[HDMI](https://es.wikipedia.org/wiki/HDMI)\(rev1.3 y 1.4\),[63](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-quickguide-63)Interfaz[DSI](https://es.wikipedia.org/w/index.php?title=DSI_(interfaz)&action=edit&redlink=1)para panel LCD[64](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-DSI-64)[65](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-65) |
|  |  |  |  |  | Salidas de audio: | [Conector](https://es.wikipedia.org/wiki/Jack_(conector))de 3.5 mm, HDMI |
|  |  |  |  | Almacenamiento integrado: | [SD](https://es.wikipedia.org/wiki/Tarjeta_SD)/[MMC](https://es.wikipedia.org/wiki/MultiMediaCard)/ ranura para[SDIO](https://es.wikipedia.org/wiki/SDIO) | [MicroSD](https://es.wikipedia.org/wiki/Tarjeta_MicroSD) |
|  |  |  | Conectividad de red:[5](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-faq-5) | Ninguna | 10/100[Ethernet](https://es.wikipedia.org/wiki/Ethernet)\([RJ-45](https://es.wikipedia.org/wiki/RJ-45)\) via hub USB[54](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-SMSC-LAN9512-Website-54) | 10/100[Ethernet](https://es.wikipedia.org/wiki/Ethernet)\([RJ-45](https://es.wikipedia.org/wiki/RJ-45)\) vía hub USB[66](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-SMSC-LAN9514-Website-66), Wifi 802.11n, Bluetooth 4.1 |
|  |  |  |  | Periféricos de bajo nivel: | 8x[GPIO](https://es.wikipedia.org/wiki/GPIO),[SPI](https://es.wikipedia.org/wiki/Serial_Peripheral_Interface),[I²C](https://es.wikipedia.org/wiki/I%C2%B2C),[UART](https://es.wikipedia.org/wiki/Universal_Asynchronous_Receiver-Transmitter)[61](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-hq-qa-61) | 17 x GPIO y un bus HAT ID |
|  |  | Consumo energético: | 500mA, \(2.5[W](https://es.wikipedia.org/wiki/Vatio)\)[5](https://es.wikipedia.org/wiki/Raspberry_Pi#cite_note-faq-5) | 700mA, \(3.5 W\) | 600 mA, \(3.0 W\) | 800 mA, \(4.0 W\) |
|  |  |  |  |  | Fuente de alimentación: | 5V vía[Micro USB](https://es.wikipedia.org/wiki/Micro_USB)o GPIO header |
|  |  |  |  |  | Dimensiones: | 85.60mm × 53.98mm |
|  |  |  |  |  |  |  |

**\* \(Tabla modificada de**[**https://es.wikipedia.org/wiki/Raspberry\_Pi**](https://es.wikipedia.org/wiki/Raspberry_Pi)**\)**



# Dando los primeros pasos: 

Al igual que no necesitamos ser ingenieros de telecomunicaciones para usar un móvil, tampoco hace falta ser informáticos para sacarle mucho partido a nuestro aula de informática. Además si podemos "montar" la clase con nuestros alumnos, conseguiremos que se formen tanto en Hardware como en Software

