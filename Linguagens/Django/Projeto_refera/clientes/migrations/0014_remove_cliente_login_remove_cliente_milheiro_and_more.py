# Generated by Django 4.1.7 on 2023-02-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0013_rename_data_voo_cliente_data_atrelamento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Login',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Milheiro',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Senha',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Ticket_voo',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Chamado',
            field=models.CharField(max_length=7),
        ),
    ]