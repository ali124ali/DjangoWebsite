from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from accounts.forms import CustomUserCreationForm

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')
                
        form = AuthenticationForm()
        content = {"form" : form}    

        return render(request, 'accounts/login.html', content)
    
    else:
        return redirect('/')
            

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('accounts:login')

        form = CustomUserCreationForm()
        content = {"form" : form}
        return render(request, 'accounts/signup.html', content)
    
    else:
        return redirect('/')

@login_required
def change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                # message
                logout(request)
                return redirect('accounts:login')
            
            else:
                # message
                return redirect('accounts:change')
            
        form = PasswordChangeForm(request)
        content = {'form' : form}
        
        return render(request, 'accounts/change_password.html', content)

    else:
        return redirect('/')
