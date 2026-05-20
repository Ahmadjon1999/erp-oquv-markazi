from django.contrib import admin
from django.urls import path, include  # 1. 'include' ni mana shu yerga qo'shing

urlpatterns = [
    path('admin/', admin.site.urls),

    # 2. Kurslar bilan bog'liq barcha yo'llarni courses ilovasiga yo'naltiramiz
    path('courses/', include('courses.urls')),
]