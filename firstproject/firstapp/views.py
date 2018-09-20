from django.shortcuts import render
from django.http import HttpResponse
#from firstapp.models import AccessRecord,Webpage,Topic,Exercise
from firstapp.forms import NewUser
# Create your views here.
def index(request):
    #weblist=AccessRecord.objects.order_by('date')
    #date_dict={'acc_rec':weblist}
    #exer=Exercise.objects.order_by('fname')
    #edict={'exe':exer}
    form=NewUser()
    if request.method =="POST":
        form=NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('error form invalid')
    return render(request,'firstapp/index.html',{'form':form})
def success(request):
    dic={'kiki':"mumu"}
    return render(request,'firstapp/success.html',content=dic)
