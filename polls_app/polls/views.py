from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Questions, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
    # ques_lis = Questions.objects.order_by('-date')[:2]
    # output = ','.join([q.ques_text for q in ques_lis])
    # return HttpResponse(output)

    ques_lis = Questions.objects.order_by('-date')[:10]
    # print(ques_lis)
    # for i in ques_lis:
    #     print(i)
    temp = loader.get_template('polls/index.html')
    ctx = {'ques_list': ques_lis}
    return HttpResponse(temp.render(ctx))

def detail(request, ques_id):
    question = get_object_or_404(Questions, pk=ques_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, ques_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response %ques_id)
    question = get_object_or_404(Questions, pk=ques_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, ques_id):
    # return HttpResponse("You're voting on question %s." %ques_id)
    question = get_object_or_404(Questions, pk=ques_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/index.html',
        {
            'question': question,
            'error_message': "Choices don't exist for this Q."
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

