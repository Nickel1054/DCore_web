from django.views.generic.edit import FormView
from calculator.forms import CalculatorForm
from django.shortcuts import render


# Create your views here.
class CalculatorPage(FormView):
    template_name = "calculator.html"
    form_class = CalculatorForm

    context = {
        "form": form_class
    }
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)
