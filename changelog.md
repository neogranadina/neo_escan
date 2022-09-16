# Neoscan

## [Unreleased]

## [0.1.711] - 2022-09-15

### Bugfixes

- Error en la orientación de las imágenes
- Correción del contador de imágenes en la patalla de Escaner
- Habilitación del comportamiento que oculta el botón de captura mientras se está capturando la imagen.
- Corregido un *bug* que hacía que después de una cantidad considerable de imágenes se incrementara el uso de la memoria RAM. Se corrigió modificando el comportamiento de *bagit* para que no se actualice el manifiesto con cada captura sino al cerrar el proyecto.
- Corrección de la orientación de las imágenes (se mostraban invertidas).
- Hallado error de sobreescritura. Se debía a un error no identificado por errores al guardar el archivo JSON que impedía identificar la siguiente imagen. Se creó un script para arreglar el archivo y poder continuar.

## [0.1.710] - 2022-07-26

### Bugfixes

Arreglado un bug que no permitía mostrar los mensajes de sincronización de archivos con B2.

## [0.1.700] - 2022-07-22

Esta versión se dedica a la creación de un sistema para el envío de archivos desde el equipo local hacia un bucket en B2.

### Added

- Se incluyó la capacidad para enviar las imágenes desde el archivo local a B2.
- Agregado un formulario para configurar la aplicación remota de B2.
- Se creó una página para el envío de las imágenes con un solo botón.

### Changed

- Se elimina el archivo .sh para iniciar la aplicación y se creó un archivo .desktop para que se pueda iniciar la aplicación desde el menú de inicio.
- Modificaciones en la ubicación de los archivos de configuración.

## [0.1.600] - 2022-04-13

Esta versión incluye una pantalla de configuración general para los escáners.

Además, hace ajustes para responder a los issues indicados en <https://github.com/neogranadina/neo_escan/issues/8> y otros que surgieron de las pruebas.

### Added

- Se creó una pantalla de configuración general para los escáners, de tal manera que se pueda probar la configuración más adecuada relacionada con el zoom, la velocidad de obturación y la orientación de las cámaras.

### Fixed

- El botón borrar funciona correctamente.
- Los thumbnails y la cantidad de imágenes se muestran correctamente.
- En la página de captura se muestran correctamente la cantidad de imágenes capturadas.
- Corregidos dos errores de claves que impedían crear libros y seriadas.
- El botón de retomar funciona correctamente.

## [0.1.5024] - 2022-04-11

Esta versión permite ajustar la velocidad de obturación para controlar la exposición de las fotos.

### Added

- Botón para ajustar la velocidad de obturación.

### Changed

- Configuración de zoom, dng y shutter en la carpeta de cada proyecto (`config_project.json`).
- Cambia el archivo config.cfg en consecuencia.
- Las previsualizaciones de las imágenes tomadas se escalan y mantienen la relación de aspecto.

## [0.1.502] - 2022-04-03

Esta versión atiende algunos cambios indicados en <https://github.com/neogranadina/neo_escan/issues/8>

### Fixed

- Ajuste del color del botón enviar.

### Changed

- El nombre de los directorios de los archivos corresponden al identificador (antes id).
- El título y el identificador de los metadatos se convierten en los valores requeridos de cada formulario.

## [0.1.5011] - 2022-03-27

Esta versión corrige el zoom de la cámara que no respondía en las versiones anteriores.

### Added

- Dial button y text box para la configuración del zoom en la pantalla de formularios.

### Changed

- El checkbox para selecionar si se quería guardar en dng se cambió a la pantalla de formularios (metadata)
- Las fotografías no se borran al validar la fotografía.
- Se cambió el botón "validar" por "continuar" en la pantalla de escáner.
- Captura de la imagen con pedal o `B`.

## [0.1.500] - 2022-03-21

Esta versión corrige un error mayor que hacía de los botones del inicio enviaran al id equivocado.

### Fixed

- Corregido el error de los botones de inicio enviando al id equivocado.

## [0.1.430] - 2022-03-20

Esta versión pretende darle estabilidad al escáner, manejar con mejor gentileza la conexión a las cámaras
para evitar que se rompa y se pierda la conexión. Asimismo, reducir las advertencias que restringían
el uso de la aplicación sin las cámaras conectadas.

### Added

- En caso de que se reestablezca la base de datos, se hace un backup de las imágenes en el directorio IMGDIR/old_backup
- Checkbox con opción para guardar en DNG en pantalla de escáner
- Barra de espacio realiza captura y valida la imagen
- Archivos de imagen se guardan en el estandar BagIt <https://datatracker.ietf.org/doc/html/rfc8493>
- Método para asignar posición derecha o izquierda de una cámara basado en su serie (ver config.cfg).
- Logs más detallados y en más procesos
- Asegurada compatibilidad con CHDK 1.5

### Changed

- Captura en DNG de predeterminada a opcional
- Nombre de las imágenes nombrada automáticamente, par e impar dependiendo si la cámara es derecha o izquierda
- eliminada la exigencia de doble cámara

### Fixed

- Correción de un while loop que bloqueaba la aplicación si no se tomaban correctamente las fotos.
- Fixed corrección de sobreexposición

### Removed

- Requisito de captura manual de folios en la pantalla de escáner.
