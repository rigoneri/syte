# -*- coding: utf-8 -*-
import json
import requests

from django.http import HttpResponse
from django.conf import settings
from xml.dom.minidom import parseString


def steam(request, username):
    # Make request to steamcommunity.com with the username to get the 64-bit Steam ID
    username_r = requests.get('http://steamcommunity.com/id/{0}/games?tab=all&xml=1'.format(username))
    steamid = str(parseString(username_r.text.encode('utf-8')).getElementsByTagName('steamID64')[0].firstChild.wholeText)
    totalgames = parseString(username_r.text.encode('utf-8')).getElementsByTagName('game').length

    payload = {'key': settings.STEAM_API_KEY, 'steamids': steamid}

    # Get user details from Steam API
    user_r = requests.get('{0}/GetPlayerSummaries/v0002/'.format(settings.STEAM_API_URL), params=payload)
    user_data = json.loads(user_r.text)
    user_friends_url = '{0}/GetFriendList/v0001/?key={1}&steamid={2}&relationship=friend'.format(settings.STEAM_API_URL, settings.STEAM_API_KEY, steamid)
    user_friends = requests.get('{0}/GetFriendList/v0001/?key={1}&steamid={2}&relationship=friend'.format(settings.STEAM_API_URL, settings.STEAM_API_KEY, steamid))

    # Add number of games and friends to user data
    for player in user_data["response"]["players"]:
        gamecount = parseString(username_r.text.encode('utf-8')).getElementsByTagName('game').length
        friendcount = len(user_friends.json["friendslist"]["friends"])
        player["gamecount"] = gamecount
        player["friendcount"] = friendcount
        if player["personastate"] == 0:
            player["personastate"] = "Offline"
        if player["personastate"] == 1:
            player["personastate"] = "Online"
        if player["personastate"] == 2:
            player["personastate"] = "Busy"
        if player["personastate"] == 3:
            player["personastate"] = "Away"
        if player["personastate"] == 4:
            player["personastate"] = "Snooze"
        if player["personastate"] == 5:
            player["personastate"] = "Looking to trade"
        if player["personastate"] == 6:
            player["personastate"] = "Looking to play"

    # Get recently played games from different XML source and make into JSON object
    recent_games_nodelist = parseString(username_r.text.encode('utf-8')).getElementsByTagName('hoursLast2Weeks')
    recent_games = {}
    games_array = []
    for recent_game in recent_games_nodelist:
        game = recent_game.parentNode
        game_data = {"name": game.getElementsByTagName('name').item(0).firstChild.nodeValue,
                     "logo": game.getElementsByTagName('logo').item(0).firstChild.nodeValue,
                     "storeLink": game.getElementsByTagName('storeLink').item(0).firstChild.nodeValue,
                     "hoursLast2Weeks": game.getElementsByTagName('hoursLast2Weeks').item(0).firstChild.nodeValue,
                     "hoursOnRecord": game.getElementsByTagName('hoursOnRecord').item(0).firstChild.nodeValue,
                     }
        games_array.append(game_data)

    recent_games["games"] = games_array

    context = {'user': user_data["response"]["players"][0]}
    context.update({'recent_games': games_array})

    # Stripping away the useless 'response' wrapper object
    return HttpResponse(content=json.dumps(context),
                        status=user_r.status_code,
                        content_type=user_r.headers['content-type'])
