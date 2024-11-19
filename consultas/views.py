from django.shortcuts import render, redirect
from django.db import connection

def realizar_consulta(request):
    resultados = None
    erro = None

    # CRUD: Criar ou Editar um Usuário
    if request.method == "POST" and "criar_editar" in request.POST:
        nome = request.POST.get("nome", "").strip()
        cpf = request.POST.get("cpf", "").strip()
        usuario_id = request.POST.get("usuario_id", "").strip()

        # Se "usuario_id" estiver presente, é uma atualização, caso contrário, é uma criação
        if usuario_id:
            # Atualizar o usuário
            query = """
                UPDATE consultas_usuario 
                SET nome = %s, cpf = %s 
                WHERE id = %s
            """
            params = [nome, cpf, usuario_id]
        else:
            # Criar um novo usuário
            query = """
                INSERT INTO consultas_usuario (nome, cpf)
                VALUES (%s, %s)
            """
            params = [nome, cpf]

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
            return redirect('consultar_usuarios')  # Redireciona de volta para a página
        except Exception as e:
            erro = f"Erro ao executar a operação de CRUD: {e}"

    # CRUD: Deletar um Usuário
    if request.method == "POST" and "deletar" in request.POST:
        usuario_id = request.POST.get("usuario_id", "").strip()
        if usuario_id:
            query = "DELETE FROM consultas_usuario WHERE id = %s"
            params = [usuario_id]
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query, params)
                return redirect('consultar_usuarios')  # Redireciona após exclusão
            except Exception as e:
                erro = f"Erro ao excluir o usuário: {e}"

    # Consultas de leitura (select)
    if request.method == "POST" and "consulta" in request.POST:
        consulta = request.POST.get("consulta", "").strip()
        params = []
        query = ""

        # Consulta para usuários
        if consulta == "usuarios":
            nome = request.POST.get("nome", "").strip()
            cpf = request.POST.get("cpf", "").strip()

            query = "SELECT * FROM consultas_usuario WHERE 1=1"
            if nome:
                query += " AND nome ILIKE %s"
                params.append(f"%{nome}%")
            if cpf:
                query += " AND cpf = %s"
                params.append(cpf)

        # Consulta para média das notas dos usuários
        elif consulta == "media_notas":
            usuario_id = request.POST.get("usuario_id", "").strip()

            query = """
                SELECT u.id, u.nome, AVG(n.valor) AS media_nota
                FROM consultas_usuario u
                JOIN consultas_nota n ON u.id = n.usuario_id
                GROUP BY u.id
            """
            if usuario_id:
                query += " HAVING u.id = %s"
                params.append(usuario_id)

        # Consulta para matrículas por curso
        elif consulta == "matriculas_curso":
            curso_id = request.POST.get("curso_id", "").strip()

            query = """
                SELECT c.id, c.nome, COUNT(m.id) AS total_matriculas
                FROM consultas_curso c
                LEFT JOIN consultas_matricula m ON c.id = m.curso_id
                GROUP BY c.id
            """
            if curso_id:
                query += " HAVING c.id = %s"
                params.append(curso_id)

        # Consulta para matrículas por período
        elif consulta == "matriculas_periodo":
            data_inicio = request.POST.get("data_inicio", "").strip()
            data_fim = request.POST.get("data_fim", "").strip()

            query = """
                SELECT u.nome, c.nome AS curso, m.data_matricula
                FROM consultas_matricula m
                JOIN consultas_usuario u ON m.usuario_id = u.id
                JOIN consultas_curso c ON m.curso_id = c.id
                WHERE 1=1
            """
            if data_inicio and data_fim:
                query += " AND m.data_matricula BETWEEN %s AND %s"
                params.append(data_inicio)
                params.append(data_fim)

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                colunas = [col[0] for col in cursor.description]
                resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]
        except Exception as e:
            erro = f"Erro ao executar a consulta: {e}"

    return render(request, "index.html", {"resultados": resultados, "erro": erro})
