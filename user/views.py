from email import message
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        sifre1 = request.POST['sifre']
        sifre2 = request.POST['sifre2']

        if kullanici != '' and email != '' and sifre1 != '' and sifre2 !='':
            if sifre1 == sifre2:
                if User.objects.filter(username = kullanici).exists():
                    messages.error(request, 'Bu kullanıcı adı zaten mevcut')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Bu mail adres adı zaten mevcut')
                    return redirect('register')
                elif len(sifre1) < 6:
                    messages.error(request,'Şifre en az 6 karakter olmalı')
                    return redirect('register')
                elif kullanici in sifre1:
                    messages.error(request,'Kullanıcı adı ile şifre benzer olmamalıdır')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=kullanici,email=email,password=sifre1)
                    user.save()
                    messages.success(request,'Kullanıcı başarı ile oluşturuldu')
                    return render(request,'özelders/base.html')
            else:
                messages.error(request,'Şifreler uyuşmuyor')
                return redirect('register') 
        else:
            messages.error(request,'Tüm alanların doldurulması gerekmektedir.')
            return redirect('register')           
    return render(request,'user/register.html')


def user_login(request):
    if request.method == 'POST':
                kullanici=request.POST['kullanici']
                sifre=request.POST['sifre']

                user=authenticate(request, username=kullanici, password=sifre)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Giriş yapıldı.')
                    return redirect('home')
                else:
                    messages.error(request, 'Kullanıcı adı ve şifre hatalı')
                    return redirect('login')
    return render(request,'user/login.html')
            




def user_logout(request):
            logout(request)
            messages.success(request,'Çıkış yapıldı')
            return render(request,'özelders/base.html')    
                