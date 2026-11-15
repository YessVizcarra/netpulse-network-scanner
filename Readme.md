# NetPulse

Escáner e inventario de red en Python para mi laboratorio.

¿Para qué sirve en la vida real?
- Descubrimiento/reconocimiento: No se requieren saber las IPs antes, solo se requiere conocer la red y el script prueba todas, una por una y solo te responde las que esten vivas.

¿Porqué no se utilizó un mensaje de difusión?
- Por seguridad, casi todos los sistemas operativos modernos ignoran el ping broadcast por defecto.
- Con broadcast, solo ves los que sí contestaron. No tienes control por host.
- No cruza routers, el unicast si puede ir a otra red sí hay ruta.

## Uso legal

Solo en mi laboratorio: mis máquinas virtuales Kali y Ubuntu. Nunca contra sistemas o redes de terceros.

## Uso

python netpulse.py --network 192.168.56.0/24
