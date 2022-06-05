-- QUESTÃO 1
CREATE TABLE automovel (
    veiculo VARCHAR(10), -- Carro/Caminhão/Moto
    marca VARCHAR(20), -- Fiat/Renault
    modelo VARCHAR(20),  -- Uno/EcoSport 
    ano CHAR(4),
    placa CHAR(7),
    cpf_proprietario CHAR(11),
    id_veiculo SERIAL
);

CREATE TABLE segurado (
    cpf CHAR(11),
    nome VARCHAR(40),
    placa_veiculo CHAR(7),
    id_veiculo SERIAL
);

CREATE TABLE perito (
    id_perito SERIAL,
    nome VARCHAR(40),
    cpf CHAR(11)
);

CREATE TABLE oficina (
    nome VARCHAR(40),
    localidade VARCHAR(40),
    id_oficina SERIAL
);

CREATE TABLE seguro (
    valor NUMERIC,
    validade DATE,
    cpf_comprador CHAR(11),
    cpf_proprietario CHAR(11),
    sinistro SERIAL
);

CREATE TABLE sinistro (
    id_sinistro SERIAL
);

CREATE TABLE pericia (
    reparo BOOLEAN,
    perda_total BOOLEAN,
    descricao TEXT
);

CREATE TABLE reparo (
    id_veiculo SERIAL,
    placa_veiculo CHAR(7)
);






