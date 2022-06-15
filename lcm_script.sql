CREATE DATABASE IF NOT EXISTS lcm_scritp;
USE lcm_scritp;

CREATE TABLE doctores(
    id       int(25) auto_increment not null,
    nombre    varchar(100),
    apellidos varchar(255),
    noConsultorio int(25),
    email     varchar(255) not null,
    password  varchar(255) not null,
    fecha     date not null,
    CONSTRAINT pk_doctores PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;


CREATE TABLE citas(
    id         int(25) auto_increment not null,
    doctor_id int(25) not null,
    paciente      varchar(255) not null,
    descripcion MEDIUMTEXT,
    horaAtencion varchar(255),
    costo        float(10,2),
    fecha       date not null,
    CONSTRAINT pk_citas PRIMARY KEY(id),
    CONSTRAINT fk_cita_doctor FOREIGN KEY(doctor_id) REFERENCES doctores(id)
)ENGINE=InnoDb;