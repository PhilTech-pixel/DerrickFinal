# Generated by Django 3.2.12 on 2024-11-21 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.train'),
        ),
    ]