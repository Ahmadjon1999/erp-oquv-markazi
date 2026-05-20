from django.contrib import admin
from .models import Assignment, Submission, Grade


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline']
    list_filter = ['deadline']
    search_fields = ['title', 'description']
    ordering = ['-deadline']


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student', 'submitted_at']
    list_filter = ['submitted_at', 'assignment']
    search_fields = ['student__username', 'assignment__title']
    date_hierarchy = 'submitted_at'


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['submission', 'score', 'graded_at']
    list_filter = ['score', 'graded_at']
    search_fields = ['submission__student__username', 'submission__assignment__title']
    raw_id_fields = ['submission']