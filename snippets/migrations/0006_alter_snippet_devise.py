# Generated by Django 3.2.8 on 2021-10-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20211028_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='devise',
            field=models.CharField(choices=[('Eur', 'Eur'), ('Dollar', 'Dollar'), ('Sol', 'Sol')], default='Eur', max_length=20),
        ),
    ]
