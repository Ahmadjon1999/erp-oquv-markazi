from django.urls import path
from . import views



urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('<int:pk>/submit/', views.submit_assignment, name='submit_assignment'),
    path('submissions/<int:pk>/grade/', views.grade_submission, name='grade_submission'),
]