from bs4 import BeautifulSoup
import sys, requests

class LoLPlayer:
    name = ""
    K = 0.0
    D = 0.0
    A = 0.0
    CSM = 0.0
    PK = 0.0
    score = 0.0


    def __init__(self, inName, inK, inD, inA, inCSM, inPK):
        self.name = inName
        self.K = inK
        self.D = inD
        self.A = inA
        self.CSM = inCSM
        self.PK = inPK
        
def scrapeLoL():
    leaguePlayers = {}
    leaguePlayers["Top"] = scrapeTop()
    leaguePlayers["Jung"] = scrapeJg()
    leaguePlayers["Mid"] = scrapeMid()
    leaguePlayers["Adc"] = scrapeAdc()
    leaguePlayers["Sup"] = scrapeSup()
    return leaguePlayers


def scrapeTop():

    topList = []

    url = "https://gol.gg/players/list/season-S9/split-ALL/tournament-ALL/position-TOP/week-ALL/"
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