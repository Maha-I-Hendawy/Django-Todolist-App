from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def index(request):
	users = User.objects.all()
	context = {
	'users': users
	}
	return render(request, 'users/index.html', context)



def adduser(request):
	form = UserForm()
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			confirm_password = form.cleaned_data["confirm_password"]
			if password == confirm_password:
				hashed_password = make_password(password)
				user = User(username=username, email=email, password=hashed_password)
				user.save()
				return redirect('/users')
	context = {
	'form': form
	}
	return render(request, 'users/adduser.html', context)




def login(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]

			user = User.objects.filter(username=username).first()
			if user and user.check_password(password):
				request.session["user_id"] = user.id
				request.session["username"] = user.username
				

				

	context = {

	  'form': form
	}

	return render(request, 'users/login.html', context)



def profile(request):
	return render(request, 'users/profile.html')
