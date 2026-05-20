from django.contrib import admin
from .models import Category, Course, Lesson, Enrollment, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'price', 'category', 'created_at']
    list_display_links = ['title']
    list_filter = ['category', 'created_at', 'teacher']
    search_fields = ['title', 'description']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    list_display_links = ['title']
    list_filter = ['course']
    search_fields = ['title']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'enrolled_at']
    list_display_links = ['student']
    list_filter = ['course', 'enrolled_at']
    search_fields = ['student__username', 'course__title']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'rating', 'comment']
    list_display_links = ['course']
    list_filter = ['rating', 'course']
    search_fields = ['comment', 'student__username', 'course__title']