from django.urls import path
from . import views

urlpatterns =[
path('shooter', views.shooter_list, name='shooter_list'),
path('rogelite', views.rogelite_list, name='rogelite_list'),
path('soulslike', views.soulslike_list, name='soulslike_list'),
]