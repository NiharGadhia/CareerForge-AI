from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from userprofile.models import UserProfile

# Create your views here.
@login_required
def dashboard(request):

    try:
        profile = UserProfile.objects.get(user=request.user)
        profile_completed = True
    except UserProfile.DoesNotExist:
        profile = None
        profile_completed = False

    return render(request, 'dashboard.html', {
        'user': request.user,
        'profile': profile,
        'profile_completed': profile_completed
    })