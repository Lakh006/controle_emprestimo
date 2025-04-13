# Generated by Django 5.1.6 on 2025-04-12 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_emprestimo', '0008_remove_emprestimomodel_data_devolucao_real'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimomodel',
            name='data_devolucao_real',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='emprestimomodel',
            name='status',
            field=models.CharField(choices=[('Emprestado', 'Emprestado'), ('Em uso', 'Em uso'), ('Fornecido', 'Forncecido'), ('Devolvido', 'Devolvido'), ('Danificado', 'Daificado'), ('Perdido', 'Perdido')], default='Pendente', max_length=20),
        ),
    ]
