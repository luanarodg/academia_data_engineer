-- database clinica
-- Listar o nome de todos os pacientes:
select * from clinica.pacientes;
select nome from pacientes; 


-- Quantos médicos estão cadastrados?
select count(*) from clinica.medicos;


-- Quais os nomes dos pacientes que fizeram mais de 2 consultas?
select count(*) as total, nome from pacientes, consultas
where pacientes.id = consultas.id_paciente
group by pacientes.nome
having total > 2;

-- OU 

select count(*) as total, p.nome
from pacientes p inner join consultas c
on p.id = c.id_paciente
group by p.nome
having total >2;


-- Listar todos os médicos com especialidade de ortopedia:
select nome from medicos
where medicos.especialidade = "ortopedia";


-- Listar apenas pacientes maiores de 30 anos:
select nome, idade from pacientes
where idade > 30;


-- Qual a quantidade de pacientes com idade acima de 40 anos?
select count(*) from pacientes
where idade > 40;


-- Quais pacientes não fizeram nenhuma consulta?
##exemplo aula
select * from pacientes p left join consultas c on p.id = c.id_paciente where c.id_paciente is null;


-- Qual a média de idade dos pacientes?
select avg(idade) from pacientes;


-- Qual o paciente mais novo?
select * from pacientes
where idade = (select min(idade) from pacientes);


-- Qual o paciente mais velho?
select * from pacientes
where idade = (select max(idade) from pacientes);


-- Quais cidades possuem mais pacientes?
select count(*) as total, cidade from pacientes, consultas
where pacientes.id = consultas.id_paciente
group by pacientes.cidade;

-- OU

select count(*) as total, cidade
from pacientes
group by cidade
order by total desc;


-- Quantos médicos estão acima de 40 anos?
select count(*) from medicos
where idade > 40;


-- Qual a capacidade da sala onde o médico Pedro atende?
select m.nome, q.capacidade from medicos m inner join quartos q on q.id = m.id_quarto where m.nome = "Pedro";


-- Qual a capacidade da sala onde a médica Márcia atende?
select m.nome, q.capacidade from medicos m inner join quartos q on q.id = m.id_quarto where m.nome = "Marcia";


-- Quantas consultas foram feitas por motivo de virose?
select count(*) from consultas
where doenca = "virose";


-- Listar o nome e idade dos pacientes cujo motivo de consulta foi fratura:
select p.nome, p.idade from pacientes p inner join consultas c on p.id = c.id_paciente where c.doenca = "fratura";


-- Listar o nome dos médicos que fizeram atendimento de tosse:
select m.nome from medicos m inner join consultas c on m.id = c.id_medico where c.doenca = "tosse";


-- Listar o nome dos médicos que fizeram atendimento de virose:
select m.nome from medicos m inner join consultas c on m.id = c.id_medico where c.doenca = "virose" group by nome;


-- Listar o nome dos médicos e a capacidade dos quartos onde atendem:
select m.nome, q.capacidade from medicos m inner join quartos q on q.id = m.id_quarto;

