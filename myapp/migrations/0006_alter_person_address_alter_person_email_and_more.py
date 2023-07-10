# Generated by Django 4.2 on 2023-05-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_person_email_alter_person_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='portfolio',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]