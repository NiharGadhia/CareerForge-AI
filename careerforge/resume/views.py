from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from google import genai
from pypdf import PdfReader
from .models import Resume
import markdown
from django.utils.html import escape
from django.utils.safestring import mark_safe

def analyze_resume_with_ai(resume):
    try:
        if not settings.GEMINI_API_KEY:
            raise ValueError("Gemini API key is not configured.")

        if not resume.extracted_text:
            raise ValueError("Resume text is missing.")

        client = genai.Client(api_key=settings.GEMINI_API_KEY)

        prompt = f"""
You are a professional resume analyst for CareerForge AI.

Analyze the resume and provide a structured report with these sections:
1. Resume Summary
2. Technical Skills
3. Soft Skills
4. Strengths
5. Skill Gaps and Skills to Improve
6. Resume Improvement Suggestions
7. Suitable Career Roles

Use bullet points under each section.
Only identify skills supported by the resume as existing skills.
Clearly label inferred gaps and suggestions.
Do not invent qualifications, experience, projects, or achievements.
If information is missing, say so.
Keep the report useful for a student or fresher.

RESUME TEXT:
{resume.extracted_text[:20000]}
"""

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        if not response.text:
            raise ValueError("Gemini returned an empty response.")

        resume.analysis_result = response.text
        resume.analysis_status = "completed"
        resume.save(
            update_fields=["analysis_result", "analysis_status"]
        )
        return True

    except Exception:
        resume.analysis_status = "failed"
        resume.save(update_fields=["analysis_status"])
        return False


@login_required
def retry_resume_analysis(request):
    if request.method != 'POST':
        return redirect('resume_analysis')

    try:
        resume = Resume.objects.get(user=request.user)
    except Resume.DoesNotExist:
        return redirect('upload_resume')

    resume.analysis_status = 'pending'
    resume.save(update_fields=['analysis_status'])

    success = analyze_resume_with_ai(resume)

    if success:
        return redirect('resume_analysis')

    return render(request, 'resume-analysis.html', {
        'resume': resume,
        'error': 'AI analysis failed. Please try again.'
    })


@login_required
def upload_resume(request):
    if request.method == 'POST':
        resume_file = request.FILES.get('resume_file')
        if not resume_file:
            return render(request, 'upload-resume.html', {
                'error': 'Please select a resume file.'
            })
        if not resume_file.name.lower().endswith('.pdf'):
            return render(request, 'upload-resume.html', {
                'error': 'Currently, only PDF resumes are supported.'
            })
        if resume_file.size > 5 * 1024 * 1024:
            return render(request, 'upload-resume.html', {
                'error': 'File size must not exceed 5 MB.'
            })
        resume, created = Resume.objects.update_or_create(
            user=request.user,
            defaults={
                'resume_file': resume_file,
                'extracted_text': '',
                'analysis_result': '',
                'analysis_status': 'pending'
            }
        )
        try:
            reader = PdfReader(resume.resume_file.path)
            text = '\n'.join(
                page.extract_text() or ''
                for page in reader.pages
            ).strip()
            if not text:
                resume.analysis_status = 'failed'
                resume.save()
                return render(request, 'upload-resume.html', {
                    'error': 'No readable text found. Please upload a text-based PDF.'
                })
            resume.extracted_text = text
            resume.save()

            success = analyze_resume_with_ai(resume)

            if not success:
                return render(request, 'upload-resume.html', {
                    'error': 'Resume was uploaded, but AI analysis failed. Please try again.'
                })
        
        except Exception:
            resume.analysis_status = 'failed'
            resume.save()
            return render(request, 'upload-resume.html', {
                'error': 'Resume was uploaded, but AI analysis failed. Please try again.'
            })
        
        return redirect('dashboard')
    return render(request, 'upload-resume.html')


@login_required
def resume_analysis(request):
    try:
        resume = Resume.objects.get(user=request.user)
    except Resume.DoesNotExist:
        return redirect('upload_resume')

    formatted_analysis = mark_safe(
        markdown.markdown(
            escape(resume.analysis_result or ""),
            extensions=[]
        )
    )

    return render(request, 'resume-analysis.html', {
        'resume': resume,
        'formatted_analysis': formatted_analysis
    })