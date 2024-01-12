CREATE TABLE cliente (
  id BIGINT, 
  idade INT, 
  sexo CHAR, 
  dependentes INT, 
  escolaridade VARCHAR(20), 
  tipo_cartao VARCHAR(10), 
  limite_credito DOUBLE, 
  valor_transacoes_12m DOUBLE, 
  qtd_transacoes_12m BIGINT
);

show TABLES;
DESC cliente;

INSERT INTO cliente VALUES (768805383, 45, 'M', 3, 'ensino medio', 'blue', 12691.51, 1144.90, 42);

INSERT INTO cliente VALUES (768805372, 40, 'F', 5, 'ensino fundamental', 'blue', 15691.51, 1024.90, 37);
INSERT INTO cliente VALUES (818770008, 49, 'F', 5, 'mestrado', 'blue', 8256.96, 1291.45, 33);
INSERT INTO cliente VALUES (713982108, 51, 'M', 3, 'mestrado', 'blue', 3418.56, 1887.72, 20);

INSERT INTO cliente VALUES (768805372, 48, 'F', 5, 'ensino medio', 'gold', 15691.51, 1024.90, 47),
						   (818550008, 69, 'F', 5, 'mestrado', 'blue', 9156.96, 251.45, 63),
						   (734982108, 41, 'M', 3, 'mestrado', 'platinum', 3568.56, 7887.72, 28);

SELECT * FROM cliente;

SELECT id, escolaridade, sexo FROM cliente;

SELECT id, escolaridade, sexo FROM cliente LIMIT 2;

SELECT 10 + 20 + 30 AS SOMA;

SELECT AVG(idade) AS Media FROM cliente;