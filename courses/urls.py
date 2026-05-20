from django.urls import path
from . import views

urlpatterns = [
    # 1. Barcha kurslar ro'yxati sahifasi (Masalan: /courses/)
    # Saytga kirgan hamma (login qilgan-qilmaganidan qat'i nazar) kurslar ro'yxatini ko'ra oladi.
    path('', views.course_list, name='course_list'),

    # 2. Bitta kurs haqida batafsil ma'lumot sahifasi (Masalan: /courses/3/)
    # <int:pk> — bu o'sha kursning bazadagi ID raqami. Shu ID orqali tanlangan kurs, uning ta'rifi va darslar ro'yxati ko'rinadi.
    path('<int:pk>/', views.course_detail, name='course_detail'),

    # 3. Yangi kurs yaratish sahifasi (Masalan: /courses/create/)
    # Faqat o'qituvchi rolidagi foydalanuvchilar kirib, yangi kurs shakllantirishi (nomi, narxi, ma'lumotlarini yozishi) uchun.
    path('create/', views.course_create, name='course_create'),

    # 4. Kursga yozilish (obuna bo'lish) tugmasi / mantiqiy yo'li (Masalan: /courses/3/enroll/)
    # Foydalanuvchi "Kursga yozilish" tugmasini bossa, shu yo'l ishga tushadi, uni bazaga o'quvchi qilib qo'shadi va ortga qaytaradi (O'zi sahifa emas, mantiqiy jarayon).
    path('<int:pk>/enroll/', views.enroll_course, name='enroll'),

    # 5. O'quvchining shaxsiy kurslari sahifasi (Masalan: /courses/my-courses/)
    # Faqat login qilgan o'quvchi o'zi sotib olgan yoki yozilgan kurslarini bitta joyda jamlangan holda ko'rishi uchun.
    path('my-courses/', views.my_courses, name='my_courses'),

    # 6. Kurs ichidagi darsni ko'rish (video darslik) sahifasi (Masalan: /courses/lessons/12/)
    # <int:pk> — darsning ID raqami. Faqat shu kursga a'zo bo'lgan o'quvchigagina video va dars materiallarini ko'rishga ruxsat beriladi.
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'),
]