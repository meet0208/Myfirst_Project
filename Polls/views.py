from datetime import date
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
    
def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def create(request):
    
    return render(request, 'polls/create.html')

'''def save(request,question_id):
     if request.method=="POST":
        question = request.POST['question']
        option1 = request.POST['choice1']
        option2 = request.POST['choice2']
        option3 = request.POST['choice3']
        option4 = request.POST['choice4']

        q=Question(question_text=question,pub_date=date.today())
        q.save()
        o=Choice(question=get_object_or_404(Question, pk=question_id),choice_text=option1) 
        o.save()   

        return render(request, 'polls/index.html')'''