from django.urls import path, include
from . views import *
from . import views
# from your_app.views import ProfileView
# from . import HodViews, StaffViews, StudentViews

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("about/", About.as_view(), name="about"),
    path('login/', loginPage.as_view(), name="login"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin/', doLogin.as_view(), name="doLogin"),
    # path('get_user_details/', get_user_details.as_view(), name="get_user_details"),
    path('logout_user/', logout_user.as_view(), name="logout_user"),

    # Profile Update
    # path('profile', views.profile, name='profile'),
    # path('profile/update', views.profile_update, name='profile_update'),
    path('profile/', ProfileView.as_view(), name='profile'),



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
