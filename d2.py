from bs4 import BeautifulSoup
import sys, requests

#Class to hold player information
class d2Player:
    name = ""
    KD              = 0.0
    E               = 0.0
    winRatio        = 0.0
    totalKills      = 0.0
    totalAssists    = 0.0


    def __init__(self, inName, inKD, inEfficiency, inWinRatio, inTotalKills, inTotalAssists):
        self.name           = inName
        self.KD             = inKD
        self.E              = inEfficiency
        self.winRatio       = inWinRatio
        self.totalKills     = inTotalKills
        self.totalAssists   = inTotalAssists

        


def scrapeD2():
    

    #Loops until user has entered a valid option
    while(1):
        #Asks user if they want to search for Red Fury's stats, or if they want to provide URL for another player
        print("Do you want to search for Red Fury's stats, or give a me URL for another 'DestinyTracker.com' players profile to rate?")
        print("Enter '1' for Red Fury, '2' for your own link to a player")
        userChoice = input()
    
        #Sets URL to default or if they choose to provide URL, then that
        if(userChoice == "1"):
            #Default URL for finding stats (Red Fury's Profile)
            url = "https://destinytracker.com/destiny-2/profile/steam/4611686018468117886/overview"
            break
        elif(userChoice == "2"):
            print("Please paste the 'DestinyTracker.com' link for that player here now: ")
            url = input()
            break
        else:
            print("You have chosen '"+userChoice+"' which is invalid. Please enter either a '1' or a '2'")

    
    #Sets up BeautifulSoup to read our webpage
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
        if count == 5:
            KD = float(i.getText())
        #Gets Efficiency
        if count == 6:
            E = float(i.getText())
        #Gets Win Ratio
        if count == 7:
            temp = i.getText().split("%")
            winRatio = float(temp[0])
        #Gets total kills
        if count == 8:
            temp = i.getText().split(",")
            tempFinal = ""
            for j in range(len(temp)):
                tempFinal = tempFinal + temp[j]
            totalKills = float(tempFinal)
        #Gets total assists
        if count == 9:
            temp = i.getText().split(",")
            tempFinal = ""
            for j in range(len(temp)):
                tempFinal = tempFinal + temp[j]
            totalAssists = float(tempFinal)

    #Creates 'Player' object with stat information and returns 'Player'
    Player = d2Player(name, KD, E, winRatio, totalKills, totalAssists)
    return Player


