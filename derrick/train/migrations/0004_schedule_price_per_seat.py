# Generated by Django 3.2.12 on 2024-11-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0003_auto_20241121_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='price_per_seat',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]