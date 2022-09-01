from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newpath/', views.addrecord, name='index1')
    # path('', views.s)
]