import moneyball, LoL, DotA2, d2, R6S

def lolStats():
    lists = LoL.scrapeLoL()
    moneyball.moneyBallLoL(lists)

      
def d2Stats():
    playerStats = d2.scrapeD2()
    print(playerStats.name, end = " ")
    print("has a rating of ", end = "")
    print(moneyball.moneyBallD2(playerStats))


def r6Stats():
    lists = R6S.stats()
    moneyball.moneyBallR6(lists)

    
def dotaStats():
    dotaList = DotA2.dotaStart()
    print(moneyball.moneyBallDota(dotaList))
