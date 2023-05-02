# from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from calculator.forms import CalculatorForm
from django.shortcuts import render


# Create your views here.
class CalculatorPage(FormView):
    template_name = "calculator.html"
    form_class = CalculatorForm
    COMMODITIES = [
        ("gas", "Gas"),
        ("clean_spark", "Clean spark spread"),
        ("spark", "Spark spread"),
        ("electricity_spot", "Electricity spot"),
        ("electricity_futures", "Electricity futures"),
        ("co2", "CO2"),
    ]

    EXCHANGE = {
        "gas":
            [
                ("icis", "ICIS"),
                ("eex", "EEX"),
            ],
        "clean_spark":
            [
                ("gas", "Gas"),
                ("icis", "ICIS"),
                ("eex_co2", "EEX + CO2")
            ],
        "spark":
            [
                ("icis", "ICIS"),
                ("eex", "EEX"),
            ],
        "electricity_spot":
            [
                ("spot", "Spot prices"),
            ],
        "electricity_futures":
            [
                ("tge", "TGE"),
                ("eex", "EEX"),
            ],
        "co2":
            [
                ("eex", "EEX"),
            ],
    }

    context = {
        "exchange": EXCHANGE,
        "form": form_class
    }
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)
