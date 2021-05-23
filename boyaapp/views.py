
from rest_framework import generics
from .models import Medicion
from .serializers import MedicionSerializer



from .serializers import *
from .models import *


class MedicionGet(generics.RetrieveAPIView):
    serializer_class = MedicionSerializer

    def get_queryset(self):
        codBoya = self.request.query_params.get('slug', None)
        print(codBoya)
        return Medicion.objects.filter(codBoya=codBoya)


from django.shortcuts import render
from django.views.generic import TemplateView
class Index(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)