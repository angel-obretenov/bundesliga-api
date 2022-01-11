from rest_framework.decorators import api_view
from rest_framework.response import Response

from openLigaPackage.OpenLigaDbApi import API
from utils.suds_helper import suds_to_dict

api = API()

LEAGUE = "bl1"
SEASON = "2021"


@api_view()
def current_group(request):
    response_data = suds_to_dict(api.getCurrentGroup(LEAGUE))

    # dict_camel_to_snake(response_data)
    return Response(data=response_data)




@api_view()
def get_current_group_matches(request):
    group = api.getCurrentGroup(LEAGUE)
    response_data = suds_to_dict(api.getMatchdataByGroupLeagueSaison(group["groupOrderID"], LEAGUE, SEASON))

    return Response(data=response_data["Matchdata"])


@api_view()
def get_next_match(request):
    response_data = suds_to_dict(api.getNextMatch(LEAGUE))

    return Response(data=response_data)


@api_view()
def get_season_matches(request):
    response_data = suds_to_dict(api.getMatchdataByLeagueSaison(LEAGUE, SEASON))

    return Response(data=response_data["Matchdata"])
