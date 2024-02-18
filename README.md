# Mujeres en la musica

Esta app busca hacer un registro de las mujeres que se dedican o se han dedicado a la música en sus vidas. El objetivo es dar más realce al arte femenino a través de una base de datos que, como proyección, sea publicada y actualizada en la web.

En términos de programación está basada en el paradigma de programación orientada a objetos y sus archivos son:

## archivos

- vista: encargada de la interfaz gráfica del usuario.
- modelo: contiene la lógica necesaria para el funcionamiento básico
- controlador: controla el funcionamiento de la app
- clases_secundarias: clases que ayudan al funcionamiento general
- observador: se implementa el patrón observador
- servidor_cliente_sockets: implementa la lógica de lanzamiento del servidor y la conexión con el cliente
- servidor: servidor con protocolo TCP

En términos de la actualización de datos en el archivo log.txt. El observador se encarga de notificar los registros nuevos, el servidor avisa si hubo cambios en los registros ya existentes y el decorador dice qué cambios hubo exactamente siendo éstos la eliminación o actualización de registros.
