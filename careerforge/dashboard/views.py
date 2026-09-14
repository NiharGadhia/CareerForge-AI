from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from userprofile.models import UserProfile
from resume.models import Resume

# Create your views here.
@login_required
def dashboard(request):

    try:
        profile = UserProfile.objects.get(user=request.user)
        profile_completed = True
    except UserProfile.DoesNotExist:
        profile = None
        profile_completed = False

    try:
        resume = Resume.objects.get(user=request.user)
        resume_uploaded = True
    except Resume.DoesNotExist:
        resume = None
        resume_uploaded = False

    return render(request, 'dashboard.html', {
        'user': request.user,
        'profile': profile,
        'profile_completed': profile_completed,
        'resume': resume,
        'resume_uploaded': resume_uploaded
    })