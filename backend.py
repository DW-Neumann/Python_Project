import moneyball, LoL, DotA2, d2, R6S

def lolStats():
    loldata = LoL.lolStart()
    keys = loldata.keys()
    print("Top 5 players in each role.")
    for key in keys:
        for player in loldata[key][:5]:
            print("{} {} :{}".format(key, player.name, player.score))


def d2Stats():
    playerStats = d2.scrapeD2()
    print(playerStats.name, end = " ")
    print("has a rating of ", end = "")
    print(moneyball.moneyBallD2(playerStats))


def r6Stats():
    stats = R6S.start()
    moneyBall.moneyBallR6S(stats)


def dotaStats():
    dotadata = DotA2.dotaStart()
    for player in dotadata[:20]:
        print("{} :{}".format(player.name, player.score))
