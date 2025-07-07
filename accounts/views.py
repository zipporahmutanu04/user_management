
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistrationForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            # Mock email verification
            user.profile.is_verified = True
            user.profile.save()
            login(request, user)
            messages.success(request, 'Registration successful! Your account is verified.')
            return redirect('verify_email')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def verify_email(request):
    return render(request, 'registration/verify_email.html')
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/edit_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully.')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'profile/change_password.html', {'form': form})