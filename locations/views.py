# clubs/views.py
from django.contrib.auth.models import User

# for I18N
from django.utils.translation import ugettext as _
# TSoD page 98, Class-based views
from django.core.urlresolvers import reverse
# end TSoD
# signals.receiver
from django.db.models import signals
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from braces.views import LoginRequiredMixin
from django.contrib import messages
from helpers.navbar_helpers import NavBarMixin
from django.contrib import messages


from locations.models import Zipcode
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from braces.views import LoginRequiredMixin
from helpers.navbar_helpers import NavBarMixin
from locations.models import Cities

class CityActionMixin(object):
    
    fields = ('postalcode', 'city', 'state', 'county', 'latitude', 'longitude')
    
    @property
    def success_msg(self):
        return NotImplemented

    @staticmethod
    def is_member_current_user(self, member):
        """
        Is the current user the member being looked at
        :param self:
        :return:
        """
        pass


def welcome(request):
    return render_to_response(
        'welcome.html',
        context_instance=RequestContext(request),
    )   

class LocationDetailView(LoginRequiredMixin, CityActionMixin, NavBarMixin, DetailView):
    model = Cities

    def get_context_data(self, **kwargs):
        context = super(LocationDetailView, self).get_context_data(**kwargs)
        this_city = self.get_object(queryset=None)
        
        # get context data for google map
        geographical_info = Cities.objects.get(postalcode=this_city.postalcode)
        # if len(geographical_set) < 1:
        #     print("zip not found, using CSUF")
        #     geographical_info = Zipcode.objects.get(zip=92834)
        # else:
        # geographical_info = geographical_set[0]
        context["lat"] = geographical_info.latitude
        context["lon"] = geographical_info.longitude
        context["city"] = this_city.city
        context["state"] = geographical_info.state

        return context



# class LocationDetailView(NavBarMixin, DetailView):
#     model = Player
#     template_name = "Players/player_detail.html"
#     page_title = _("Available Player Detail")

#     def get(self, request, *args, **kwargs):
#         player = self.get_object(queryset=None)
#         return super(PlayerDetailView, self).get(self, request, *args, **kwargs)
        
# def search(request):
#     if not request.GET.get('q'):
#         return HttpResponseRedirect('/')
#     searchString = request.GET.get('q')
#     # foundPlayers = Player.objects.filter(name__contains=searchString)
#     context = RequestContext(request)
#     context["page_title"] = _("Magenta Backpack - Search Results")
#     return render_to_response(
#             'search_results.html',
#             { 'object_list': foundPlayers},
#             context_instance=context,
#     )