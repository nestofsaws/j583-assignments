from django.contrib import admin
from league.models import Team, Player

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Team, TeamAdmin)

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Player, PlayerAdmin)
