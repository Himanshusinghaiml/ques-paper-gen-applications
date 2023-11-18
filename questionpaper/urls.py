from django.urls import path
from questionpaper import views
urlpatterns=[
    path('',views.add_question,name="add_questions"),
    path('question-generator/',views.generator,name="generator"),
    path('get_next_question/<int:current_question_id>/', views.get_next_question, name='get_next_question'),
    path('get_previous_question/<int:current_question_id>/', views.get_previous_question, name='get_previous_question'),
]