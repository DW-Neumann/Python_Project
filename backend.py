import moneyball, LoL, DotA2, d2

def lolStats():
    lists = LoL.scrapeLoL()
    keys = lists.keys()
    for key in keys:
        for player in lists[key]:
            print(moneyball.moneyBallLoL(player))

      
def d2Stats():
    playerStats = d2.scrapeD2()
    print(playerStats.name, end = " ")
    print("has a rating of ", end = "")
    print(moneyball.moneyBallD2(playerStats))


"""
def r6sStats():
    #call moneyball on players
"""

def dotaStats():
    dotaList = DotA2.dotaStart()
    print(moneyball.moneyBallDota(dotaList))

