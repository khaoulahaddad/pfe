# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.conf import settings
from suppervision.models import Agent , Product

from django.core.mail import send_mail
from django.contrib.auth.models import User

from datetime import datetime
from django.utils.timezone import get_current_timezone
from time import strftime

import random


from django.shortcuts import get_object_or_404

############## Template Login ##############

class LoginView(TemplateView):

  template_name = 'front/login.html'

  def post(self, request, **kwargs):

    user = request.POST.get('email', False)
    password = request.POST.get('password', False)
    return render(request, self.template_name)

############## Login and Dashboard ##############

def test_cookies(request):
    resultat={}
    response=TemplateResponse(request, 'index.html',{'resultat': resultat})
    user=request.COOKIES.get('Your_Cookies')
    if(user):
        resultat["name_user"]=Agent.objects.get(email=user).first_name + ' ' + Agent.objects.get(email=user).last_name
        resultat["pending_requests"]= Product.objects.filter(date_livraison= None).count()
        resultat["order"]= Product.objects.count()
        resultat["money_monthly"]=0
        resultat["money_annual"]=00
        #mois elli ana en cours 
        #année elli en cours
        return response
    else:
        resultat["name_user"]="ok"
        return TemplateResponse(request, 'front/login.html',resultat)

def login(request):
    user = request.POST.get('email',False)
    password = request.POST.get('password',False)
    resultat={}
    response= TemplateResponse(request, 'index.html',{'resultat': resultat})
    if(Agent.objects.filter(email=user, code=password)):
        response.set_cookie('Your_Cookies', str(user))
        resultat["name_user"]=Agent.objects.get(email=user, code=password).first_name + ' ' + Agent.objects.get(email=user, code=password).last_name
        resultat["pending_requests"]= Product.objects.filter(date_livraison= None).count()
        resultat["order"]= Product.objects.count()
        resultat["money_monthly"]=0
        resultat["money_annual"]=00
        return response
    else:
        return HttpResponseRedirect('/')

def connectCarte(request):
    resultat={}
    return TemplateResponse(request, 'connectCarte.html',resultat)

############## ForgetPassword ##############

def forgetpassword(request):
    resultat={}
    return TemplateResponse(request, 'forgot-password.html',resultat)

def search (request):
    mail = request.POST.get('email',False)
    caracteres = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789" #Tu peux en ajouter si tu veux
    longueur = 30
    mdp = "" #Variable mot de passe
    compteur = 0 #Compteur de lettres
    
    while compteur < longueur:
        lettre = caracteres[random.randint(0, len(caracteres)-1)] #On tire au hasard une lettre
        mdp += lettre #Ona joute la lettre au mot de passe
        compteur += 1 #On incrémente le compteur de lettres
    Agent.objects.filter(email=mail).update(code=mdp)
    resultat={}
    subject = 'Please reset your password'
    message = " We heard that you lost your espace password. Sorry about that! \n But don’t worry! You can use this password to reset your password : " + mdp 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mail,]
    send_mail( subject, message, email_from, recipient_list )
    return TemplateResponse(request, 'email-password.html',resultat)

def teste(request):
    mail = request.POST.get('email',False)
    password = request.POST.get('password', False)
    resultat={}
    if (Agent.objects.filter(email=mail,code=password)):
        return TemplateResponse(request, 'reset-password.html',resultat)
    else :
        return HttpResponseRedirect('/')

def resetpsw(request):
    mail = request.POST.get('email',False)
    password1 = request.POST.get('password1', False)
    password2 = request.POST.get('password2', False)
    resultat={}
    response = TemplateResponse(request, 'index.html',resultat)
    if(password1==password2):
        response.set_cookie('Your_Cookies', str(mail))
        resultat["name_user"]=Agent.objects.get(email=mail).first_name + ' ' + Agent.objects.get(email=mail).last_name
        Agent.objects.filter(email=mail).update(code=password1)
        return response
    else :
        return HttpResponseRedirect('/')

############## EditProfil ##############

def profil(request):
    resultat={}
    user=request.COOKIES.get('Your_Cookies')
    resultat["firstname_user"]=Agent.objects.get(email=user).first_name
    resultat["lastname_user"]=Agent.objects.get(email=user).last_name
    resultat["name_user"]=resultat["firstname_user"] + ' ' +resultat["lastname_user"]
    return TemplateResponse(request, 'profil.html',{'resultat' : resultat})

def confirm(request):
    firstname = request.POST.get('firstname',False)
    lastname = request.POST.get('lastname',False)
    currentpassword = request.POST.get('currentpassword',False)
    newpassword= request.POST.get('newpassword',False)
    confirmpassword= request.POST.get('confirmpassword',False)
    if(firstname !=''):
        Agent.objects.filter(id=1).update(first_name = firstname)
    if(lastname != ''):
        Agent.objects.filter(id=1).update(last_name = lastname)
    if(Agent.objects.filter(id=1,code=currentpassword)and(newpassword!=False)and(confirmpassword!=False)and(newpassword==confirmpassword)):
        Agent.objects.filter(id=1).update(code = newpassword)
    return HttpResponseRedirect('/profil')

############## Products ##############

def allproduct(request):
    products = Product.objects.all()
    resultat={}
    user=request.COOKIES.get('Your_Cookies')
    resultat["name_user"]=Agent.objects.get(email=user).first_name + ' ' + Agent.objects.get(email=user).last_name
    return render(request,'allProduct.html', {'resultat': resultat, 'products': products})

def newproduct(request):
    products = Product.objects.filter(statut='nouveau')
    resultat={}
    user=request.COOKIES.get('Your_Cookies')
    resultat["name_user"]=Agent.objects.get(email=user).first_name + ' ' + Agent.objects.get(email=user).last_name
    return render(request,'newProduct.html', {'resultat': resultat, 'products': products})

def currentproduct(request):
    products = Product.objects.filter(statut='occupe')
    resultat={}
    user=request.COOKIES.get('Your_Cookies')
    resultat["name_user"]=Agent.objects.get(email=user).first_name + ' ' + Agent.objects.get(email=user).last_name
    return render(request,'currentProduct.html', {'resultat': resultat, 'products': products})

def resolvedproduct(request):
    products = Product.objects.filter(statut='termine')
    resultat={}
    user=request.COOKIES.get('Your_Cookies')
    resultat["name_user"]=Agent.objects.get(email=user).first_name + ' ' + Agent.objects.get(email=user).last_name
    return render(request,'resolvedProduct.html', {'resultat': resultat, 'products': products})

def detailproduct(request):
    resultat= {}
    user=request.COOKIES.get('Your_Cookies')
    resultat["name_user"]=Agent.objects.get(email=user).first_name + ' ' + Agent.objects.get(email=user).last_name
    return render(request,'detailProduct.html', {'resultat':resultat})

def addproduct(request):
    resultat= {}
    user=request.COOKIES.get('Your_Cookies')
    resultat["name_user"]=Agent.objects.get(email=user).first_name + ' ' + Agent.objects.get(email=user).last_name
    return render(request,'addProduct.html', {'resultat':resultat})

############## Logout ##############

def logout(request):
    response =HttpResponseRedirect('/') 
    response.delete_cookie('Your_Cookies')
    return response



    