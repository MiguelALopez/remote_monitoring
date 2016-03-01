DROP TABLE IF EXISTS os CASCADE;
CREATE TABLE os (
  id              SERIAL PRIMARY KEY,
  kernel          VARCHAR,
  release         VARCHAR,
  nodename        VARCHAR,
  kernelversion   VARCHAR,
  machine         VARCHAR,
  processor       VARCHAR,
  operatingsystem VARCHAR,
  hardware        VARCHAR,
  fecha           TIMESTAMP
);

DROP TABLE IF EXISTS who CASCADE;
CREATE TABLE who (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR,
  fecha  TIMESTAMP
);

DROP TABLE IF EXISTS cpu CASCADE;
CREATE TABLE cpu (
  id      SERIAL PRIMARY KEY,
  usuario VARCHAR,
  sistema VARCHAR,
  idle    VARCHAR,
  waiting VARCHAR,
  stolen  VARCHAR,
  fecha   TIMESTAMP
);

DROP TABLE IF EXISTS mem CASCADE;
CREATE TABLE mem (
  id    SERIAL PRIMARY KEY,
  swpd  VARCHAR,
  free  VARCHAR,
  buff  VARCHAR,
  cache VARCHAR,
  fecha TIMESTAMP
);

DROP TABLE IF EXISTS swap CASCADE;
CREATE TABLE swap (
  id    SERIAL PRIMARY KEY,
  si    VARCHAR,
  so    VARCHAR,
  fecha TIMESTAMP
);

DROP TABLE IF EXISTS torrent CASCADE;
CREATE TABLE torrent (
  id        INT PRIMARY KEY, -- identificador unico de cada torrent
  cod_hash  VARCHAR UNIQUE, -- hash que deriva cada torrent
  done      VARCHAR, -- porcentaje de la descarga
  have      VARCHAR, -- Numero de bytes descargados
  eta       VARCHAR, -- Estimate time to finish
  up        VARCHAR, -- Rate upload
  down      VARCHAR, -- Rate Download
  status    VARCHAR, -- Estado de la descarga
  name_torr VARCHAR, -- Nombre del torrent
  fecha     TIMESTAMP
);

DROP TABLE IF EXISTS cola_torrents CASCADE;
CREATE TABLE cola_torrents (
  id           SERIAL PRIMARY KEY,
  nombre       VARCHAR,
  magnet       VARCHAR,
  magnet_short VARCHAR,
  state        VARCHAR, -- Could be PENDIENTE, ESPERA_CONFIRMACION, CONFIRMADO
  fecha        TIMESTAMP
);