from django.contrib import admin
from django.urls import path, include  # 1. 'include' ni mana shu yerga qo'shin
from assignments.views import home_view  



urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include("accounts.urls")),
    

    # 2. Kurslar bilan bog'liq barcha yo'llarni courses ilovasiga yo'naltiramiz
    path('courses/', include('courses.urls')),
    path('', home_view, name='home'),  # Bosh sahifa yo'li
    path('assignments/', include('assignments.urls')),
    # path('courses/', include('courses.urls')), # buni vaqtincha ochirib turgan edik
]




