# Generated by Django 4.1.4 on 2022-12-08 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_tasklist_manage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]