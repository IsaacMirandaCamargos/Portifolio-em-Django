from django.shortcuts import render
from django.views.decorators.http import require_http_methods


# Create your views here.

@require_http_methods(['GET'])
def machine_learn(request):
    return render(request, 'machine_learn/index.html')