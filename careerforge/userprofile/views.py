from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.

@login_required
def profile(request):

    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = UserProfileForm(
            request.POST,
            instance=user_profile
        )

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('upload_resume')

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {
        'form': form
    })