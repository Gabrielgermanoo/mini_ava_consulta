# Mini_ava_consulta

## Como instalar e executar o sistema?
- Instalação:
  Ao fazer o clone do repositório é recomendado utilizar um ambiente virtual para instalar os pacotes Python para o uso do sistema. Após isso, instalar os pacotes necessários usando:
  ```bash
  pip install -r requirements.txt
  ```
  Após isso, é necessário fazer uma migração dos dados do backend do projeto de maneira a registrar as tabelas no sistema.
  ```bash
  python manage.py migrate
  ```
  Com isso, é possível executar o sistema:
  ```bash
    python manage.py runserver
  ```

Todos esses passos apenas são possíveis se o sistema tiver um banco de dados funcionando. O usado nesse projeto foi o POSTGRESQL.


# Consultas SQL

## Operações CRUD
### Criar ou Editar um Usuário

**Descrição**: Insere um novo usuário no banco de dados ou atualiza um usuário existente.

**Inserção**:

INSERT INTO consultas_usuario (nome, cpf)
VALUES (%s, %s);

**Parâmetros**:
%s: Nome do usuário.
%s: CPF do usuário.

**Atualização**:

UPDATE consultas_usuario 
SET nome = %s, cpf = %s 
WHERE id = %s;

**Parâmetros**:
%s: Nome atualizado.
%s: CPF atualizado.
%s: ID do usuário a ser atualizado.

### Deletar um Usuário
**Descrição**: Remove um usuário do banco de dados com base no ID fornecido.

**Consulta**:

DELETE FROM consultas_usuario 
WHERE id = %s;

**Parâmetros**:
%s: ID do usuário a ser excluído.

## Consultas de Leitura (SELECT)
### Listar Usuários
**Descrição**: Busca usuários no banco, com filtros opcionais por nome ou CPF.

**Consulta**:

SELECT * FROM consultas_usuario 
WHERE 1=1
[AND nome ILIKE %s]
[AND cpf = %s];

**Parâmetros opcionais**:
%s: Nome do usuário (com suporte a correspondência parcial).
%s: CPF exato do usuário.

### Média das Notas dos Usuários
**Descrição**: Calcula a média das notas de cada usuário, agrupando por ID do usuário.

**Consulta**:

SELECT u.id, u.nome, AVG(n.valor) AS media_nota
FROM consultas_usuario u
JOIN consultas_nota n ON u.id = n.usuario_id
GROUP BY u.id
[HAVING u.id = %s];

**Parâmetros opcionais**:
%s: ID do usuário para filtrar resultados.

### Matrículas por Curso
**Descrição**: Conta o total de matrículas para cada curso, agrupando por ID do curso.

**Consulta**:

SELECT c.id, c.nome, COUNT(m.id) AS total_matriculas
FROM consultas_curso c
LEFT JOIN consultas_matricula m ON c.id = m.curso_id
GROUP BY c.id
[HAVING c.id = %s];

**Parâmetros opcionais**:
%s: ID do curso para filtrar resultados.

### Matrículas por Período
**Descrição**: Retorna matrículas realizadas em um intervalo de datas, com informações do curso e do usuário.

**Consulta**:

SELECT u.nome, c.nome AS curso, m.data_matricula
FROM consultas_matricula m
JOIN consultas_usuario u ON m.usuario_id = u.id
JOIN consultas_curso c ON m.curso_id = c.id
WHERE 1=1
[AND m.data_matricula BETWEEN %s AND %s];

**Parâmetros opcionais**:
%s: Data de início do período.
%s: Data de fim do período.
