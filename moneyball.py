import math

def moneyBallLoL(player):
    player.score = (player.K * 2.0 - player.D * .5 + player.A * 1.5 + player.CSM + player.PK * 10.0)

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
    #placeholder
    """
    for player in players:
        
    """
    return "placeholder"
