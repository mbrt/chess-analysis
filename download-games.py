#!/usr/bin/python

import json
import requests
import sys


def get_archives(player):
    r = requests.get('https://api.chess.com/pub/player/{}/games/archives'.format(player))
    if not r.ok:
        raise Exception('get_archives failed')
    archive = json.loads(r.content)
    return archive['archives']


def get_month_games(player, yyyy_mm):
    r = requests.get('https://api.chess.com/pub/player/{}/games/{}'.format(player, yyyy_mm))
    if not r.ok:
        raise Exception('get_month_pgn failed')
    games = json.loads(r.content)
    # Format: {games: [{url, pgn}, ...]}
    return games['games']


player = sys.argv[1]
archives = get_archives(player)
all_games = []

for url in archives:
    yyyy_mm = url[-7:]
    games = get_month_games(player, yyyy_mm)
    all_games += [g['pgn'] for g in games]

print(json.dumps(all_games))
