# Generated by Django 5.0 on 2024-01-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0005_remove_product_image_productimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.CharField(default="sasta", max_length=200),
            preserve_default=False,
        ),
    ]
