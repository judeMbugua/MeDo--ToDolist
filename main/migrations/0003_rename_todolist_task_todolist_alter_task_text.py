# Generated by Django 5.0.3 on 2024-05-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_task"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="toDolist",
            new_name="todolist",
        ),
        migrations.AlterField(
            model_name="task",
            name="text",
            field=models.CharField(max_length=200),
        ),
    ]
