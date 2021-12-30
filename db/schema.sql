BEGIN TRANSACTION;
DROP TABLE IF EXISTS "elements_metadata";
CREATE TABLE IF NOT EXISTS "elements_metadata" (
	"element_metadata_id"	INTEGER NOT NULL,
	"name"	TEXT,
	"description"	INTEGER,
	"URI"	TEXT,
	PRIMARY KEY("element_metadata_id")
);
DROP TABLE IF EXISTS "document_type";
CREATE TABLE IF NOT EXISTS "document_type" (
	"document_type_id"	INTEGER NOT NULL,
	"name"	TEXT,
	"description"	TEXT,
	PRIMARY KEY("document_type_id")
);
DROP TABLE IF EXISTS "users";
CREATE TABLE IF NOT EXISTS "users" (
	"user_id"	INTEGER NOT NULL,
	"username"	TEXT NOT NULL,
	"name"	TEXT,
	"password"	TEXT,
	"role"	TEXT,
	PRIMARY KEY("user_id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "elements_metadata_text";
CREATE TABLE IF NOT EXISTS "elements_metadata_text" (
	"element_metadata_text_id"	INTEGER NOT NULL,
	"element_id"	INTEGER NOT NULL,
	"element_metadata"	INTEGER NOT NULL,
	"text"	TEXT,
	PRIMARY KEY("element_metadata_text_id"),
	FOREIGN KEY("element_metadata") REFERENCES "elements_metadata"("element_metadata_id"),
	FOREIGN KEY("element_id") REFERENCES "elements"("element_id")
);
DROP TABLE IF EXISTS "images";
CREATE TABLE IF NOT EXISTS "images" (
	"images_id"	INTEGER NOT NULL,
	"element_id"	INTEGER,
	"orden"	INTEGER,
	"size"	INTEGER,
	"mime_type"	TEXT,
	"filename"	TEXT,
	"path"	TEXT,
	"img_ts"	TEXT,
	"img_modified_ts"	TEXT,
	"img_metadata"	TEXT,
	PRIMARY KEY("images_id" AUTOINCREMENT),
	FOREIGN KEY("element_id") REFERENCES "elements"("element_id")
);
DROP TABLE IF EXISTS "elements";
CREATE TABLE IF NOT EXISTS "elements" (
	"element_id"	INTEGER NOT NULL,
	"document_type"	INTEGER NOT NULL,
	"user_id"	INTEGER,
	"public"	INTEGER,
	"created_ts"	TEXT,
	"modified_ts"	TEXT,
	FOREIGN KEY("user_id") REFERENCES "users"("user_id"),
	FOREIGN KEY("document_type") REFERENCES "document_type"("document_type_id"),
	PRIMARY KEY("element_id")
);
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (1,'título','un nombre dado al recurso','http://purl.org/dc/terms/title');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (2,'descripción','resumen, índice, representación gráfica, o cualquier texto que de cuenta del recurso

','http://purl.org/dc/terms/description');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (3,'creador','autor, creador o entidad responsable por la hechura del recurso. Un creador puede ser una persona, una organización o un servicio.','http://purl.org/dc/terms/creator');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (4,'fecha','un periodo de tiempo asociado con un evento en la vida del recurso (creación, actualización, finalización)','http://purl.org/dc/terms/date');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (5,'espacio','Ubicación, región o cualquier otra referencia espacial asociada al recurso','http://purl.org/dc/terms/spatial');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (6,'idioma','lenguaje o lenguajes del recurso','http://purl.org/dc/elements/1.1/language');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (7,'folios','folios (hojas) en total del recurso',NULL);
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (8,'páginas','páginas del libro',NULL);
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (9,'identificadores','una referencia precisa del recurso en un contexto determinado (p. ej: catálogo bibliográfico)

','http://purl.org/dc/terms/identifier');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (10,'descripción_física','corta descripción de las características físicas del objeto','http://purl.org/dc/terms/format');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (11,'tipo_imagen','MIME type de la imagen (image/jpg, image/png, image/tiff, image/x-adobe-dng)',NULL);
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (12,'volumen','volumen dentro de un conjunto de libros que compone la obra',NULL);
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (13,'ejemplar','número que corresponde a una publicación seriada. Puede ser único o parte de un volumen',NULL);
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (14,'isbn','','http://purl.org/dc/terms/bibliographicCitation');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (15,'issn',NULL,'http://purl.org/dc/terms/bibliographicCitation');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (16,'serie',NULL,'http://purl.org/dc/terms/bibliographicCitation');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (17,'edición',NULL,'http://purl.org/dc/terms/bibliographicCitation');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (18,'editorial','editorial responsable del recurso','http://purl.org/dc/terms/publisher');
INSERT INTO "elements_metadata" ("element_metadata_id","name","description","URI") VALUES (19,'fecha_final',NULL,NULL);
INSERT INTO "document_type" ("document_type_id","name","description") VALUES (1,'legajo','conjunto de documentos en un expediente');
INSERT INTO "document_type" ("document_type_id","name","description") VALUES (2,'documento','unidad documental simple compuesta de uno o varios folios');
INSERT INTO "document_type" ("document_type_id","name","description") VALUES (3,'imagen','dibujo o impreso con una representación gráfica, se incluyen dibujos, mapas, banderas, escudos, entre otros');
INSERT INTO "document_type" ("document_type_id","name","description") VALUES (4,'seriada','periódico o revista');
INSERT INTO "document_type" ("document_type_id","name","description") VALUES (5,'libro','impresos o manuscritos empastados');
COMMIT;
