import moneyball, LoL, DotA2

def lolStats():
    lists = LoL.scrapeLoL()
    keys = lists.keys()
    for key in keys:
        for player in lists[key]:
            moneyball.moneyBallLoL(player)

"""       
def r6sStats():
    #call moneyball on players
"""

"""
def r6sStats():
    #call moneyball on players
"""

"""
def dotaStats():
    #call moneyball on players
"""
