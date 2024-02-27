# Generated by Django 3.2 on 2024-02-27 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('credits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditAddition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Credit Addition',
                'verbose_name_plural': 'Credit Additions',
            },
        ),
        migrations.CreateModel(
            name='CreditSubtraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('amount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='credit_purchases', to='credits.credittype')),
            ],
            options={
                'verbose_name': 'Credit Subtraction',
                'verbose_name_plural': 'Credit Subtractions',
            },
        ),
    ]
