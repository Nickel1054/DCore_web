# from django.urls import reverse
# from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login


class HomePage(TemplateView):
    template_name = 'index.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class DocumentationPage(TemplateView):
    template_name = 'documentation.html'


class ProfilePage(TemplateView):
    # login_url = 'login/'
    # redirect_field_name = 'email'
    template_name = 'registration/profile.html'

# class LogOutPage(TemplateView):
#     template_name = 'registration/logged_out.html'

# class LoginPage(TemplateView):
#     form_class = LoginForm
#     initial = {'email': 'Username@dtek.com'}
#     template_name = 'registration/login.html'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request,  *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             print(kwargs)
#             user = authenticate(username='john', password='secret')
