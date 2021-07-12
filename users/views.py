from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .user_form import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            form.save()
            # Instead of getting the user and creating a profile here, we could also use signals
            # refer to users/signals.py and apps.py for how signals are being implemented
            # we are commenting out way of creating profiles
            # user1 = User.objects.filter(username=username).first()
            # p1 = Profile(user=user1, image='profile_pics/default.png')
            # p1.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form':form, "title":"User creation"})
