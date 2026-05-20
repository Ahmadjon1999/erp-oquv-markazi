from django.db import models
from django.conf import settings

class Assignment(models.Model):
    # lesson = models.ForeignKey('courses.Lesson', on_delete=models.CASCADE)  # Vaqtincha yopamiz
    lesson_name = models.CharField(max_length=200, blank=True)  # Vaqtincha oddiy matn qilamiz
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/', blank=True)
    text = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['assignment', 'student']

class Grade(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
    score = models.IntegerField()
    feedback = models.TextField(blank=True)
    graded_at = models.DateTimeField(auto_now_add=True)