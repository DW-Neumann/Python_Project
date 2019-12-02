import moneyball, LoL

def makeLeague():
    leaguePlayers = {}
    leaguePlayers["Top"] = LoL.scrapeTop()
    leaguePlayers["Jung"] = LoL.scrapeJg()
    leaguePlayers["Mid"] = LoL.scrapeMid()
    leaguePlayers["Adc"] = LoL.scrapeAdc()
    leaguePlayers["Sup"] = LoL.scrapeSup()

    return leaguePlayers

def lolStats():
    lists = makeLeague()
    keys = lists.keys()
    for key in keys:
        for player in lists[key]:
            moneyball.moneyBallLoL(player)

"""       
def makeSiege():
    #instantiate R6S player list/ dicts

def r6sStats():
    #call moneyball on players
"""

"""
def makeD2():
    #instantiate D2 player list/ dicts

def r6sStats():
    #call moneyball on players
"""

"""
def makeDota2():
    #instantiate DotA2 player list/ dicts

def dotaStats():
    #call moneyball on players
"""
