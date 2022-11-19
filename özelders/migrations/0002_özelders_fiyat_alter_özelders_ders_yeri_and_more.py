# Generated by Django 4.1.2 on 2022-10-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('özelders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='özelders',
            name='fiyat',
            field=models.IntegerField(default=250, verbose_name='Ders ücreti'),
        ),
        migrations.AlterField(
            model_name='özelders',
            name='ders_yeri',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ders yeri'),
        ),
        migrations.AlterField(
            model_name='öğrenci',
            name='açıklama',
            field=models.TextField(max_length=250, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='öğrenci',
            name='isim_soyisim',
            field=models.CharField(max_length=25, verbose_name='İsim, Soyisim'),
        ),
        migrations.AlterField(
            model_name='öğrenci',
            name='sınıf',
            field=models.CharField(max_length=15, verbose_name='Sınıf'),
        ),
        migrations.AlterField(
            model_name='öğretmen',
            name='branş',
            field=models.CharField(max_length=25, verbose_name='Branş'),
        ),
        migrations.AlterField(
            model_name='öğretmen',
            name='isim_soyisim',
            field=models.CharField(max_length=25, verbose_name='İsim, Soyisim'),
        ),
    ]
