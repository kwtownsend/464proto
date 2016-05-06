from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# from helpers.backpack_helpers import count_user_items, requests_count
# from helpers.backpack_helpers import borrows_count, lends_count

# from thingys.models import Thingy
# from clubs.models import Club
# from lends.models import Lend
# from asks.models import AskBorrow

# def thingys_available_function(user):
#     all_clubs = Club.objects.filter(members=user)
#     members = []
#     for aClub in all_clubs:
#         members += User.objects.filter(club=aClub)
#     if user and len(members) > 0:
#         members.remove(user)
#     set_of_members = list(set(members))
#     total_count = 0
#     for aMember in set_of_members:
#         total_count += Thingy.objects.filter(owner=aMember).count()  # TODO: add lendable=true filter

#     if total_count > 0:
#         return total_count, "#AAFFAA"
#     else:
#         return total_count, "#FFEEEE"

# def memberClubList_function(user):
#     return Club.objects.filter(members=user)

# def my_thingys_function(user):
#     count = count_user_items(user)
#     if count > 0:
#         return count, "#AAFFAA"
#     else:
#         return count, "#FFEEEE"

# def requests_function(user):
#     request_count = requests_count(user)
#     if request_count > 0:
#         return request_count, "#AAFFAA"
#     else:
#         return request_count, "#FFEEEE"



# def borrowed_thingys_function(user):
#     borrowed_count =  borrows_count(user)
#     if borrowed_count > 0:
#         return borrowed_count, "#AAFFAA"
#     else:
#         return borrowed_count, "#FFEEEE"


# def loaned_thingys_function(user):
#     # TODO: implement
#     loaned_thingys = lends_count(user)
#     if loaned_thingys > 0:
#         return loaned_thingys, "#AAFFAA"
#     else:
#         return loaned_thingys, "#FFEEEE"


# def browse_notice_color_function(user):
#     # TODO: implement by finding events that are soon or past
#     return "#FFEEFF"
#
# def requests_notice_color_function(user):
#     # TODO: implement by finding events that are soon or past
#     return "#00FF00"
#
# def borrow_notice_color_function(user):
#     # TODO: implement by finding events that are soon or past
#     return "#CCFFFF"
#
# def lend_notice_color_function(user):
#     # TODO: implement by finding events that are soon or past
#     return "#FFFFCC"
#

class NavBarMixin(object):
    """
    Sometimes a view will be needed for both Members
    and anonymous users.
    To NOT call this mixin's get_context_data method,
    The super of this class is (to get NavBarMixin data, for Members)
        super(<your class based view>, self)
    To skip calling NavBarMixin, we call the super of THAT class
    (to skip getting data for anonymous),
        super(NavBarMixin, self)
    WARNING: if you try to call this get_context_data() method with no session user,
             no objects will be found and it JUST WON'T WORK!
    See a more detailed description in help_app/views.py
    """
    # TODO: the test of whether the user exists or not should be done here, locally, but I don't know how.
    page_title = _("Magenta Backpack")

    def get_context_data(self, **kwargs):
        # world+dog context data goes here
        context = super(NavBarMixin, self).get_context_data(**kwargs)
        context["page_title"] = self.page_title
        # if self.request.user.is_anonymous == True:
        #     return context
        # context["my_thingys_count"], context["my_thingys_color"] = self.my_thingys_count()
        # context["available_thingys"], context["browse_notice_color"] = self.thingys_available()
        # context["requests_count"], context["requests_notice_color"] = self.requests_count()
        # context["borrowed"], context["borrowed_notice_color"] = self.borrowed_thingys()
        # context["loaned"], context["loaned_notice_color"] = self.loaned_thingys()
        # context["clubs"] = self.member_club_list()
        # # TODO: find out how many items are due or near due, and use to look up color value
        # context["browse_notice_color"] = self.browse_notice_color()
        # context["requests_notice_color"] = self.requests_notice_color()
        # context["borrowed_notice_color"] = self.borrow_notice_color()
        # context["loaned_notice_color"] = self.lend_notice_color()
        template_name = "templates/player_detail.html"
        return context

    # def my_thingys_count(self):
    #     # TODO: is there any reason to change color for my thingys count?
    #     count = count_user_items(self.request.user)
    #     if count > 0:
    #         return count, "#EEEEEE"
    #     else:
    #         return count, "#FFEEEE"

    # def thingys_available(self):
    #     all_clubs = Club.objects.filter(members=self.request.user)
    #     members = []
    #     for aClub in all_clubs:
    #         members += User.objects.filter(club=aClub)
    #     if self.request.user and len(members) > 0:
    #         members.remove(self.request.user)
    #     total_count = 0
    #     set_of_members = list(set(members))
    #     for aMember in set_of_members:
    #         total_count += Thingy.objects.filter(owner=aMember).count()  # TODO: add lendable=true filter
    #     if total_count > 0:
    #         return total_count, "#EEEEEE"
    #     else:
    #         return total_count, "#FFEEEE"

    # def requests_count(self):
    #     request_count = requests_count(self.request.user)
    #     if request_count > 0:
    #         return request_count, "#AAFFAA"
    #     else:
    #         return request_count, "#EEEEEE"

    # def member_club_list(self):
    #     return Club.objects.filter(members=self.request.user)

    # def borrowed_thingys(self):
    #     # TODO: make colors better,
    #     # TODO: make search for overdue and make red if overdue > 0
    #     borrow_count = borrows_count(self.request.user)
    #     if borrow_count > 0:
    #         return borrow_count, "#EEBBEE"
    #     else:
    #         return borrow_count, "#EEEEEE"

    # def loaned_thingys(self):
    #     # TODO: make better colors
    #     # TODO: overdue in red?
    #     lend_count = lends_count(self.request.user)
    #     if lend_count > 0:
    #         return lend_count, "#EEBBEE"
    #     else:
    #         return lend_count, "#EEEEEE"


    # def browse_notice_color(self):
    #     # TODO: implement by finding events that are soon or past
    #     return "#FFEEFF"
    #
    # def requests_notice_color(self):
    #     # TODO: implement by finding events that are soon or past
    #     return "#00FF00"
    #
    # def borrow_notice_color(self):
    #     # TODO: implement by finding events that are soon or past
    #     return "#CCFFFF"
    #
    # def lend_notice_color(self):
    #     # TODO: implement by finding events that are soon or past
    #     return "#FFFFCC"




