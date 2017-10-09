from __future__ import unicode_literals

from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
    "time": datetime.now()
    }
    return render(request, "Time_Display/index.html", context)
