# Generated by Django 2.0.5 on 2018-06-10 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('cpf', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('contato', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('cnpj', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('endereco', models.CharField(max_length=45)),
                ('contato', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cpf', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('historico', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('cpf', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('contato', models.CharField(max_length=45)),
                ('cnpj_clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brain.Clinica')),
            ],
        ),
        migrations.CreateModel(
            name='Trabalha_Em',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj_clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brain.Clinica')),
                ('cpf_profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brain.Profissional')),
            ],
        ),
        migrations.AddField(
            model_name='admin',
            name='cnpj_clinica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brain.Clinica'),
        ),
    ]
