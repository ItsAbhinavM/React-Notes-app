# Generated by Django 3.2.9 on 2023-12-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoNotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
