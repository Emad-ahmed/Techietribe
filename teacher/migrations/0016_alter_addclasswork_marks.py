# Generated by Django 4.0.3 on 2022-08-20 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0015_alter_createclass_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addclasswork',
            name='marks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]