from django.shortcuts import render

# Create your views here.

def upload_resume(request):
    return render(request, 'upload-resume.html')