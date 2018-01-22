from django.http import HttpResponse
from django.views import generic
from .models import Question, Poll, Choice


class IndexView(generic.ListView):

    context_object_name = 'polls'
    queryset = Poll.objects.order_by('-pub_date')[:100]
    template_name = 'polls/index.html'

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
