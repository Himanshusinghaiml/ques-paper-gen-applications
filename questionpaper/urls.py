from django.urls import path
from questionpaper import views
urlpatterns=[
    path('',views.index,name="index")
]