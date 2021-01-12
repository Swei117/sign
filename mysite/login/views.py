from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms

# Create your views here.
def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
     if request.method == "POST":
         login_form = forms.UserForm(request.POST)
         message = '请检查填写的内容!'
       #username = request.POST.get('username')
       #password = request.POST.get('password')
        
       #if username.strip() and password:
         if login_form.is_valid():
              username = login_form.cleaned_data.get('username')
              password = login_form.cleaned_data.get('password')
              try:
                  user=models.User.objects.get(name=username)
              except:
                  message = '用户不存在！'
               #return render (request,'login/login.html',{'message':message})
                  return render (request,'login/login.html',locals())
              if user.password == password: 
               #print(username, password)
                   return redirect('/index/')
              else:
                   message = '密码不正确！'
               #return render(request,'login/login.html',{'message':message})
                   return render(request,'login/login.html',locals())
         else:
            #return render (request,'login/login.html',{'message':message})
              return render(request, 'login/login.html', locals())
            
    #return render(request,'login/login.html')
     login_form = forms.UserForm()
     return render (request, 'login/login.html',locals())

       #print(username, password)
    #return render(request, 'login/login.html')

def register(request):
    pass
    return render(request,'login/register.html')
def cost(request):
    pass
    return render(request,'login/cost.html')
def electric(request):
    pass
    return render(request,'login/electric.html')
def manufacture(request):
    pass
    return render(request,'login/manufacture.html')
def mechanical(request):
    pass
    return render(request,'login/mechanical.html')
def logout(request):
    pass
    return render(request,"login")