from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Enrollment


# (Agar kurs yaratish uchun Form ishlatsangiz, uni ham import qilasiz)

# 1. /courses/ - Kurslar ro'yxati (Hamma ko'radi)
def course_list(request):
    courses = Course.objects.all()
    data = {'courses': courses}
    return render(request, 'courses/course_list.html', context=data)


# 2. /courses/id/ - Kurs batafsil (Hamma ko'radi)
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    # Kurs ichidagi darslarni ham sahifaga yuboramiz
    lessons = Lesson.objects.filter(course=course)
    context = {
        'course': course,
        'lessons': lessons
    }
    return render(request, 'courses/course_detail.html', context)


# 3. /courses/create/ - Kurs yaratish (Faqat o'qituvchi)
def course_create(request):
    # Oddiy mantiq 1: Login qilganmi?
    if not request.user.is_authenticated:
        return redirect('login')

    # Oddiy mantiq 2: O'qituvchimi? (Sherigingiz User modeliga is_teacher qo'shgan bo'lishi kerak)
    # Agar is_teacher bo'lmasa, uni bosh sahifaga qaytaramiz
    if not getattr(request.user, 'is_teacher', False):
        return redirect('course_list')

    if request.method == 'POST':
        # Kursni saqlash kodi shu yerda bo'ladi...
        pass

    return render(request, 'courses/course_form.html')


# 4. /courses/id/enroll/ - Kursga yozilish (Faqat login qilganlar)
def enroll_course(request, pk):
    # Oddiy mantiq: Login qilmagan bo'lsa, ro'yxatdan o'tishga haydaymiz
    if not request.user.is_authenticated:
        return redirect('login')

    course = get_object_or_404(Course, pk=pk)
    # get_or_create — agar oldin yozilmagan bo'lsa, yangi qator ochadi
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('my_courses')


# 5. /my-courses/ - O'z kurslari (Faqat o'quvchi)
def my_courses(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Faqat shu o'quvchi yozilgan kurslarni bazadan qidiramiz
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})


# 6. /lessons/id/ - Dars ko'rish (Faqat shu kursga yozilgan o'quvchi)
def lesson_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    lesson = get_object_or_404(Lesson, pk=pk)

    # Eng muhim xavfsizlik mantig'i: O'quvchi shu dars tegishli bo'lgan kursga yozilganmi?
    is_enrolled = Enrollment.objects.filter(student=request.user, course=lesson.course).exists()

    # Agar yozilmagan bo'lsa va bu kursning o'qituvchisi ham bo'lmasa, darsni ko'rsatmaymiz!
    if not is_enrolled and lesson.course.teacher != request.user:
        return redirect('course_detail', pk=lesson.course.pk)

    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})