# Neoscan

## [Unreleased]

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
