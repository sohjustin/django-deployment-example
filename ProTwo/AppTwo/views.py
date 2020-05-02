from django.shortcuts import render
from AppTwo.models import UserInfo, SignIn
from AppTwo.forms import NewUser, UserForm, UsesrProfileInfoForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def main_page(request):
    my_dict = {'Help': "Help Page"}
    return render(request, "AppTwo/main_page.html", context = my_dict)


def users_info_page(request):
    users_content = UserInfo.objects.all()
    users_dict = {'users': users_content}
    return render(request, 'AppTwo/users_info_page.html', context = users_dict)

def users_page(request):
    users_content = User.objects.all()
    users_dict = {'users': users_content}
    return render(request, 'AppTwo/users_page.html', context = users_dict)

def sign_in_page(request):

    sign_in_form = NewUser()

    if request.method == 'POST':
        sign_in_form = NewUser(request.POST)

        if sign_in_form.is_valid():
            sign_in_form.save(commit = True)
            return main_page(request)

        else:
            print("Error. Form Invalid")

    return render(request, 'AppTwo/sign_in_page.html', {'sign_in_form': sign_in_form})


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UsesrProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UsesrProfileInfoForm()

    return render(request, 'AppTwo/registration.html',
                    {'registered': registered,
                    'user_form':user_form,
                    'profile_form':profile_form})


def user_login(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main'))

            else:
                return HttpResponse("Account not active")

        else:
            print("Someone tried to login and failed!")
            print("Username: " + username + " and password: " + password)
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, 'AppTwo/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))

@login_required
def special(request):
    return render(request, 'AppTwo/special.html', {'special': "You have successfully logged in!"})
