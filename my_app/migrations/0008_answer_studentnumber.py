# Generated by Django 3.1.7 on 2021-03-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_homework_tozihat'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='studentNumber',
            field=models.IntegerField(null=True),
        ),
    ]