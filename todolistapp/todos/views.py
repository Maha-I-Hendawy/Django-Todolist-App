from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def home(request):
	form = TodoForm()
	if(request.method == 'POST'):
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.cleaned_data['todo']
			completed = form.cleaned_data['completed']
			#print(todo, completed)
			mytodo = Todo(todo=todo, complated=completed)
			mytodo.save()
			return redirect('/')

	todos = Todo.objects.all()

	context = {
	  'form': form,
	  'todos': todos
	}
	return render(request, 'todos/home.html', context)



def update(request, id):
	todo = Todo.objects.get(pk=id)
	form = TodoForm(initial={'todo': todo.todo, 'completed': todo.complated})
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			todo.todo = form.cleaned_data['todo']
			todo.complated = form.cleaned_data['completed']
			todo.save()
			return redirect('/')
    	

	context = {
	  'form': form,
	  'todo': todo
	}
	return render(request, 'todos/update.html', context)



def delete(request, id):
	todo = Todo.objects.get(pk=id)
	todo.delete()
	return redirect('/')
