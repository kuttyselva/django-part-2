from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict={'insert':"hello!! im from class"}
    return render(request,'firstapp/index.html',context=my_dict)
