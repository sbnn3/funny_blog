from django.shortcuts import render
from django.views import generic, View
from .models import Guitars


class GuitarsPage(generic.ListView):
    model = Guitars
    queryset = Guitars.objects.filter(status=1).order_by('-created_on')
    template_name = 'guitars.html'
    paginate_by = 10