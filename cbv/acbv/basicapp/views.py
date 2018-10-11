from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
class Indexview(TemplateView):
    template_name='index.html'
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['injected']='basic injuction'
        return context
