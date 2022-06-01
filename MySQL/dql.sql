/*
Curso em Vídeo - MySQL
Structured Query Language (Linguagem de Consulta Estruturada) 
---
by geanclm in 05/2022
*/

select user, authentication_string, plugin, host from mysql.user;

select * from cursos;
select * from clientes;
select * from amigos;
select * from gafanhotos;
desc gafanhotos;
select * from gafanhoto_assiste_curso;

select * from cursos order by nome DESC;
select nome, descricao, carga  from cursos WHERE ano = '2016' order by nome;
select nome, descricao, carga  from cursos WHERE ano != '2016' order by nome;
select nome, descricao, carga  from cursos WHERE ano <> '2016' order by nome;
select nome, ano from cursos WHERE ano between '2014' and '2016 'order by ano desc, nome asc;
select nome, ano from cursos WHERE ano in (2014,2016) order by ano;

select * from cursos WHERE nome LIKE 'P%' order by nome;
select * from cursos WHERE nome not LIKE '%A%' order by nome;
select * from cursos WHERE nome LIKE 'PHP_' order by nome;
select * from gafanhotos where nome like '%silva%';
select distinct carga from cursos;
select distinct nacionalidade from gafanhotos order by nacionalidade;
select count(*) from cursos;
select carga, count(nome) from cursos group by carga;
select max(carga) from cursos order by carga;
#select nome, min(totaulas) from cursos where ano = '2016'; VERIFICAR QUAL A SINTAXE CORRETA
select sum(totaulas) from cursos where ano = '2016';
select avg(totaulas) from cursos where ano = '2016';


# EXERCÍCIOS
select * from gafanhotos where sexo ='F';
select * from gafanhotos where nascimento between '2000-01-01' and '2015-12-31';
select * from gafanhotos where profissao = 'Programador' and sexo = 'M';
select * from gafanhotos where nacionalidade = 'Brasil' and nome like 'J%' and sexo ='F';
select nome, nacionalidade from gafanhotos where nome like '%Silva%' and not nacionalidade = 'Brasil' and peso < 100 and sexo = 'M';
select max(altura) from gafanhotos where sexo = 'M' and nacionalidade = 'Brasil';
select avg(peso) from gafanhotos;
select min(peso) from gafanhotos where sexo = 'F' and not nacionalidade = 'Brasil' and nascimento between '1990-01-01' and '2000-12-31';
select count(*) from gafanhotos where altura > '1.90' and sexo = 'F';

# Aula 13 – SELECT (Parte 3)
select distinct carga from cursos order by carga;
select carga, count(*) from cursos group by carga;
select carga, totaulas from cursos where totaulas = 30 group by carga;
select carga, count(nome) from cursos where totaulas = 30 group by carga;
select carga, count(nome) from cursos group by carga having count(nome) >3;
select ano, count(*) from cursos group by ano having count(ano) >= 5 order by count(*) desc;
select avg(carga) from cursos;

select avg(carga) from cursos order by count(*) desc;

select carga, count(*) from cursos
where ano > 2015
group by carga
having carga > (select avg(carga) from cursos) order by count(*) desc;

# EXERCÍCIOS
# 1) UMA LISTA COM AS PROFISSÕES DOS GAFANHOSTOS E SEUS RESPECTIVOS QUANTITATIVOS
select * from gafanhotos;
select profissao, count(profissao) from gafanhotos group by profissao order by count(profissao) desc;

# 2) QUANTOS GAFANHOS HOOMENS E QUANTAS MULHERES NASCERAM APÓS 01/JAN/2005?
select * from gafanhotos where nascimento > '2005-01-01';

# 3) UMA LISTA COM OS GAFANHOTOS QUE NASCERAM FORA DO BRASIL, MONSTRANDO O PAÍS DE ORUGEM
	# E O TOTAL DE PESSOAS NASCIDAS LÁ. SÓ NOS INTERESSAM OS PAÍSES QUE TIVEREM MAIS DE 3 GAFANHOTOS COM ESSA NACIONALIDADE
select nacionalidade, count(nacionalidade) from gafanhotos
where nacionalidade != 'Brasil'
group by nacionalidade having count(nacionalidade) > 3 order by count(nacionalidade) desc;

# 4) UMA LISTA AGRUPADA PELA ALTURA DOS GAFANHOTOS, MOSTRANDO QUANTAS PESSOAS PESAM MAIS DE 100Kg E QUE ESTÁO
	# ACIMA DA MÉDIA DE ALTURA DE TODOS OS CADASTRADOS
#select avg(altura) from gafanhotos; # descobrindo a média das alturas
SELECT altura, COUNT(*) FROM gafanhotos WHERE peso >100 AND altura > (SELECT AVG(altura) FROM gafanhotos) GROUP BY altura;

select nome, idcurso from gafanhotos;

select g.nome, g.idcurso, c.nome, c.ano from gafanhotos as g inner join cursos as c on c.idcurso = g.idcurso order by g.nome;
select g.nome, g.idcurso, c.nome, c.ano from gafanhotos as g right outer join cursos as c on c.idcurso = g.idcurso order by g.nome;

select g.id, g.nome, c.idcurso, c.nome from gafanhotos as g
join gafanhoto_assiste_curso as a on g.id = a.idgafanhoto
join cursos as c on c.idcurso = a.idcurso
order by g.nome;