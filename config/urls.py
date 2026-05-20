from django.urls import path, include
from django.contrib import admin
from assignments.views import home_view  



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home'),  # Bosh sahifa yo'li
    path('assignments/', include('assignments.urls')),
    # path('courses/', include('courses.urls')), # buni vaqtincha ochirib turgan edik
]