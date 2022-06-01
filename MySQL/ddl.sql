#Conteúdo Curso em Vídeo MySql
#by geanclm in 05/2022

CREATE DATABASE cadastro; #Criar novo banco de dados
#DEFAULT CHARACTER SET utf8
#DEFAULT COLLATE utf8_general_ci;

CREATE TABLE pessoas (
id int not null auto_increment,
nome varchar(30) not null,
nascimento date,
sexo enum('M','F'),
peso float (5,2),
altura float (3,2),
nacionalidade varchar(20) DEFAULT 'Brasil',
primary key (id)
) DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS cursos (
nome varchar(30) NOT NULL UNIQUE,
descricao text,
carga int unsigned,
totaulas int unsigned,
ano year default '2022'
) DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS amigos (
id int NOT NULL auto_increment,
nome varchar(30) NOT NULL UNIQUE,
tel varchar(11),
primary key (id)
) DEFAULT CHARSET = utf8;


CREATE TABLE IF NOT EXISTS gafanhoto_assiste_curso (
id int NOT NULL auto_increment, 
data_ date,
idgafanhoto int,
idcurso int,
foreign key (idgafanhoto) references gafanhotos (id),
foreign key (idcurso) references cursos (idcurso),
primary key (id)
) DEFAULT CHARSET = utf8;


ALTER TABLE pessoas add column profissao varchar(10) after nome;
ALTER TABLE pessoas drop column profissao;
ALTER TABLE clientes drop column prof;
ALTER TABLE pessoas add codigo int first;
ALTER TABLE clientes drop column codigo;
ALTER TABLE pessoas modify column profissao varchar(20) not null default '';
ALTER TABLE pessoas change column profissao prof varchar(20);
ALTER TABLE pessoas rename to clientes;

ALTER TABLE cursos add idcurso int first;
ALTER TABLE cursos add primary key (idcurso);

DROP table if exists cursos;
DROP table if exists amigos;
DROP DATABASE cadastro; #apaga todo o banco de dados | MUITA atenção com eessa linha de comando!


ALTER TABLE gafanhotos add column idcurso int;
ALTER TABLE gafanhotos add foreign key (idcurso) references cursos (idcurso);