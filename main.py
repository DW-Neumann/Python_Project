import sys
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
        
                

while(True):
    print('Which game would you like stats for?\n1.\tLeague of Legends\n2.\tCSGO\n3.\tDOTA2\n4.\tRainbow 6 Siege\n5.\tExit Program\nPlease enter the number of the option to navigate to it, eg. "1" for League of Legends.')
    inp = input().strip()
    if inp == "1":
        lolStats()
    elif inp == "2":
        print(2)
        #CSGO stuff
    elif inp == "3":
        print(3)
        #Dota stuff
    elif inp == "4":
        print(4)
        #R6S stuff
    elif inp == "5":
        exit()
    else:
        print("Please enter only the integer correlating to an option. (1, 2, 3, 4 or 5)")

    print("Would you like to see stats for another game? (Y/N)")
    inp2 = input().lower()
    if inp2 == "y":
        continue
    elif inp2 == "n":
        exit()
    else:
        print('Please enter "Y" or "N"')