# Generated by Django 4.0.5 on 2022-07-11 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_quesmodel_myclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='topics',
            field=models.CharField(default='new', max_length=200),
        ),
    ]
