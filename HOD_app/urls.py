from django.urls import path
from .views import *

app_name = 'HOD_app'

urlpatterns = [
    path('Hod/Home', AdminHomeView.as_view(), name="hod_home"),

]