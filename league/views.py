# roster/views.py
from django.shortcuts import render, get_object_or_404#, redirect_render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from league.models import Team, Player

def home(request):
    context = {
        'player_count': Player.objects.count(),
        'team_count': Team.objects.count(),
    }
    return render(request, 'league/home.html', context)

def team(request, pk):
    team = get_object_or_404(Team, id=pk)
    return render(request, 'league/team.html', {'team': team})

def player(request, pk):
    player = get_object_or_404(Player, id=pk)
    return render(request, 'league/player.html', {'player': player})
    
def teamList(request):
    team_list = Team.objects.all()
    return render(request, 'league/team_list.html', {'teams': team_list})

def playerList(request):
    player_list = Player.objects.all()
    return render(request, 'league/player_list.html', {'players': player_list})