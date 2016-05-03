from locations.models import Zipcode
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from braces.views import LoginRequiredMixin

# class ClubActionMixin(object):
    
#     fields = ('name', 'description', 'zipcode')
    
#     @property
#     def success_msg(self):
#         return NotImplemented

#     @staticmethod
#     def is_member_current_user(self, member):
#         """
#         Is the current user the member being looked at
#         :param self:
#         :return:
#         """
#         pass



def welcome(request):
    return render_to_response(
        'welcome.html',
        context_instance=RequestContext(request),
    )   

# class LocationDetailView(LoginRequiredMixin, NavBarMixin, DetailView):
#     model = Zipcode
#     page_title = _("Location Detail")

#     def get_context_data(self, **kwargs):
#         context = super(ClubDetailView, self).get_context_data(**kwargs)
#         # self.navBar_context(context)
#         # context["page_title"] = _("Club Detail")
#         # context["available_thingys"] = self.thingys_available()
#         this_club = self.get_object(queryset=None)
#         member_list = this_club.members.all()
#         context["top_panel_name"] = "Members"
#         context["bottom_panel_name"] = "Request Membership"
#         context["member_count"] = len(member_list)
#         if Club.is_member(this_club, self.request.user):
#             # member specific context data goes here
#             context["bottom_panel_name"] = "Membership Requests"
#             context["member"] = True
#             context["members_list"] = member_list

#             context["member_requests"] = this_club.member_requests_list()
#             if Club.is_leader(this_club, self.request.user):
#                 context["leader"] = True

#         if Club.is_leader(this_club, self.request.user):
#             # leader specific context data goes here
#             pass
#         return context


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