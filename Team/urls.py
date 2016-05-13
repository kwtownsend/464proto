# clubs urls.py
from django.conf.urls import patterns, include, url
from Team import views


# TODO: I want to standardize namespace names to all lowercase
# e.g. confirmAskJoin > confirmaskjoin,
#      editMember > editMember
# TODO: addMembers is plural. singularize it
# were we really going to add members en masse?


urlpatterns = [
    url(
        regex=r"^$",
        view=views.TeamListView.as_view(),
        name="list"
    ),
    url(
        regex=r"^new$",
        view=views.TeamCreateView.as_view(),
        name="new"
    ),
    url(
        regex=r"^(?P<pk>\d+)$",
        view=views.TeamDetailView.as_view(),
        name="detail"
    ),
    url(
        regex=r"^join/(?P<pk>\d+)$",
        view=views.TeamAskJoinView.as_view(),
        name="askjoin"
    ),
    url(
        regex=r"^confirm/(?P<pk>\d+)$",
        view=views.TeamConfirmAskJoinView.as_view(),
        name="confirmAskJoin"
    ),
    url(
        regex=r"^deleterequest/(?P<pk>\d+)$",
        view=views.DeletePlayerRequest, 
        name="deleterequest"
        ),
    url(
        regex=r"^deleteplayer/(?P<team>\d+)/(?P<player>\d+)$",
        view=views.DeleteTeamPlayer, 
        name="deleteplayer"
    ),

   url(
        regex=r"^addplayer/(?P<pk>\d+)$",
        view=views.TeamAddPlayerView.as_view(),
        name="addplayer"
    ),

    # url(
    #     regex=r"^removeplayer/(?P<pk>\d+)$",
    #     view=views.TeamRemovePlayerView.as_view(),
    #     name="removeplayer"
    # ),
   # url(
   #      regex=r"^editmember/(?P<pk>\d+)$",
   #      view=views.ClubEditMemberView.as_view(),
   #      name="editMember"
   #  ),
    url(
        regex=r"^results/(?P<pk>\d+)$",
        view=views.TeamResultsView.as_view(),
        name="result"
    ),
    # url(
    #     regex=r"^update/(?P<pk>\d+)$",
    #     view=views.ClubUpdateView.as_view(),
    #     name="update"
    # ),
    # url(
    #     regex=r"^delete/(?P<pk>\d+)$",
    #     view=views.ClubDeleteView.as_view(),
    #     name="delete"
    # ),
]
