from django.urls import path
from questionpaper import views
urlpatterns=[
    path('',views.add_question,name="add_questions"),
    path('question-generator/',views.generator,name="generator"),
]