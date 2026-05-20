from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import TeacherProfile, StudentProfile

# 1. Ro'yxatdan o'tish logikasi
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get('password')
            user.set_password(raw_password)
            user.save()

            if user.is_teacher:
                TeacherProfile.objects.create(user=user, subject="Belgilanmagan")
            else:
                StudentProfile.objects.create(user=user)

            login(request, user)
            return redirect('home')  # Mana shu nomli URLga jo'natadi
    else:
        form = RegisterForm()
        
    return render(request, 'accounts/register.html', {'form': form})


# 2. Siz aytgan Bosh sahifa logikasi (Sizning kodingiz!)
def home_view(request):
    return render(request, 'accounts/home.html')
























