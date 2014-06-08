from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from datetime import datetime, timedelta
from django.db import DatabaseError
from django.utils import simplejson
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from literacy_network.models import *
from literacy_network.forms import *
from django.core.exceptions import PermissionDenied
import csv, sys, os
from django.contrib.auth import authenticate, login

def home_redirect(request):
    """ Redirects the user to a registration form or volunteer list 
        depending on their account role 
    """
    if request.user.is_authenticated() and request.user.is_staff:
        return redirect("volunteers")
    elif request.user.is_authenticated() and not request.user.is_superuser:
        related_volunteer = get_object_or_404(Volunteer, user_id=request.user.pk)
        return redirect("edit-volunteer-profile", volunteer_id=related_volunteer.pk)
    else:
        return redirect("new-volunteer")

def logged_out(request):
    """ Renders a page notifying the user that they have logged out
        and points them back to the organization's main site
    """
    return render(request, "logged-out.html")

def create_volunteer(request, volunteer_id=None):
    """ Presents a view used to edit a volunteer

        Keyword arguments:
            volunteer_id -- The primary key of the volunteer
                        to edit, or None to perform an add
        Returns a view used to edit the volunteer on GET,
            or a redirection to the volunteer list on POST
    """
    volunteer = None
    try:
        volunteer = Volunteer.objects.get(id=volunteer_id)
        user = User.objects.get(id=volunteer.user_id)
    except Volunteer.DoesNotExist:
        vol_form = VolunteerForm()
        user_form = UserCreationForm()
        user = User()
    except User.DoesNotExist:
        user_form = UserCreationForm()

    if request.method == "POST":
        vol_form = VolunteerForm(request.POST, request.FILES)
        user_form = UserCreationForm(request.POST, request.FILES)

        if vol_form.is_valid() and user_form.is_valid():
            svol = vol_form.save()
            user = user_form.save()

            # associate the user with the volunteer
            svol.user = user
            svol.save()
            user = authenticate(username=user.username, password=user_form.clean_password2())
            login(request, user)

            return redirect("edit-volunteer-profile", 
                volunteer_id=svol.id, hide_contact_form=True)
    elif volunteer_id:
        vol_form = VolunteerForm(instance=volunteer)
        if user:
            user_form = UserCreationForm(instance=user)

    return render(request, 'edit-volunteer.html', 
        {"vol_form" : vol_form, "user_form" : user_form })
         
@login_required
def edit_volunteer_profile(request, volunteer_id, hide_contact_form=False):
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
    if (volunteer.user and request.user.pk != volunteer.user.pk) and not request.user.is_superuser:
        raise PermissionDenied()

    # make sure there is a record for each volunteer help type
    new_helps = [q for q in HelpType.objects.all()
                    if not q in [r.help_type for r in 
                             volunteer.helptyperesponse_set.all()]]
    for helptype in new_helps:
        resp = HelpTypeResponse.objects.create(volunteer=volunteer, 
                help_type=helptype, affirmative=False)

    # make sure there is a record for each class site
    new_sites = [s for s in Site.objects.all()
                    if not s in [r.site for r in volunteer.volunteersite_set.all()]]
    for site in new_sites:
        addsite = VolunteerSite.objects.create(volunteer=volunteer, 
                            site=site, affirmative=False)

    if request.method == 'POST':
        vol_form = VolunteerForm(request.POST, instance=volunteer)
        user_form = UserEditForm(request.POST, instance=request.user)
        occ_formset = OccupationFormset(request.POST, 
            prefix="occ", instance=volunteer)
        help_formset = HelpResponseFormset(request.POST, 
            prefix="help", instance=volunteer)
        site_formset = SiteFormset(request.POST, 
            prefix="site", instance=volunteer)

        if occ_formset.is_valid() and help_formset.is_valid() \
            and site_formset.is_valid() and vol_form.is_valid() \
            and user_form.is_valid():
            vol_form.save()
            occ_formset.save()
            help_formset.save()
            site_formset.save()
            return render(request, 'thanks.html')
        else:
            print("Vol form errors")
            print(vol_form.errors)
            print("Occ form errors")
            print(occ_formset.errors)
            print("Help form errors")
            print(help_formset.errors)
            print("Site form errors")
            print(site_formset.errors)
    else:
        vol_form = VolunteerForm(instance=volunteer)
        user_form = UserEditForm(instance=request.user)
        occ_formset = OccupationFormset(instance=volunteer, prefix="occ")
        help_formset = HelpResponseFormset(instance=volunteer, prefix="help")
        site_formset = SiteFormset(instance=volunteer, prefix="site")

    return render(request, 'edit_profile.html', {
        "vol_form" : vol_form,
        "user_form" : user_form,
        'occ_formset' : occ_formset,
        'help_formset' : help_formset,
        "site_formset" : site_formset,
        "anchor" : None,
        "hide_contact_form" : hide_contact_form,
        "willvisit" : volunteer.volunteersite_set.filter(affirmative=True).count() > 0
    })

def view_volunteer(request, volunteer_id):
    """ Opens a page for staff members or the public 
        (if the profile is public-enabled) to view a volunteer
    """
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
    if not volunteer.is_public and not \
        (request.user.is_authenticated and 
            (request.user.is_superuser or request.user.is_staff
                (volunteer.user and request.user.pk == volunteer.user.pk))):
        raise PermissionDenied()
    return render(request, "view-volunteer.html", {"volunteer" : volunteer})
    
@user_passes_test(lambda u: u.is_staff)
def volunteers(request):
    """ Presents a list of volunteers """
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers.html',
            {"volunteers" : volunteers})

    return render(request, 'edit-volunteer.html',
        {"form" : form})

def upload_industries(request):
    '''Handles upload of industry data in CSV format'''
    if request.method == "POST":
        for row in csv.DictReader(request.FILES["industries-csv"]):
            industry = Industry()
            industry.code=row["Industry_Code"]
            industry.name=row["Industry_Name"]
            industry.save()
        return redirect("/")
    else:
        return render(request, "upload-industries.html")

    return redirect("/")

def thanks(request):
    return render(request, "thanks.html")
