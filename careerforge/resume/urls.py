from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),
    path('analysis/', views.resume_analysis, name='resume_analysis'),
    path('retry-analysis/', views.retry_resume_analysis, name='retry_resume_analysis'),
]