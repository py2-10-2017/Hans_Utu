# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string
from django.shortcuts import render, redirect

def random_word(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

# Create your views here.
def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0

    return render(request, "RandomWordGenerator/index.html")

def generate(request):
    request.session['tries'] += 1
    request.session['word'] = random_word(10)
    return redirect('/')

def reset(request):
    del request.session['tries']
    del request.session['word']
    return redirect('/')
