from django.db import models
from django.conf import settings

# Create your models here.
class Resume(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='resume'
    )
    resume_file = models.FileField(upload_to='resumes/')
    extracted_text = models.TextField(blank=True, null=True)
    analysis_result = models.TextField(blank=True, null=True)
    analysis_status = models.CharField(max_length=20, default='pending')
    skill_gap_result = models.TextField(blank=True, null=True)
    career_recommendations_result = models.TextField(blank=True, null=True)
    institute_recommendations_result = models.TextField(blank=True, null=True)
    learning_roadmap_result = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'resumes'

    def __str__(self):
        return f"{self.user.username} Resume"