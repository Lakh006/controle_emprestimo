# Generated by Django 5.1.6 on 2025-04-12 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_emprestimo', '0002_rename_colaborador_colaboradormodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='GerenteModel',
            fields=[
                ('idGERENTE', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True)),
            ],
        ),
    ]
