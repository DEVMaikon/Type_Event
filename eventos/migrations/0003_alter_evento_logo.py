# Generated by Django 4.2 on 2023-04-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_alter_evento_criador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='logo',
            field=models.ImageField(upload_to='logos'),
        ),
    ]
