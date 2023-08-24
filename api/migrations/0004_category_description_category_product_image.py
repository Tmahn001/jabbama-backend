# Generated by Django 4.2.3 on 2023-08-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='product_image',
            field=models.ImageField(default=1, upload_to='categories/'),
            preserve_default=False,
        ),
    ]
