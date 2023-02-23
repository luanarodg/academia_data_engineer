create table campeonato(
	id integer primary key auto_increment,
    nome varchar(30),
    cidade varchar(30)
);
create table times(
	id integer primary key auto_increment,
    nome varchar(30),
    cidade varchar(30)
);
create table inscritos(
	id_times integer,
    foreign key (id_times) references times(id),
    id_campeonato integer,
    foreign key (id_campeonato) references campeonato(id)
);
create table jogadoras(
	cpf varchar(20) primary key,
    nome varchar(30),
    id_times integer,
    foreign key (id_times) references times(id)
);

-- Inserir 3 times
insert into times (nome, cidade) values ('accenture' , 'são paulo'), ('gama', 'recife'), ('azure', 'rio de janeiro');

-- Inserir 4 registros na tabela de jogadoras
insert into jogadoras (cpf, nome) values ('111.111.111-11','Beatriz'),('22222222222','Lígia'),('333.333.333-33','Carolina'),('444444444-44','Luana');

-- Inserir 2 campeonatos
insert into campeonato (nome, cidade) values ('brasileiro', 'são paulo'), ('americano','rio de janeiro');

-- Relacionar os 3 times nos 2 campeonatos disponíveis
insert into inscritos (id_times, id_campeonato) values (1,1), (2,1), (3,1), (1,2), (2,2), (3,2);

-- Escolha um dos times para deletar. Essa operação foi bem sucedida?
delete from times where id = 1; 
-- operação não foi bem sucedida por conta da chave estrangeira;