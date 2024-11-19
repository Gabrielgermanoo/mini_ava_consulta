from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15, unique=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    
    class Meta:
        db_table = 'consultas_usuario'  # Garantir que a tabela seja 'consultas_usuario'

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateField()

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateField()

    def __str__(self):
        return f'{self.usuario.nome} - {self.curso.nome}'

class Aula(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.curso.nome} - {self.descricao}'

class Material(models.Model):
    descricao = models.TextField()
    tipo = models.CharField(max_length=50)
    arquivo = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.aula.descricao} - {self.descricao}'

class Nota(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    comentarios = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.nome} - {self.valor}'
