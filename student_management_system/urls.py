"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from student_management_system import settings

urlpatterns = [
    path('', include('student_management_app.urls')),
    path('', include('HOD_app.urls')),
    path('', include('Staff_app.urls')),
    # path('', include('Students_app.urls')),
    path("admin/", admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)















# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
#
# from .import views
# from . views import *
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('', include('student_management_app.urls')),
#     path('base/', views.Base, name='base'),
#     # path('', include('HOD_app.urls')),
#     # path('', include('Staff_app.urls')),
#     # path('', include('Student_app.urls')),
#     # path('', include('verification.urls'), name="verification")
#
#     # Login Path
#     path('Login', loginPage.as_view(), name="Login"),
#     path('doLogin/', doLogin.as_view(), name="doLogin"),
#
# ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
