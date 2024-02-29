# Generated by Django 5.0.2 on 2024-02-29 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelves', '0003_remove_bookshelf_shelf_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=64)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelves.bookshelf')),
            ],
        ),
    ]