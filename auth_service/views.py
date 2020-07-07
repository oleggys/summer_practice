from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.


def registration_view(request):
    """
    View which return page with registration form.
    If the submitted form is valid then person will log in automatically
    :param request:
    :return:
    """
    args = {}
    if request.POST:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'],
                         password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    args['form'] = form
    return render(request, 'auth_service/registration_page.html', args)


def login_view(request):
    """
    View, which return page with login form
    :param request:
    :return:
    """
    args = {}
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    args['form'] = form
    return render(request, 'auth_service/login_page.html', args)


@login_required
def logout_view(request):
    """
    View for logout
    :param request:
    :return:
    """
    logout(request)
    return redirect('/')
