# Generated by Django 4.2 on 2023-05-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='passport',
            field=models.IntegerField(unique=True),
        ),
    ]
