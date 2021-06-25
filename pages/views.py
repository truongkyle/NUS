from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


def index(request):
    return HttpResponse(' this is pages')


# Common
class LoginClass(View):
    def get(self, request):
        return render(request, 'Common/login.html')


class DashboardClass(View):
    def get(self, request):
        return render(request, 'Common/dashboard.html', {'title': 'Dashboard'})


# User
class ChangePasswordClass(View):
    def get(self, request):
        context = {'title': 'Change Password'}
        return render(request, 'User/change_password.html', context)
