from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from datetime import datetime, timedelta
from django.db import DatabaseError
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
import csv, sys, os


def home(request):
    return render(request, "home.html")

