"""
Python WebScraping Project
Written by: Wil Neumann, Charlie Walker, and Keevin Lane
12/15/19
A Program designed to scrape the web for esport player data for the games League of Legends, 
Destiny2, DotA2, and Rainbow 6 Siege in order to apply a weighted scoring system to player 
performances for use in fantasy team creation or generally judging the ability of players.
"""
import sys
import backend


while(True):
    print('Which game would you like stats for?\n1.\tLeague of Legends\n2.\tDestiny 2\n3.\tDOTA2\n4.\tRainbow 6 Siege\n5.\tExit Program\nPlease enter the number of the option to navigate to it, eg. "1" for League of Legends.')
    inp = input().strip()
    if inp == "1":
        backend.lolStats()
    elif inp == "2":
        backend.d2Stats()
    elif inp == "3":
        backend.dotaStats()
    elif inp == "4":
        print(4)
        #R6S stuff
    elif inp == "5":
        exit()
    else:
        print("Please enter only the integer correlating to an option. (1, 2, 3, 4 or 5)")

    print("Would you like to see stats for another game? (Y/N)")
    inp2 = input().lower().strip()
    if inp2 == "y":
        continue
    elif inp2 == "n":
        exit()
    else:
        print('Please enter "Y" or "N"')
