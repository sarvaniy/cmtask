# Generated by Django 3.2.9 on 2021-11-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency', models.CharField(max_length=100)),
                ('to_currency', models.CharField(max_length=100)),
                ('ex_rate', models.CharField(max_length=100)),
            ],
        ),
    ]
