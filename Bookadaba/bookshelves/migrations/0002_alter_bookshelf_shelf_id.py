# Generated by Django 5.0.2 on 2024-02-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelves', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshelf',
            name='shelf_id',
            field=models.IntegerField(),
        ),
    ]