# Generated by Django 4.1.2 on 2022-11-13 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('özelders', '0012_ucretler_ders_saati_ucretler_ders_tarihi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='öğrenci',
            name='sınıf',
        ),
    ]
