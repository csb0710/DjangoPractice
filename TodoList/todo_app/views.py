from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Todo, Date
from django.urls import reverse
from .forms import TodoForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    author = request.user
    dates = Date.objects.filter(author = author).exclude(strdate = timezone.now().strftime("%Y-%m-%d"))
    dates = dates.order_by('-strdate')
    
    return render(
        request,
        'todo/index.html',
        {
            'dates' : dates,
        }
    )

@login_required
def todo_list(request, date):
    author = request.user
    todos = Todo.objects.filter(author = author).filter(completed = False).filter(str_date = date)
    todosc = Todo.objects.filter(author = author).filter(completed = True).filter(str_date = date)
    
    return render(
        request,
        'todo/todo_list.html',
        {
            'todos' : todos,
            'todosc' : todosc
        }
    )

@login_required
def todo_today(request):
    author = request.user
    dates = Date.objects.filter(author = author).filter(strdate = timezone.now().strftime("%Y-%m-%d"))
    
    if(len(dates) == 0):
        new_date = Date()
        new_date.author = request.user
        new_date.save()
    
    todos = Todo.objects.filter(author = author).filter(completed = False).filter(str_date = timezone.now().strftime("%Y-%m-%d"))
    todosc = Todo.objects.filter(author = author).filter(completed = True).filter(str_date = timezone.now().strftime("%Y-%m-%d"))
    
    return render(
        request,
        'todo/todo_today.html',
        {
            'todos' : todos,
            'todosc' : todosc
        }
    )
 

@login_required
def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    
    return render(request, 'todo/todo_detail.html', {'todo' : todo})

@login_required
def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    
    todo.delete()
    
    previous_page = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(previous_page)

@login_required
def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('/todo/today')
    else:
        form = TodoForm()
    
    return render(request, 'todo/todo_post.html', {'form': form})

@login_required
def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('/todo/today')
    else:
        form = TodoForm(instance=todo)
    
    return render(request, 'todo/todo_post.html', {'form': form})

@login_required
def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    if(todo.completed == False) :
        todo.completed = True    
    else :
        todo.completed = False
        
    todo.save()
    
    previous_page = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(previous_page)

