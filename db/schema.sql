CREATE TABLE IF NOT EXISTS folios_data (
	id_folio INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_numerico_folio NUMERIC,
	folio_rov TEXT,
	raw_img INTEGER NOT NULL,
	edited_img INTEGER,
	pic_asociada INTEGER NOT NULL,
	unidad_documental INTEGER NOT NULL,
	CONSTRAINT folios_data_FK FOREIGN KEY (pic_asociada) REFERENCES pics_data(id_pic) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT folios_data_FK_1 FOREIGN KEY (unidad_documental) REFERENCES unidad_documental(id_unidad_documental) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS instituciones (
	id_institucion INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_institucion TEXT NOT NULL,
	tipo_institucion TEXT
);

CREATE TABLE IF NOT EXISTS pics_data (
	id_pic INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	unidad_documental INTEGER NOT NULL,
	raw_file_path TEXT NOT NULL,
	mod_file_path TEXT,
	camara TEXT NOT NULL,
	filename TEXT NOT NULL,
	shutter_speed TEXT,
	valorISO TEXT,
	apertura TEXT,
	ts_toma TEXT
);

CREATE TABLE IF NOT EXISTS proyectos (
	id_proyecto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_proyecto TEXT NOT NULL,
	tipo_proyecto INTEGER NOT NULL,
	institucion_proyecto INTEGER,
	ts_creacion_proyecto TEXT NOT NULL,
	path_proyecto TEXT NOT NULL,
	cobertura_temporal TEXT,
	cobertura_espacial TEXT,
	CONSTRAINT proyectos_FK FOREIGN KEY (tipo_proyecto) REFERENCES tipos_proyecto(id_tipo_proyecto) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT proyectos_FK_1 FOREIGN KEY (institucion_proyecto) REFERENCES instituciones(id_institucion) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS tipos_proyecto (
	id_tipo_proyecto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_tipo_proyecto TEXT NOT NULL,
	descripcion_tipo_proyecto TEXT
);

CREATE TABLE IF NOT EXISTS unidad_documental (
	id_unidad_documental INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_proyecto INTEGER NOT NULL,
	codigo_referencia TEXT,
	titulo TEXT NOT NULL,
	fechas TEXT NOT NULL,
    CONSTRAINT unidad_documental_FK FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto)
);

CREATE TABLE IF NOT EXISTS usuarios (
	id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_usuario TEXT NOT NULL,
    password TEXT,
    rol TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS usuarios_proyectos (
	id_relacion_uyp INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_proyecto INTEGER NOT NULL,
	id_usuario INTEGER NOT NULL,
	CONSTRAINT usuarios_proyectos_FK FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto),
	CONSTRAINT usuarios_proyectos_FK_1 FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
