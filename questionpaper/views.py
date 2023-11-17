from django.shortcuts import render,redirect
from .models import QuestionStore
# Create your views here.
from django.contrib import messages
 
def add_question(request):
    if request.method == 'POST':
        # Get the input from the request
        question_text = request.POST.get('question')
        subject = request.POST.get('subject')
        topic = request.POST.get('topic')
        difficulty = request.POST.get('difficulty')
        marks = request.POST.get('marks')

        # Create and save a new question
        QuestionStore.objects.create(
            question=question_text,
            subject=subject,
            topic=topic,
            difficulty=difficulty,
            marks=marks
        )
        messages.success(request, 'Question saved successfully in database !')
        return redirect('add_questions')  # Redirect to the question paper page

    return render(request, 'index.html')
def generator(req):
    return render(req,'ques_gen.html')