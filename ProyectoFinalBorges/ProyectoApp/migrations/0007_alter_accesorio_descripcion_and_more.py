# Generated by Django 4.2.5 on 2023-10-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoApp', '0006_alter_maquillaje_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorio',
            name='descripcion',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='cremascorporales',
            name='descripcion',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='cremasfaciales',
            name='descripcion',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='maquillaje',
            name='descripcion',
            field=models.TextField(max_length=1000),
        ),
    ]
