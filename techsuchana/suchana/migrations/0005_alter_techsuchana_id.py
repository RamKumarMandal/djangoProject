# Generated by Django 3.2.10 on 2023-02-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suchana', '0004_auto_20221230_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techsuchana',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]