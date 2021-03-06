# Generated by Django 4.0 on 2021-12-26 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.icon'),
        ),
        migrations.AlterField(
            model_name='list',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.image'),
        ),
    ]
