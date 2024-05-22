# Generated by Django 5.0.3 on 2024-05-09 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_todolist_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="todolist",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task",
                to="main.todolist",
            ),
        ),
    ]