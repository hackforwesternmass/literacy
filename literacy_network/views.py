from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from datetime import datetime, timedelta
from dateutil import parser
from django.db import DatabaseError
from django.db.models import Sum, Count
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms import widgets
from django.core import serializers
from django.utils import simplejson
from django.db import connection
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import csv, sys, os


def home(request):
    return render(request, "home.html")

