from django.shortcuts import render
from django.views import View

class Landing(View):
    def get(self,request):
        return render (request,"Landing.html")

class Register(View):
    def get(self,request):
        return render(request,"Register.html")

class Login(View):
    def get(self,request):
        return render(request,"Login.html")
