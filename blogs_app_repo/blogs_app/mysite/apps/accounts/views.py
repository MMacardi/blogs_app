from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import Http404, HttpResponseRedirect, HttpResponse

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('articles:articles_home')
    else:
        if request.method == 'POST': # if you want to make new user
            form = UserSignupForm(request.POST) # sending request to server
            if form.is_valid(): # if username is free, etc.
                username = form.cleaned_data.get('username').capitalize()
                messages.success(request, f'Account created for {username}! Now you able to login')
                user = form.save()#.capitalize() # save on server
                return redirect('login')
        else:
            form = UserSignupForm() # just returning to current page
        return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('articles:articles_home')
    else:
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = AuthenticationForm(data=request.POST) # what you fill
            if form.is_valid(): # if passwords are matching, etc.
                user = form.get_user()
                username = form.cleaned_data.get('username').capitalize()
                messages.success(request, 'You are logged in.')
                login(request, user) # log the user in
                if 'next' in request.POST: # if have ?next=
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('articles:articles_home') # if no ?next=

        else:
            form = AuthenticationForm() # just returning to current page
        return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile_settings(request):
    context_object_name = 'profile'
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile_settings')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile_settings.html', context)