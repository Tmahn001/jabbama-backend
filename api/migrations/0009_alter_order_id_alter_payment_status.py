# Generated by Django 4.2.3 on 2023-08-28 17:01

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_payment_id_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
