from django.conf.urls import patterns, url

from league import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='league_home'),
    url(r'^team/$', views.teamList, name='league_team_list'),
    url(r'^player/$', views.playerList, name='league_player_list'),
    url(r'^team/(?P<pk>\d+)$', views.team, name='league_team'),
    url(r'^player/(?P<pk>\d+)$', views.player, name='league_player'),
)
