from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Resume
from pypdf import PdfReader

# Create your views here.

@login_required
def upload_resume(request):
    if request.method == 'POST':
        resume_file = request.FILES.get('resume_file')

        if resume_file:
            resume, created = Resume.objects.update_or_create(
                user=request.user,
                defaults={'resume_file': resume_file}
            )

            reader = PdfReader(resume.resume_file.path)
            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""

            resume.extracted_text = text
            resume.save()

            return redirect('dashboard')

    return render(request, 'upload-resume.html')