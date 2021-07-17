from django import forms
from django.shortcuts import render, HttpResponse
from polls.models import Voter
from polls.forms import register_form, UserForm, UserProfileInfoForm
# Create your views here.
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


@login_required
def employee_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('voter_list:login_employee'))


@login_required
def get_users(request):
    users = Voter.objects.all()
    dct = {'all_users': users, 'block': range(4)}
    return render(request, "get_users.html", context=dct)


@login_required
def user_register(request):
    f = register_form()

    if request.method == 'POST':
        f = register_form(request.POST)
        if f.is_valid():
            f.save()
            a = get_users(request)
            return a
    dct = {'f': f}
    return render(request, "register_user.html", context=dct)


def help(request):
    return render(request, "help.html", context={'email': 'kroy@gmail.com', 'phone': '9999999999'})


def index(request):
    return render(request, "help.html", context={'email': 'kroy@gmail.com', 'phone': '99999999999'})


@login_required
def register_employee(request):
    registerd = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registerd = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    dct = {'registered': registerd, 'user_form': user_form, 'profile_form': profile_form}
    return render(request, "registration.html", context=dct)


def login_employee(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('voter_list:get_users'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
        else:

            print("SomeOne Tried to login and Failed")
            print(username, password)
            return HttpResponse("invalid Password/Username")


    else:
        return render(request, "login_me.html", {})
