from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator







# Create your views here.
# @method_decorator(login_required, name='dispatch')
class AdminHomeView(View):
    def get(self, request):
        return render(request, "HOD_template/home.html")