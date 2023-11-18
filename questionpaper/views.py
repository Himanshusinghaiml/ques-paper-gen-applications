from django.shortcuts import render,redirect
from .models import QuestionStore
# Create your views here.
from django.contrib import messages
from django.http import JsonResponse
 
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

def get_next_question(request, current_question_id):
    try:
        next_question = QuestionStore.objects.get(id=current_question_id + 1)
    except QuestionStore.DoesNotExist:
        next_question = None
    
    if next_question:
        data = {
            'id':next_question.id,
            'question_text': next_question.question,
            'size':QuestionStore.objects.count()
        }
    else:
        data = {
            'id':'',
            'question_text': "No more questions",
            'size':QuestionStore.objects.count()
        }

    return JsonResponse(data)

def get_previous_question(request, current_question_id):
    if current_question_id > 1:
        previous_question = QuestionStore.objects.get(id=current_question_id - 1)
    else:
        previous_question = None

    if previous_question:
        data = {
            'id':previous_question.id,
            'question_text': previous_question.question,
        }
    else:
        data = {
            'id':'',
            'question_text': "No previous questions",
        }

    return JsonResponse(data)
