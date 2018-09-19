from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name(request):
    form=forms.Formname()
    if request.method =='POST':
        form=forms.Formname(request.POST)
        if form.is_valid():
            print("valid")
            print("name:"+form.cleaned_data['name'])
            print("email:"+form.cleaned_data['email'])
            print("text:"+form.cleaned_data['text'])
    return render(request,'basicapp/form.html',{'form':form})