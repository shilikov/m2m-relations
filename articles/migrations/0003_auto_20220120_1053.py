# Generated by Django 3.1.2 on 2022-01-20 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20211004_0209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scopeship',
            options={'ordering': ['-is_main', 'tag__name'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики Статьи'},
        ),
    ]
