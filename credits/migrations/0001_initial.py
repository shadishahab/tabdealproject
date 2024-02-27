# Generated by Django 3.2 on 2024-02-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Credit Type',
                'verbose_name_plural': 'Credit Types',
            },
        ),
    ]