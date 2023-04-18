# Generated by Django 3.2.4 on 2021-06-29 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechSuchana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlines', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('teaser', models.TextField()),
                ('largeteaser', models.TextField()),
                ('news', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='newspic')),
                ('sharelink', models.CharField(max_length=200)),
                ('displaylink', models.CharField(max_length=200)),
                ('home', models.BooleanField(default=False)),
                ('technews', models.BooleanField(default=False)),
                ('gadgets', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('techdeals', models.BooleanField(default=False)),
                ('automobile', models.BooleanField(default=False)),
                ('techsiksha', models.BooleanField(default=False)),
                ('techjobs', models.BooleanField(default=False)),
                ('uninotice', models.BooleanField(default=False)),
            ],
        ),
    ]