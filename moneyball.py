import math

def moneyBallLoL(lists):
    keys = lists.keys()
    for key in keys:
        for player in lists[key]:
            player.score = (player.K * 2.0 - player.D * .5 + player.A * 1.5 + player.CSM + player.PK * 10.0)

    sortLoL(lists)
    for key in keys:
        for player in lists[key]:
            print("{} : {}".format(player.name, player.score))

def moneyBallD2(player):
    #weighs players total kills
    if player.totalKills < 1000:
        totalKillsWeight = .5
    elif (player.totalKills >= 1000 and player.totalKills < 10000):
        totalKillsWeight = 1
    elif (player.totalKills >= 10000 and player.totalKills < 25000):
        totalKillsWeight = 1.5
    elif (player.totalKills >= 25000 and player.totalKills < 50000):
        totalKillsWeight = 2
    elif (player.totalKills >= 50000 and player.totalKills < 100000):
        totalKillsWeight = 2.5
    else:
        totalKillsWeight = 3

    #Weighs players total assists
    if player.totalAssists < 1000:
        totalAssistsWeight = .5
    elif (player.totalAssists >= 1000 and player.totalAssists < 10000):
        totalAssistsWeight = 1
    elif (player.totalAssists >= 10000 and player.totalAssists < 25000):
        totalAssistsWeight = 1.5
    elif (player.totalAssists >= 25000 and player.totalAssists < 50000):
        totalAssistsWeight = 2
    elif (player.totalAssists >= 50000 and player.totalAssists < 100000):
        totalAssistsWeight = 2.5
    else:
        totalAssistsWeight = 3
        
    player.score = (player.KD * 2.0 + player.E * .5 + player.winRatio * 2 + totalKillsWeight + totalAssistsWeight)
    return player.score

def moneyBallDota(players):
    
    for player in players:
        if player.HH > 1000:
            tempHH = round(player.HH, -3)
            player.score += .4*(tempHH/1000)
        if player.HD > 1000:
            tempHD = round(player.HD, -3)
            player.score += .3*(tempHD/1000)
        if player.TD > 1000:
            tempTD = round(player.TD, -3)
            player.score += .2*(tempTD/1000)

        player.score += player.K * .3 + player.D * -.3 + player.A * .15 + player.LH * .003 + player.De * .0015

    return players

def sortLoL(lists):
    keys = lists.keys()
    for k in keys:
        lists[k].sort(key = lambda LoLPlayer: LoLPlayer.score, reverse=True)