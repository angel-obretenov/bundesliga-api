from django.urls import path
from .views import current_group, get_current_group_matches, get_next_match, get_season_matches

urlpatterns = [
    path('', get_season_matches, name='current-matches'),
    path('current-group/', current_group, name='current-group'),
    path('next/', get_next_match, name='next-match'),
    path('group/', get_current_group_matches, name='next-match'),
]
