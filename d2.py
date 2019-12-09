from bs4 import BeautifulSoup
import sys, requests

class d2Player:
    name = ""
    KD              = 0.0
    E               = 0.0
    winRatio        = 0.0
    totalKills      = 0.0
    totalAssists    = 0.0


    def __init__(self, inName, inKD, inE, inWinRatio, inTotalKills, inTotalAssists):
        self.name           = inName
        self.KD             = inKD
        self.E              = inE
        self.winRatio       = inWinRatio
        self.totalKills     = inTotalKills
        self.totalAssists   = inTotalAssists

        


def scrapeD2():
    
    url = "https://destinytracker.com/destiny-2/profile/steam/4611686018468117886/overview"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Gets UserName of player from website
    valueList = soup.find_all(class_="username")
    for i in valueList:
        name = i.getText()


    #Gets stats we are interested in for moneyball formula
    valueList = soup.find_all(class_="value")

    count = 0
    for i in valueList:
        count += 1
        #Gets KD ratio
        if count == 12:
            KD = float(i.getText())
        #Gets Efficiency
        if count == 13:
            E = float(i.getText())
        #Gets Win Ratio
        if count == 14:
            temp = i.getText().split("%")
            winRatio = float(temp[0])
        #Gets total kills
        if count == 15:
            temp = i.getText().split(",")
            tempFinal = ""
            for j in range(len(temp)):
                tempFinal = tempFinal + temp[j]
            totalKills = float(tempFinal)
        #Gets total assists
        if count == 16:
            temp = i.getText().split(",")
            tempFinal = ""
            for j in range(len(temp)):
                tempFinal = tempFinal + temp[j]
            totalAssists = float(tempFinal)

    Player = d2Player(name, KD, E, winRatio, totalKills, totalAssists)
    
    return Player


