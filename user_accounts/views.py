from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			return redirect('blog-home')
	else:
		form = UserRegisterForm()

	data = {
			'form': form,
	}
	return render(request, 'user_accounts/register.html', data)


@login_required
def profile(request):
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST,
										request.FILES,
										instance=request.user.profile)

		if user_form.is_valid and profile_form.is_valid:
			user_form.save()
			profile_form.save()
			
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

	data = {
		'user_form': user_form,
		'profile_form': profile_form,
	}

	return render(request, 'user_accounts/profile.html', data)
