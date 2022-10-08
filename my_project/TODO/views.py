from django.shortcuts import render
from. models import Todo

# Create your views here.
def index(request):
    todo_lost=Todo.objects.order_by('id')

    context = {'todo_list':todo_lost}

    return render(request, 'todo/index.html', context)

