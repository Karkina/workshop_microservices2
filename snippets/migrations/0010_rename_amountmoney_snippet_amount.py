# Generated by Django 3.2.8 on 2021-10-29 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_rename_montant_snippet_amountmoney'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='amountMoney',
            new_name='amount',
        ),
    ]
