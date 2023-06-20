from django.urls import path, include
from . views import *
from . import views
# from . import HodViews, StaffViews, StudentViews

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("about/", About.as_view(), name="about"),
    path('login/', loginPage.as_view(), name="login"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin/', doLogin.as_view(), name="doLogin"),
    # path('get_user_details/', get_user_details.as_view(), name="get_user_details"),
    path('logout_user/', logout_user.as_view(), name="logout_user"),
]











# from django.urls import path, include
# from .views import *
# # from .views import UserRegistrationView, UserLoginView, UserLogoutView
#
# urlpatterns = [
#     path("", Home.as_view(), name="Home"),
#     # path("register/", UserRegistrationView.as_view(), name="register"),
#     # path("login/", UserLoginView.as_view(), name="login"),
#     # path("logout/", UserLogoutView.as_view(), name="logout"),
#     path("about/", About.as_view(), name="about"),
# ]
