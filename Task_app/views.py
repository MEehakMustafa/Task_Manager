from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import task
from .forms import TaskForm
from django.contrib.auth import logout as auth_logout


# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        tasks = task.objects.filter(user=request.user) 
        return render(request, 'homepage.html', {'tasks': tasks})
    else:
        return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                new_user = User.objects.create_user(username=username, password=password)
                new_user.save()
                messages.success(request, 'Account created successfully. You can now login.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

    return render(request, 'signup.html')
   

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect back to the login page
    return render(request, 'login.html')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Create a new task object with the form data
            new_task = form.save(commit=False)
            new_task.user = request.user  # Assign the current user to the task
            new_task.save()
            return redirect('homepage')  # Redirect to the homepage after adding the task
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def update_task_status(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_id')
        for task_id in task_ids:
            task_object = task.objects.get(pk=task_id)  # Change the variable name
            # Toggle the is_done status of the task
            task_object.is_done = not task_object.is_done
            task_object.save()
        return redirect('homepage')  # Assuming 'home' is the name of your home page URL pattern
    else:
        return redirect('homepage')  # Redirect to home page if accessed via GET request
def logout(request):
    auth_logout(request)  # Logout the user
    return redirect('login')  # Redirect to the homepage after logout
    

