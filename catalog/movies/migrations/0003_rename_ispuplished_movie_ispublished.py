# Generated by Django 4.2 on 2023-04-30 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_ispuplished_alter_movie_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='isPuplished',
            new_name='isPublished',
        ),
    ]