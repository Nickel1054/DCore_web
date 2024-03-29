from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from calculator.forms import CalculatorForm
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .calculator_utils import Calculator_class
from .calculator_utils import SpreadVis
from django.http import HttpResponse
from io import BytesIO
import pandas as pd
import datetime
import json

# Create your views here.

class Success(TemplateView):
    template_name = 'result.html'


def calculator_view(request):
    if request.method == 'POST':
        print('success')
        return render(request, 'base.html', {})
    form = CalculatorForm
    return render(request, 'calculator.html', {'form': form})


class CalculatorPage(FormView):
    template_name = "calculator.html"
    form_class = CalculatorForm
    success_name = "result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # print("CONTEXT: \n", context['planets'])
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            df, excel_name, data_pieces = Calculator_class.Calculator(form.cleaned_data).run()
            request.session['data'] = df.to_json()
            request.session['excel_name'] = excel_name + datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # graphs = SpreadVis.SpreadVis(df.copy()).run()
            print('REDIRECTING')
            return render(request, self.success_name, {"df": df, 'graphs': data_pieces})

        print('STAYING')
        return render(request, self.template_name, {"form": form})


def download_view(request):
    df = pd.DataFrame(json.loads(request.session['data']))
    with BytesIO() as b:
        # Use the StringIO object as the filehandle.
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        # Set up the Http response.
        filename = request.session['excel_name'] + '.xlsx'
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response
