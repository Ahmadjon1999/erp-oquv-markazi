from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_teacher = models.BooleanField(verbose_name="Foydalanuvchi roli",default=False)


class StudentProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name="Tel raqam", max_length=13)
    bio = models.TextField(verbose_name="Tarjimayu hol",blank=True)
    avatar = models.ImageField(verbose_name="Profil rasim", upload_to="avatars/",blank=True,null=True)


    def __str__(self):
        return f"O'quvchi: {self.user.username}"
    

    @property
    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return '/static/css/default-avatar.png'
    

class TeacherProfile(models.Model):
    user = models.OneToOneField(to=User, related_name='teacher_profile', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,verbose_name="Mutaxassislik fani")
    experience = models.IntegerField(verbose_name="O'qituvchi staji", default=0)


    def __str__(self):
        return f"O'qituvchi: {self.user.username}"
    
















