# Generated by Django 5.1.4 on 2024-12-30 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
