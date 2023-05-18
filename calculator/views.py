from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from calculator.forms import CalculatorForm
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .calculator_utils.Calculator_class import *


# Create your views here.

class Success(TemplateView):
    template_name = 'base.html'


def calculator_view(request):
    if request.method == 'POST':
        print('success')
        return render(request, 'base.html', {})
    form = CalculatorForm
    return render(request, 'calculator.html', {'form': form})

class CalculatorPage(FormView):
    template_name = "calculator.html"
    form_class = CalculatorForm
    # success_url = 'success/'

    # context = {
    #     "form": form_class
    # }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # print("CONTEXT: \n", context['planets'])
        return context

    def form_valid(self, form):
        return super(CalculatorPage, self).form_valid(form)

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     a = Calculator()
    #     return super().form_valid(form)
    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, self.context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = CalculatorForm(request.POST)
    #     if form.is_valid():
    #         answer = form.cleaned_data
    #
    #     context = {'form': answer}
    #     return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     a = Calculator()
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request, **kwargs):
    #     form =
    #     if form.is_valid():
    #         a = Calculator()
    #         # Success! We can use form.cleaned_data now
    #         return redirect('success')

    # def form_invalid(self, form, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     # here you can add things like:
    #     context['show_results'] = False
    #     return self.render_to_response(context)
    #
    # def form_valid(self, form, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     a = Calculator()
    #     # here you can add things like:
    #     context['show_results'] = True
    #     return self.render_to_response(context)
    #
    # def form_valid(self, form):
    #     self.render_to_response()
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     return super().form_valid(form)
    #
    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, context=self.context)
