# Generated by Django 4.2.11 on 2025-02-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paciente_crianca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField()),
                ('nome', models.CharField(max_length=32)),
                ('data_de_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='profissional_de_saude',
            fields=[
                ('cpf', models.CharField(max_length=16, primary_key=1, serialize=False)),
                ('crm', models.CharField(max_length=16, null=1, unique=1)),
                ('coren', models.CharField(max_length=16, null=1, unique=1)),
                ('nome', models.CharField(max_length=64)),
                ('telefone', models.CharField(max_length=16)),
                ('senha', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='responsavel_crianca',
            fields=[
                ('cpf', models.CharField(max_length=16, primary_key=1, serialize=False)),
                ('nome', models.CharField(max_length=64)),
                ('telefone', models.CharField(max_length=16)),
            ],
        ),
    ]
