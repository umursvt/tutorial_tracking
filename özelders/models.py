from email.policy import default
from django.db import models
from django.forms import CharField
from datetime import datetime




# Create your models here.

class Öğretmen(models.Model):
    isim_soyisim=models.CharField('İsim, Soyisim',max_length=25)
    branş=models.CharField('Branş',max_length=25)
    tel=models.CharField('No',max_length=11)

    def __str__(self):
        return self.isim_soyisim


class Öğrenci(models.Model):
     isim_soyisim=models.CharField('İsim, Soyisim',max_length=25)
     
     def __str__(self):
         return self.isim_soyisim
     
        


    

class ÖzelDers(models.Model):
    öğretmen=models.ForeignKey(Öğretmen,max_length=25, on_delete=models.CASCADE, null=False, blank=False)
    öğrenci=models.ManyToManyField(Öğrenci,'Öğrenci',max_length=25)
    ders_ad= models.CharField('Dersin adı',max_length=25)
    ders_konu= models.CharField('Ders konu',max_length=50)
    ders_tarihi=models.DateField()
    ders_saati=models.CharField(max_length=5)
    ders_yeri= models.CharField('Ders yeri',max_length=100, blank=True)
    fiyat= models.IntegerField(verbose_name='Ders ücreti', default=250)

    def __str__(self):
        return str(self.öğretmen) + ' - ' + '/'.join(i.isim_soyisim for i in self.öğrenci.all()) + ' / ' + str(self.ders_tarihi) + ' / ' + str(self.ders_saati)

class Ucretler(models.Model):
    isim=models.CharField(max_length=20, null=True)
    ders_tarihi=models.DateField(null=True)
    ders_saati=models.CharField(max_length=5,null=True)
    fiyat= models.IntegerField(verbose_name='Ders ücreti', default=250,null=True)

    def __str__(self):
        return self.isim + '    -->   ' + str(self.ders_tarihi)