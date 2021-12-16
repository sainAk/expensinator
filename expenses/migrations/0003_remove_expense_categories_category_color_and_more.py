# Generated by Django 4.0b1 on 2021-11-05 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0002_alter_expense_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="expense",
            name="categories",
        ),
        migrations.AddField(
            model_name="category",
            name="color",
            field=models.CharField(default="#000000", max_length=7),
        ),
        migrations.AddField(
            model_name="expense",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
            ),
        ),
    ]
