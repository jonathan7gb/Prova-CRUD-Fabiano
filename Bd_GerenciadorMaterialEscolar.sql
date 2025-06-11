create database materialEscolar;
use materialEscolar;

create table materiais(
	id int auto_increment primary key,
    titulo longtext not null,
    quantidade_estoque int check (quantidade_estoque >= 0 ),
    isbn varchar(50) not null unique,
    data_aquisicao date default '2025-06-11' check (data_aquisicao <= '2025-06-11'),
    tipo enum('Livro', 'Apostila', 'Multimídia', 'Periódico', 'Equipamento')
);

select * from materiais;