from django.conf.urls import url
from firstapp import views

urlpatterns=[
    url('',views.index,name='index'),
    url('success/',views.success,name='success'),

]
