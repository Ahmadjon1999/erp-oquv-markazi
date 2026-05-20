from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(verbose_name="Kategorya nomi", max_length=100)

    class Meta:
        verbose_name = 'Kategorya'
        verbose_name_plural = 'Kategoryalar'

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(verbose_name="Kurs nomi", max_length=200)
    price = models.DecimalField(verbose_name="Narxi", max_digits=12, decimal_places=2)
    description = models.TextField(verbose_name="Kurs haqida ma'lumot")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Ustoz")

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name="Kurs nomi")
    title = models.CharField(verbose_name="Dars nomi", max_length=200)
    video = models.FileField(verbose_name="Video", upload_to='lessons/videos/')
    order = models.IntegerField(verbose_name="Darslar tartib raqami")

    class Meta:
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="O'quvchi")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Kurs nomi")
    enrolled_at = models.DateTimeField(auto_now_add=True,verbose_name="Yozilgan vaqti")

    class Meta:
        unique_together = ['student', 'course']
        verbose_name = "Kursga yozilish"
        verbose_name_plural = "Kursga yozilishlar"

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Kurs nomi")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="O'quvchi")
    rating = models.IntegerField(verbose_name="Baho (1-5)")
    comment = models.TextField(verbose_name="Izoh")

    class Meta:
        unique_together = ['course', 'student']
        verbose_name = "Fikr-mulohaza"
        verbose_name_plural = "Fikr-mulohazalar"

    def __str__(self):
        return f"{self.student.username} - {self.course.title} ({self.rating})"














