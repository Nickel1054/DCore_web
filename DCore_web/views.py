from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.contrib.auth import authenticate, login
import os
from dotenv import load_dotenv
import ast


class HomePage(TemplateView):
    template_name = 'index.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class ContactsPage(TemplateView):
    template_name = 'contacts.html'


class DocumentationPage(TemplateView):
    template_name = 'documentation.html'


class ProfilePage(UserPassesTestMixin, TemplateView):
    # login_url = 'login/'
    # redirect_field_name = 'email'
    template_name = 'registration/profile.html'

    def test_func(self):
        load_dotenv()
        domains = ast.literal_eval(os.getenv('DOMAINS'))
        return any([self.request.user.username.endswith(i) for i in domains])
        # return self.request.user.username.endswith('@dtek.com')


def page_not_found_view(request, exception):
    return render(request, '404.html', status=400)


def page_not_found_view_404(request, exception):
    return render(request, '404.html', status=404)

def page_not_found_view_500(request):
    return render(request, '404.html', status=500)
