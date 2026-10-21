from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),
    path('analysis/', views.resume_analysis, name='resume_analysis'),
    path('retry-analysis/', views.retry_resume_analysis, name='retry_resume_analysis'),
    path('skill-gap/', views.skill_gap_analysis, name='skill_gap_analysis'),
    path('career-recommendations/', views.career_recommendations, name='career_recommendations'),
    path('institute-recommendations/', views.institute_recommendations, name='institute_recommendations'),
    path('learning-roadmap/', views.learning_roadmap, name='learning_roadmap'),
]