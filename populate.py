import os
import django
import random

# Configurar as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_consultas.settings')  # Substitua 'nome_do_seu_projeto' pelo nome do seu projeto Django
django.setup()

from consultas.models import Usuario, Nota, Curso, Matricula, Aula, Material
from faker import Faker
from django.db import transaction

fake = Faker()

def criar_usuarios(num=50):
    for _ in range(num):
        nome = fake.name()
        cpf = fake.unique.ssn()
        telefone = fake.phone_number()
        Usuario.objects.create(nome=nome, cpf=cpf, telefone=telefone)

def criar_cursos(num=50):
    for _ in range(num):
        nome = fake.word()
        descricao = fake.text(max_nb_chars=200)
        data_criacao = fake.date_this_year()
        Curso.objects.create(nome=nome, descricao=descricao, data_criacao=data_criacao)

def criar_matriculas(num=50):
    usuarios = Usuario.objects.all()
    cursos = Curso.objects.all()
    for _ in range(num):
        usuario = random.choice(usuarios)
        curso = random.choice(cursos)
        data_matricula = fake.date_this_year()
        Matricula.objects.create(usuario=usuario, curso=curso, data_matricula=data_matricula)

def criar_aulas(num=50):
    cursos = Curso.objects.all()
    for _ in range(num):
        curso = random.choice(cursos)
        descricao = fake.sentence()
        data = fake.date_this_year()
        Aula.objects.create(descricao=descricao, data=data, curso=curso)

def criar_materiais(num=50):
    aulas = Aula.objects.all()
    for _ in range(num):
        aula = random.choice(aulas)
        descricao = fake.sentence()
        tipo = random.choice(["PDF", "Vídeo", "Apresentação"])
        arquivo = fake.file_name(extension="pdf")
        link = fake.url()
        Material.objects.create(descricao=descricao, tipo=tipo, arquivo=arquivo, link=link, aula=aula)

def criar_notas(num=50):
    usuarios = Usuario.objects.all()
    aulas = Aula.objects.all()
    for _ in range(num):
        usuario = random.choice(usuarios)
        aula = random.choice(aulas)
        valor = round(random.uniform(5, 10), 2)  # Nota entre 5.0 e 10.0
        comentarios = fake.sentence()
        Nota.objects.create(usuario=usuario, aula=aula, valor=valor, comentarios=comentarios)

@transaction.atomic
def popular_banco():
    criar_usuarios(50)
    criar_cursos(50)
    criar_matriculas(50)
    criar_aulas(50)
    criar_materiais(50)
    criar_notas(50)
    print("Banco de dados populado com 50+ registros em cada tabela.")

if __name__ == "__main__":
    popular_banco()
