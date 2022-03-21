# Neoscan

## [Unreleased]

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

### Deprecated

- Botón validación.
