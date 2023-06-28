from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, LoginForm
from student_management_app.EmailBackEnd import EmailBackEnd
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser




class Home(View):
    def get(self, request):
        return render(request, "home.html")

class About(View):
    def get(self, request):
        return render(request, "about.html")

class Base(View):
    def get(self, request):
        return render(request, "base.html")

# def Base(request):
#     return render(request, 'base.html')

class loginPage(View):
    def get(self, request):
        return render(request, 'login.html')

class doLogin(View):
    def get(self, request):
        return HttpResponse("<h2>Method Not Allowed</h2>")

    def post(self, request):
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        print(user)
        if user:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                # return HttpResponse("HOD Login")
                return redirect('HOD_app:hod_home')
            elif user_type == '2':
                return HttpResponse("Staff Login")
                # return redirect('staff_home')
            elif user_type == '3':
                return HttpResponse("Student Login")
                # return redirect('student_home')

        messages.error(request, "Invalid Login Credentials!")
        return redirect('login')



# class doLogin(View):
#     def post(self, request):
#         if request.method != "POST":
#             return HttpResponse("<h2>Method Not Allowed</h2>")
#
#         user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
#         print(user)
#         if user:
#             login(request, user)
#             user_type = user.user_type
#             if user_type == '1':
#                 # return HttpResponse("HOD Login")
#                 return redirect('HOD_app:hod_home')
#             elif user_type == '2':
#                 return HttpResponse("Staff Login")
#                 # return redirect('staff_home')
#             elif user_type == '3':
#                 return HttpResponse("Student Login")
#                 # return redirect('student_home')
#
#         messages.error(request, "Invalid Login Credentials!")
#         return redirect('login')



class logout_user(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

class ProfileView(View):
    @staticmethod
    @login_required(login_url='login')
    def get(request):
        user = CustomUser.objects.get(id=request.user.id)
        context = {
            "user": user,
        }
        return render(request, 'profile.html', context)

    @staticmethod
    @login_required(login_url='login')
    def post(request):
        if request.method == "POST":
            profile_pic = request.FILES.get('profile_pic')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')

            try:
                customuser = CustomUser.objects.get(id=request.user.id)
                customuser.first_name = first_name
                customuser.last_name = last_name
                # customuser.profile_pic = profile_pic

                if password != None and password != "":
                    customuser.set_password(password)
                if profile_pic != None and profile_pic != "":
                    customuser.profile_pic = profile_pic
                customuser.save()
                messages.success(request, "Your Profile Updated Successfully !")
                return redirect('profile')
            except:
                messages.error(request, "Failed To Update Your Profile")

        return render(request, 'profile.html')






# @login_required(login_url='login')
# def profile(request):
#     user = CustomUser.objects.get(id=request.user.id)
#
#
#     context = {
#         "user" : user,
#     }
#     return render(request, 'profile.html', context)
#
# @login_required(login_url='login')
# def profile_update(request):
#     if request.method == "POST":
#         profile_pic = request.FILES.get('profile_pic')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         # email = request.POST.get('email')
#         # username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         try:
#             customuser = CustomUser.objects.get(id=request.user.id)
#             customuser.first_name = first_name
#             customuser.last_name = last_name
#
#             if password != None and password != "":
#                 customuser.set_password(password)
#             if profile_pic != None and profile_pic != "":
#                 customuser.profile_pic = profile_pic
#             customuser.save()
#             customuser.success(request, "Your Profile Updated Successfully !")
#             redirect('profile')
#         except:
#             messages.error(request, "Failed To Update Your Profile")
#
#     return render(request, 'profile.html')



# class get_user_details(View):
#     def get(self, request):
#         if request.user:
#             return HttpResponse("User: " + request.user.email + " User Type: " + request.user.user_type)
#         else:
#             return HttpResponse("Please Login First")



# class UserRegistrationView(View):
#     def get(self, request):
#         form = UserRegistrationForm()
#         return render(request, 'register.html', {'form': form})

    # def post(self, request):
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('login')
    #     return render(request, 'register.html', {'form': form})






# class UserLoginView(View):
#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'login.html', {'form': form})
#
#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('Home')
#         return render(request, 'login.html', {'form': form})
#
#
# class UserLogoutView(View):
#     def post(self, request):
#         logout(request)
#         return redirect('Home')
