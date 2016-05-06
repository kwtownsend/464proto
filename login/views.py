# login/views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


from django.contrib import auth
from django.shortcuts import render

# from thingys.templates.thingys import thingy_list
from django.core.urlresolvers import reverse
# from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login
from django.views.generic import View, DetailView, ListView
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.utils.translation import ugettext as _
from locations.models import Cities


# This logic will need to be completely re-thought if we're going to use
# the start page with buttons for login and register.
#
# We can either remove the /login and /register urls
# but I think a /login url is a good thing. I like to be able to 
# bookmark a page with a normal web form, so my password manager
# works easily. 
# We can abstract the login form itself to a template, and call it from
# either /login or the homepage. It might not look correct in both 
# instances, though.
#
# 

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )

def welcome(request):
    return render_to_response(
        'welcome.html',
        context_instance=RequestContext(request),
    )   



def help_page(request):
    return render_to_response(
            '../templates/help_app/home.html',
            # context_instance=RequestContext(request),
    )

def search(request):
    if not request.GET.get('q'):
        return HttpResponseRedirect('/')
    searchString = request.GET.get('q')
    foundCities = Cities.objects.filter(city__contains=searchString)
    context = RequestContext(request)
    context["page_title"] = _("Magenta Backpack - Search Results")

    return render_to_response(
            'search_results.html',
            { 'object_list': foundCities},
            context_instance=context,
    )