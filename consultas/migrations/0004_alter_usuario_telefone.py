# Generated by Django 5.1.3 on 2024-11-19 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0003_alter_usuario_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]