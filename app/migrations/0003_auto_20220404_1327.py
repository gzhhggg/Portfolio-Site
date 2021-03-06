# Generated by Django 3.1.14 on 2022-04-04 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='cloud',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='cloud'),
        ),
        migrations.AlterField(
            model_name='work',
            name='database',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='database'),
        ),
        migrations.AlterField(
            model_name='work',
            name='framework',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='framework'),
        ),
        migrations.AlterField(
            model_name='work',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='言語'),
        ),
        migrations.AlterField(
            model_name='work',
            name='os',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='OS'),
        ),
    ]
