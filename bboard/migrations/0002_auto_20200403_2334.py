# Generated by Django 2.2.12 on 2020-04-03 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
