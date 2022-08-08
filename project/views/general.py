"""Обшее"""
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from project.decorators import unauthenticated_user
from project.forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from project.models import Student
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

@unauthenticated_user
def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=User.objects.create_user(username=username, password=password)
            group = Group.objects.get(name='student')
            user.groups.add(group)
            user.save()
            
            Student.objects.create(
                user=user,
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'general/register.html', {'form':  form})

# @unauthenticated_user
# def registerPage(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user=User.objects.create_user(username=username, password=password)
#             group = Group.objects.get(name='student')
#             user.groups.add(group)
#             user.save()

#             Student.objects.create(
#                 user=user,

#             )
#             messages.success(request, 'Account was created for ' + username)
#             return redirect('login')
#     else:
#         form = CreateUserForm()
#     context = {'form': form}
#     return render(request, 'general/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.groups.all()[0].name == 'admin':
                return redirect('admin_page')
            elif request.user.groups.all()[0].name == 'student' :
                return redirect('student_page')
            else:
                return HttpResponse('Aut of roles')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'general/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

