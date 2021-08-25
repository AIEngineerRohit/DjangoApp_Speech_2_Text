from django.urls import path
from . import views


urlpatterns = [

path('',views.index),
path('index/speech',views.speech,name="script"),
path('external/',views.external),

]