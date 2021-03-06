from django.shortcuts import render
from django.views.generic import TemplateView
from .models import City
from rest_framework.views import APIView
from rest_framework.response import Response


def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    return render(request, 'accounts/product.html')


def customer(request):
    return render(request, 'accounts/customer.html')


class CityCharView(TemplateView):
    template_name = 'cities/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = City.objects.all()
        return context



class ListCity(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        violence_count = {city.violence for city in City.objects.all()}
        print(violence_count)
        return Response(violence_count)
