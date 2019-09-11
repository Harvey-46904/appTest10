from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('',views.hello,name='hello'),
    path('',views.list_clients,name='list'),
]
print(type(urlpatterns))