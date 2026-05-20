from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Assignment, Submission, Grade
from .forms import SubmissionForm, GradeForm



# @login_required
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})


# @login_required
def submit_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.student = request.user
            sub.assignment = assignment
            sub.save()
            return redirect('my_grades')
    else:
        form = SubmissionForm()
    return render(request, 'assignments/submit.html', {'form': form})

# @login_required
def grade_submission(request, pk):
    if not request.user.is_teacher:
        return redirect('home')
    submission = get_object_or_404(Submission, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.submission = submission
            grade.save()
            return redirect('assignment_list')
    else:
        form = GradeForm()
    return render(request, 'assignments/grade.html', {'form': form})