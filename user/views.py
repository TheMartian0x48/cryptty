import user
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateFrom

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}')
      return redirect('front')
  else:
    form = UserRegistrationForm()
  return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
  return render(request, 'user/profile.html')

@login_required
def profile_update(request):
  # print(request.user.profile.image.url)
  if request.method == 'POST':
    user_form = UserUpdateForm(request.POST, instance=request.user)
    profile_form = ProfileUpdateFrom(
      request.POST, 
      request.FILES,
      instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      return redirect('profile')
  else:
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateFrom(instance=request.user.profile)
  context = {
    'user_form' : user_form,
    'profile_form' : profile_form
  }
  return render(request, 'user/profile_update.html', context)