from django.contrib import admin
from Team.models import Team, PlayerRequest



class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'pk')

admin.site.register(Team, TeamAdmin)


class PlayerRequestAdmin(admin.ModelAdmin):
    list_display = ('player', 'pk')

admin.site.register(PlayerRequest, PlayerRequestAdmin)