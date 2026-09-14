from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.

@login_required
def profile(request):

    # Skip profile setup
    if request.method == 'GET' and request.GET.get('skip') == '1':
        return redirect('dashboard')

    if request.method == 'POST':

        try:
            user_profile = UserProfile.objects.get(user=request.user)

            form = UserProfileForm(
                request.POST,
                instance=user_profile
            )

        except UserProfile.DoesNotExist:

            form = UserProfileForm(request.POST)

        if form.is_valid():

            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('dashboard')

    else:

        try:
            user_profile = UserProfile.objects.get(
                user=request.user
            )

            form = UserProfileForm(
                instance=user_profile
            )

        except UserProfile.DoesNotExist:

            form = UserProfileForm()

    return render(request, 'profile.html', {
        'form': form
    })