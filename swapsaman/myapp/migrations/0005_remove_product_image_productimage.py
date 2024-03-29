# Generated by Django 5.0 on 2024-01-01 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_alter_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_image", models.ImageField(upload_to="products/%Y/%m/%d")),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.product"
                    ),
                ),
            ],
        ),
    ]
