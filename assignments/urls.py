from django.urls import path
from . import views



urlpatterns = [
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/<int:pk>/submit/', views.submit_assignment, name='submit_assignment'),
    path('submissions/<int:pk>/grade/', views.grade_submission, name='grade_submission'),
]