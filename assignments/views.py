from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Assignment, Submission, Grade
from .forms import SubmissionForm, GradeForm


def home_view(request):
    return render(request, 'home.html')


def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})



@login_required
def submit_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    submission = Submission.objects.filter(assignment=assignment, student=request.user).first()
    
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES, instance=submission)
        if form.is_valid():
            new_sub = form.save(commit=False)
            new_sub.assignment = assignment
            new_sub.student = request.user
            new_sub.save()
            return redirect('assignment_list')
    else:
        form = SubmissionForm(instance=submission)
    
    return render(request, 'assignments/submit.html', {'form': form, 'assignment': assignment})



@login_required
def grade_submission(request, pk):
    if not (request.user.is_staff or request.user.groups.filter(name='Teachers').exists()):
        raise PermissionDenied
        
    submission = get_object_or_404(Submission, pk=pk)
    grade = getattr(submission, 'grade', None)
    
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            new_grade = form.save(commit=False)
            new_grade.submission = submission
            new_grade.grader = request.user
            new_grade.save()
            return redirect('assignment_list')
    else:
        form = GradeForm(instance=grade)
        
    return render(request, 'assignments/grade.html', {'form': form, 'submission': submission})