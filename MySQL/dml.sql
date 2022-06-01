#Conteúdo Curso em Vídeo MySql
#by geanclm in 05/2022

show databases;

use cadastro;

show status;

show tables;
describe clientes;
desc clientes;
describe cursos;

INSERT INTO pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES
(default, 'Creuza', '1920-12-30', 'F', '50.2', '1.65', default);

INSERT INTO pessoas VALUES
(default, 'Adalgiza', '1930-11-2', 'F', '63.2', '1.75', 'Irlanda');

INSERT INTO pessoas VALUES
(default, 'Ana', '1975-11-22', 'F', '52.3', '1.45', 'EUA'),
(default, 'Pedro', '2000-07-15', 'M', '52.3', '1.75', 'Brasil'),
(default, 'Maria', '1999-05-30', 'F', '75.9', '1.70', 'Portugal');

INSERT INTO cursos VALUES
('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
('2', 'Algorítmos', 'Lógica de programcação', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de Photoshop CC', '10', '8', '2014'),
('4', 'PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('5', 'Jarva', 'Introdução a Linguagem Java', '10', '29', '2000'),
('6', 'MySQL', 'Banco de dados MySQL', '30', '15', '2016'),
('7', 'Word', 'Curso completo de Word', '40', '30', '2016'),
('8', 'Sapateado', 'Danças Rítmicas', '40', '30', '2018'),
('9', 'Cozinha Àrabe', 'Aprenda a fazer Kibe', '40', '30', '2018'),
('10', 'YouTube', 'Gerar polêmica e ganhar inscritos', '5', '2', '2016');

INSERT INTO amigos VALUES
(default,'Adalgiza','F', '47996773032'),
(default,'José','M', '48996773033'),
(default,'Pedro','M', '83996773034'),
(default,'Ana','F', '61996773035');

INSERT INTO gafanhoto_assiste_curso VALUES
(default,'2014-03-01','1','2'),
(default,'2015-12-22','3','6'),
(default,'2014-01-01','22','12'),
(default,'2016-05-12','1','19');


UPDATE cursos set nome = 'HTML5' WHERE idcurso = 1;
UPDATE cursos set nome = 'PHP', ano = '2015' WHERE idcurso = 4;
UPDATE cursos set nome = 'Java', carga = '40', ano = '2015' WHERE idcurso = 5 LIMIT 1;
UPDATE cursos set carga = '0', ano = '2018' WHERE ano = '2018' LIMIT 1;
UPDATE cursos set carga = '40' WHERE idcurso = 8 LIMIT 8;

UPDATE gafanhotos set idcurso = 6 WHERE id = 1 LIMIT 1;

DELETE from cursos WHERE ano = '2018' LIMIT 3;
DELETE from cursos WHERE idcurso = 6 LIMIT 1;

TRUNCATE table cursos; # comando para apagar todas as linhas da tabela