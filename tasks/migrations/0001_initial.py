# Generated by Django 4.0.1 on 2022-05-20 23:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('conc_date', models.DateField()),
                ('concluded', models.BooleanField(default=False)),
            ],
        ),
    ]
