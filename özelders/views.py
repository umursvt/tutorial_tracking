# Create your views here.
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import *





   
    



def get_current_time():
    #Get current time
    now = datetime.now()
    time = now.strftime('%H:%M')
    return time

def get_current_date():
    #Get current date
    date= datetime.now().date()
    return date
   



    
   
   
   


def current_lesson():
    current_time= get_current_time()
    current_date=get_current_date()
    
   
 #Tablodan gelen özel ders verisinin bilgilerini gerçek tarihe göre çeker
    current_lesson=ÖzelDers.objects.filter(ders_tarihi=current_date)
    print(current_lesson)   
        #Tablodan gelen özel ders verisinin tarihlerini çeker.
    
        
    for i in (current_lesson):
        derslerin_tarihi=i.ders_tarihi
        print(derslerin_tarihi )
        if derslerin_tarihi == current_date:
            derslerin_saati=i.ders_saati
            if (derslerin_saati) == current_time:
                if Ucretler.objects.filter(ders_tarihi=current_date, ders_saati=derslerin_saati).exists():
                    print('obje mevcut')
                else:
                    ucret=Ucretler(isim=i.öğretmen,ders_tarihi=i.ders_tarihi,ders_saati=i.ders_saati,fiyat=i.fiyat) #isim= Dersteki öğrencini ismi olmalı manytomany olduğu için alamıyorum
                    ucret.save()
                    print(ucret)
            else:
                print('Bu tarihteki ders saatleri uygun değil')
        else:
            print('tarihler uyuşmuyor')   
    return 


     
        
            
            
    

def home(request):
    current_date=get_current_date()
    current_lesson()
   
    #Get all objects
    dersler=ÖzelDers.objects.all()
    #Get only today's objects
    today=ÖzelDers.objects.filter(ders_tarihi=current_date)
    #Get ucretler for all
    ucretler=Ucretler.objects.all()
    time=get_current_time()
    
  
    context={
        'time':time,
        'dersler':dersler,
        'ucret':ucretler,
        'today':today
       
    }
    
    return render(request,'özelders/base.html',context)

