from bs4 import BeautifulSoup
import sys, requests, json, jsonpickle, moneyball, os

class LoLPlayer:
    name = ""
    K = 0.0
    D = 0.0
    A = 0.0
    CSM = 0.0
    PK = 0.0
    score = 0.0


    def __init__(self, inName, inK, inD, inA, inCSM, inPK, inscore = 0.0):
        self.name = inName
        self.K = inK
        self.D = inD
        self.A = inA
        self.CSM = inCSM
        self.PK = inPK
        self.score = inscore


def lolStart():
    #retrieving location of project for file saving
    path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(path,"loldata.json")
    #checking for existing data for faster execution if update isn't needed
    if os.path.exists(filepath):
        x = True

        while x == True:
            print("An old data file has been found, would you like to seek new data?(Y/N)")
            lolinput = input().lower()

            if lolinput == "y":
                os.remove(filepath)
                print("Old data file removed, now seeking new data.")
                x = False
                loldata = scrapeLoL(filepath)
                return loldata
            elif lolinput == "n":
                print("Parsing current data for display.")
                x = False
                loldata = parseJSON(filepath)
                return loldata
    else:
        loldata = scrapeLoL(filepath)
        return loldata
        

def scrapeLoL(path):
    leaguePlayers = {}
    leaguePlayers["Top"] = scrapeTop()
    leaguePlayers["Jung"] = scrapeJg()
    leaguePlayers["Mid"] = scrapeMid()
    leaguePlayers["Adc"] = scrapeAdc()
    leaguePlayers["Sup"] = scrapeSup()
    with open(path, 'w') as outfile:
        json.dump(jsonpickle.encode(leaguePlayers), outfile)
    leaguePlayers = moneyball.moneyBallLoL(leaguePlayers)
    return leaguePlayers


def parseJSON(path):
    with open(path) as jsonfile:
        loldata = json.load(jsonfile)
        loldata = jsonpickle.decode(loldata)
        print(loldata)
        return loldata


def scrapeTop():

    topList = []

    url = "https://gol.gg/players/list/season-S9/split-ALL/tournament-ALL/position-TOP/week-ALL/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #HTML is dynamically created on page load so tracking by table id not possible
    tb = soup.find('table', {'class': 'table_list playerslist tablesaw trhover'})

    for tr in tb.find_all('tr')[1:]:
        tds = tr.find_all('td')
        name = tds[0].text
        kills = float(tds[5].text)
        deaths = float(tds[6].text)
        assists = float(tds[7].text)
        csm = float(tds[8].text)
        pentas = float(tds[21].text)
        topList.append(LoLPlayer(name, kills, deaths, assists, csm, pentas))
    return topList


def scrapeMid():

    midList = []

    url = "https://gol.gg/players/list/season-S9/split-ALL/tournament-ALL/position-MID/week-ALL/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tb = soup.find('table', {'class': 'table_list playerslist tablesaw trhover'})

    for tr in tb.find_all('tr')[1:]:
        tds = tr.find_all('td')
        name = tds[0].text
        kills = float(tds[5].text)
        deaths = float(tds[6].text)
        assists = float(tds[7].text)
        csm = float(tds[8].text)
        pentas = float(tds[21].text)
        midList.append(LoLPlayer(name, kills, deaths, assists, csm, pentas))

    return midList


def scrapeJg():

    jgList = []

    url = "https://gol.gg/players/list/season-S9/split-ALL/tournament-ALL/position-JUNGLE/week-ALL/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tb = soup.find('table', {'class': 'table_list playerslist tablesaw trhover'})

    for tr in tb.find_all('tr')[1:]:
        tds = tr.find_all('td')
        name = tds[0].text
        kills = float(tds[5].text)
        deaths = float(tds[6].text)
        assists = float(tds[7].text)
        csm = float(tds[8].text)
        pentas = float(tds[21].text)
        jgList.append(LoLPlayer(name, kills, deaths, assists, csm, pentas))

    return jgList


def scrapeAdc():

    adcList = []

    url = "https://gol.gg/players/list/season-S9/split-ALL/tournament-ALL/position-ADC/week-ALL/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tb = soup.find('table', {'class': 'table_list playerslist tablesaw trhover'})

    for tr in tb.find_all('tr')[1:]:
        tds = tr.find_all('td')
        name = tds[0].text
        kills = float(tds[5].text)
        deaths = float(tds[6].text)
        assists = float(tds[7].text)
        csm = float(tds[8].text)
        pentas = float(tds[21].text)
        adcList.append(LoLPlayer(name, kills, deaths, assists, csm, pentas))

    return adcList


def scrapeSup():

    supList = []

    url = "https://gol.gg/players/list/season-S9/split-ALL/tournament-ALL/position-SUPPORT/week-ALL/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tb = soup.find('table', {'class': 'table_list playerslist tablesaw trhover'})

    for tr in tb.find_all('tr')[1:]:
        tds = tr.find_all('td')
        name = tds[0].text
        kills = float(tds[5].text)
        deaths = float(tds[6].text)
        assists = float(tds[7].text)
        csm = float(tds[8].text)
        pentas = float(tds[21].text)
        supList.append(LoLPlayer(name, kills, deaths, assists, csm, pentas))

    return supList