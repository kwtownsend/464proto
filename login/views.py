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

# @csrf_protect
# def register(request):
#     if request.method == 'POST':
#         print("register function of login app, POSTing")
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                     username=form.cleaned_data['username'],
#                     password=form.cleaned_data['password1'],
#                     email=form.cleaned_data['email'],
#             )
#             # member = ClubMember.objects.create(
#             #         member=user,
#             # )
#             currentUser = authenticate(username=user.username, password=form.cleaned_data['password1'])
#             if currentUser is not None:
#                 login(request, currentUser)
#             else:
#                 return HttpResponseRedirect(reverse('members:firsttime', kwargs={'pk': currentUser.pk} ))
#                 # return HttpResponseRedirect(reverse("welcome"))

#             return HttpResponseRedirect(reverse('members:update', kwargs={'pk': currentUser.pk} ))
#     else:
#         print("form not valid yet")
#         form = RegistrationForm()

#     variables = RequestContext(request, {
#         'form': form
#     })

#     return render_to_response(
#             'registration/register.html',
#             variables,
#             # context_instance=RequestContext(request),
#     )



# THIS FUNCTION IS NEVER CALLED (I think)
# def register_success(request):
#     print("register_success() function called")
#     return render_to_response(
#         'registration/success.html',
#         context_instance=RequestContext(request),
#     )

# def logout_page(request):
#     print("logout_page() function called")
#     logout(request)
#     return HttpResponseRedirect('/')


# class Welcome(NavBarMixin, DetailView):
#     page_title = _("Magenta Backpack - Welcome")
#     template_name = "welcome.html"
#     model = None
#
#     def get_context_data(self, **kwargs):
#         context = super(DetailView, self).get_context_data(**kwargs)
#         context["bookCount"]  = Thingy.objects.filter(thingy_type='BK').count()
#         context["musicCount"] = Thingy.objects.filter(thingy_type='MU').count()
#         context["movieCount"] = Thingy.objects.filter(thingy_type='MV').count()
#         context["gameCount"]  = Thingy.objects.filter(thingy_type='GM').count()
#         context["sportCount"] = Thingy.objects.filter(thingy_type='SP').count()
#         context["toolCount"]  = Thingy.objects.filter(thingy_type='TL').count()
#         print("got a bunch of context data")
#         return context
#
#     def get_queryset(self):
#         qs = set()
#         return qs


# def welcome(request):
#     return render_to_response(
#             'welcome.html',
#             # context_instance=context,
#     )


# def about(request):
#     # context = RequestContext(request)
#     # context["page_title"] = _("Magenta Backpack - About")
#     # # context["bookCount"]  = Thingy.objects.filter(thingy_type='BK').count()
#     # # context["musicCount"] = Thingy.objects.filter(thingy_type='MU').count()
#     # # context["movieCount"] = Thingy.objects.filter(thingy_type='MV').count()
#     # # context["gameCount"]  = Thingy.objects.filter(thingy_type='GM').count()
#     # # context["sportCount"] = Thingy.objects.filter(thingy_type='SP').count()
#     # # context["toolCount"]  = Thingy.objects.filter(thingy_type='TL').count()
#     # if not request.user.is_anonymous():
#     #     # this is a logged in user
#     #     context["my_thingys_count"], context["my_thingys_color"] = my_thingys_function(request.user)
#     #     context["available_thingys"], context["browse_notice_color"] = thingys_available_function(request.user)
#     #     context["requests_count"], context["requests_notice_color"] = requests_function(request.user)
#     #     context["borrowed"], context["borrowed_notice_color"] = borrowed_thingys_function(request.user)
#     #     context["loaned"], context["loaned_notice_color"] = loaned_thingys_function(request.user)
#     #     context["clubs"] = memberClubList_function(request.user)
#     #     return render_to_response(
#     #             'about_page.html',
#     #             context_instance=context,
#     #     )
#     # else:
#         return render_to_response(
#             'about_page.html',
#             # context_instance=context,
#         )



def help_page(request):
    return render_to_response(
            '../templates/help_app/home.html',
            # context_instance=RequestContext(request),
    )


# @login_required
# def home(request):
#     # bookCount = Thingy.objects.filter(thingy_type='BK').count()
#     # musicCount = Thingy.objects.filter(thingy_type='MU').count()
#     # movieCount = Thingy.objects.filter(thingy_type='MV').count()
#     # gameCount = Thingy.objects.filter(thingy_type='GM').count()
#     # sportCount = Thingy.objects.filter(thingy_type='SP').count()
#     # toolCount = Thingy.objects.filter(thingy_type='TL').count()
#     # print("home() function called")
#     return render_to_response(
#             'home.html',
#             # { 'user': request.user, 'bookCount': bookCount, 'movieCount': movieCount, 'musicCount': musicCount,
#             #   'gameCount': gameCount, 'sportCount': sportCount, 'toolCount': toolCount},
#             # context_instance=RequestContext(request),
#     )


# def search(request):
#     if not request.GET.get('q'):
#         return HttpResponseRedirect('/')
#     searchString = request.GET.get('q')
#     foundObjects = Thingy.objects.filter(shortDescription__contains=searchString)
#     # TODO: The way to make this DRY is to make this a class-based view
#     # See attempt above, that didn't work
#     context = RequestContext(request)
#     context["page_title"] = _("Magenta Backpack - Search Results")
#     # context["bookCount"]  = Thingy.objects.filter(thingy_type='BK').count()
#     # context["musicCount"] = Thingy.objects.filter(thingy_type='MU').count()
#     # context["movieCount"] = Thingy.objects.filter(thingy_type='MV').count()
#     # context["gameCount"]  = Thingy.objects.filter(thingy_type='GM').count()
#     # context["sportCount"] = Thingy.objects.filter(thingy_type='SP').count()
#     # context["toolCount"]  = Thingy.objects.filter(thingy_type='TL').count()
#     if not request.user.is_anonymous():
#         # this is a logged in user
#         context["my_thingys_count"], context["my_thingys_color"] = my_thingys_function(request.user)
#         context["available_thingys"], context["browse_notice_color"] = thingys_available_function(request.user)
#         context["requests_count"], context["requests_notice_color"] = requests_function(request.user)
#         context["borrowed"], context["borrowed_notice_color"] = borrowed_thingys_function(request.user)
#         context["loaned"], context["loaned_notice_color"] = loaned_thingys_function(request.user)
#         context["clubs"] = memberClubList_function(request.user)
#         return render_to_response(
#                 'thingys/thingy_list.html',
#                 { 'object_list': foundObjects},
#                 context_instance=context,
#         )

#     # anonymous user
#     return render_to_response(
#             'search_results.html',
#             { 'object_list': foundObjects},
#             context_instance=context,
#     )