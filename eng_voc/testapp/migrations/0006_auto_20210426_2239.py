# Generated by Django 3.1.5 on 2021-04-26 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20210426_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='example',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=3000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vocabulary',
            name='meaning',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=3000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vocabulary',
            name='mnemonic',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=3000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vocabulary',
            name='word',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=3000),
            preserve_default=False,
        ),
    ]
