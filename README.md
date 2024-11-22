# Mini-AVA (Ambiente Virtual de Aprendizagem)

Bem-vindo ao Mini-AVA, um projeto desenvolvido para gerenciar e facilitar o processo de ensino e aprendizagem em um ambiente virtual. Este sistema é composto por múltiplos microsserviços que, juntos, permitem a administração de cursos, aulas, notas e usuários.

---

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **Django Framework**: Usado para criar a API e os serviços relacionados.
- **Django Rest Framework (DRF)**: Utilizado para criar endpoints RESTful para comunicação entre microsserviços.
- **PostgreSQL**: Banco de dados para persistência das informações.
- **HTML, CSS**: Frontend básico para renderizar páginas.
- **Docker**: Containerização para gerenciar microsserviços.
- **Gunicorn e Nginx**: Usados para servir a aplicação em produção.

---

## Estrutura do Projeto

O Mini-AVA está dividido em diversos microsserviços:

### 1. **Autenticação**
- **Descrição**: Gerencia os usuários e a autenticação.
- **Funções**:
  - Registro de usuários.
  - Autenticação (login e logout).
  - Integração com grupos e permissões.
- **Endpoints**:
  - `/api/usuarios/`: CRUD de usuários.
  - `/api/login/`: Endpoint de login.
  - `/api/logout/`: Endpoint de logout.
- **Modelo Principal**:
  - `Usuario`: Substitui o modelo padrão `auth.User` para customização.

---

### 2. **Cursos**
- **Descrição**: Gerencia os cursos disponíveis no sistema.
- **Funções**:
  - CRUD de cursos.
  - Matrícula de usuários em cursos.
- **Endpoints**:
  - `/api/cursos/`: Listagem e manipulação de cursos.
  - `/api/matriculas/`: Gerenciamento de matrículas.
- **Modelo Principal**:
  - `Curso`: Representa um curso no sistema.
  - `Matricula`: Liga alunos a cursos.

---

### 3. **Aulas**
- **Descrição**: Gerencia as aulas associadas aos cursos.
- **Funções**:
  - CRUD de aulas.
  - Associação de aulas a cursos.
- **Endpoints**:
  - `/api/aulas/`: Listagem e manipulação de aulas.
- **Modelo Principal**:
  - `Aula`: Representa uma aula dentro de um curso.

---

### 4. **Notas**
- **Descrição**: Gerencia as notas atribuídas a alunos.
- **Funções**:
  - CRUD de notas.
  - Associação de notas a alunos e aulas.
- **Endpoints**:
  - `/api/notas/`: Listagem e manipulação de notas.
- **Modelo Principal**:
  - `Nota`: Representa a nota atribuída a um aluno em uma aula específica.

---

### 5. **Frontend**
- **Descrição**: Interface gráfica para usuários finais.
- **Funções**:
  - Renderização de páginas HTML para usuários administrativos.
  - Formulários e tabelas para manipulação dos dados.
- **URLs Principais**:
  - `/usuarios/`: Listagem e gerenciamento de usuários.
  - `/cursos/`: Listagem e gerenciamento de cursos.
  - `/aulas/`: Listagem e gerenciamento de aulas.
  - `/notas/`: Listagem e gerenciamento de notas.

---

## Funcionalidades

- **Gerenciamento de Usuários**:
  - Cadastro de novos usuários.
  - Associação de usuários a grupos.
- **Gerenciamento de Cursos e Matrículas**:
  - Criação, edição e exclusão de cursos.
  - Matrícula de usuários em cursos.
- **Gerenciamento de Aulas**:
  - Criação de aulas associadas a cursos.
- **Atribuição de Notas**:
  - Registro de notas para alunos em aulas específicas.
  - Visualização de notas por data e aluno.

---

## Instruções de Instalação

### 1. Requisitos
- **Python 3.10 ou superior**
- **Docker e Docker Compose**
- **Node.js (opcional, para desenvolvimento frontend avançado)**

### 2. Configuração do Ambiente
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-repositorio/mini-ava.git
   cd mini-ava
   ```
2. Crie um ambiente virtual
  ```bash
  python3 -m venv venv
  source venv/bin/activate
   ```
3. Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```
4. Aplique as migrações do banco de dados:
  ```bash
  python manage.py migrate
  ```
5. Crie um superusuário:
  ```bash
  python manage.py createsuperuser
  ```
7. Rodar o servidor
  ```bash
  python manage.py runserver
  ```
