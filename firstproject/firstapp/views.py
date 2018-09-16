from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import AccessRecord,Webpage,Topic,Exercise
# Create your views here.
def index(request):
    #weblist=AccessRecord.objects.order_by('date')
    #date_dict={'acc_rec':weblist}
    exer=Exercise.objects.order_by('fname')
    edict={'exe':exer}



    my_dict={'insert':"hello!! im from class"}
    return render(request,'firstapp/index.html',context=edict)
