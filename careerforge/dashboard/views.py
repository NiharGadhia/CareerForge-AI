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

    # Check resume analysis status
    resume_analysis_completed = (
        resume_uploaded
        and resume.analysis_status == 'completed'
        and bool(resume.analysis_result)
    )

    # Check skill gap analysis status
    skill_gap_completed = (
        resume_uploaded
        and bool(resume.skill_gap_result)
    )

    # Check career insights status
    career_insights_completed = (
        resume_uploaded
        and bool(resume.career_recommendations_result)
        and bool(resume.institute_recommendations_result)
    )

    # Career Journey steps
    journey = [
        {
            'title': 'Build Profile',
            'description': 'Education & interests',
            'completed': profile_completed,
        },
        {
            'title': 'Analyze Resume',
            'description': 'Skills & experience',
            'completed': (
                resume_analysis_completed and skill_gap_completed
            ),
        },
        {
            'title': 'Career Insights',
            'description': 'AI recommendations',
            'completed': career_insights_completed,
        },
        {
            'title': 'Learning Roadmap',
            'description': 'Build your future',
            'completed': False,
        },
    ]

    # Set completed, active and pending states
    active_found = False

    for step in journey:
        if step['completed']:
            step['state'] = 'completed'
        elif not active_found:
            step['state'] = 'active'
            active_found = True
        else:
            step['state'] = 'pending'

    return render(request, 'dashboard.html', {
        'user': request.user,
        'profile': profile,
        'profile_completed': profile_completed,
        'resume': resume,
        'resume_uploaded': resume_uploaded,
        'journey': journey,
    })