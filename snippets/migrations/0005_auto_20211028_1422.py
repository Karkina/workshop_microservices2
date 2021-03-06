# Generated by Django 3.2.8 on 2021-10-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_remove_snippet_linenos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='montant',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='status',
            field=models.CharField(choices=[('Closing', 'Closing'), ('Structuring', 'Structuring'), ('Push', 'Push')], default='Waiting', max_length=20),
        ),
    ]
