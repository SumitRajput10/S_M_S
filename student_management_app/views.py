from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, LoginForm
from student_management_app.EmailBackEnd import EmailBackEnd
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required






class Home(View):
    def get(self, request):
        return render(request, "home.html")

class About(View):
    def get(self, request):
        return render(request, "about.html")



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

def Base(request):
    return render(request, 'base.html')

class loginPage(View):
    def get(self, request):
        return render(request, 'login.html')

class doLogin(View):
    def post(self, request):
        if request.method != "POST":
            return HttpResponse("<h2>Method Not Allowed</h2>")

        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        print(user)
        if user:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                # return HttpResponse("HOD Login")
                return redirect('HOD_app:hod_home')
            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')
            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('student_home')

        messages.error(request, "Invalid Login Credentials!")
        return redirect('login')

# class get_user_details(View):
#     def get(self, request):
#         if request.user:
#             return HttpResponse("User: " + request.user.email + " User Type: " + request.user.user_type)
#         else:
#             return HttpResponse("Please Login First")


class logout_user(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')








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




