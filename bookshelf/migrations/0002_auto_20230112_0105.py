# Generated by Django 3.2 on 2023-01-12 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='anio_pub',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='origen_disponible',
            field=models.BooleanField(default=False),
        ),
    ]