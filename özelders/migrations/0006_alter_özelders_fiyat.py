# Generated by Django 4.1.2 on 2022-10-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('özelders', '0005_alter_özelders_fiyat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='özelders',
            name='fiyat',
            field=models.IntegerField(default=250, verbose_name='Ders ücreti'),
        ),
    ]
