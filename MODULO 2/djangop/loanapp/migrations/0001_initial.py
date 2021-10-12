# Generated by Django 3.2.8 on 2021-10-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('duracion', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='serv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(max_length=13)),
                ('servicio', models.CharField(choices=[('M', 'Maquillaje'), ('TC', 'Tratamientos Corporales'), ('TF', 'Tratamientos Faciales'), ('E', 'Especial')], max_length=50)),
            ],
        ),
    ]
