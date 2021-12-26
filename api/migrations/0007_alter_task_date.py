# Generated by Django 4.0 on 2021-12-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(auto_now=True, choices=[('Today', 'Bugun'), ('Tomorrow', 'Ertaga'), ('Next_week', 'Keyingi hafta')], null=True),
        ),
    ]
