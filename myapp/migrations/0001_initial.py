# Generated by Django 4.2 on 2023-04-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('passport', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('height', models.FloatField(max_length=2)),
                ('portfolio', models.URLField()),
                ('profile_image', models.ImageField(upload_to='')),
            ],
        ),
    ]