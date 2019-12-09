from selenium import webdriver
import time, os, csv

class DotAPlayer:
    name = ""
    K = 0.0
    D = 0.0
    A = 0.0
    LH = 0.0
    De = 0.0
    HD = 0.0
    TD = 0.0
    HH = 0.0
    score = 0.0



    def __init__(self, inName, inK, inD, inA, inLH, inDe, inHD, inTD, inHH):
        self.name = inName
        self.K = inK
        self.D = inD
        self.A = inA
        self.LH = inLH
        self.De = inDe
        self.HD = inHD
        self.TD = inTD
        self.HH = inHH


def dotaStart():
    path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join("_ datdota » Average Player Performances  .csv")

    if path.exists(filepath):
        x = True

        while x == True:
            print("An old data file has been found, would you like to seek new data?(Y/N)")
            input = input().lower()

            if input == "y":
                os.remove(filepath)
                print("Old data file removed, now seeking new data.")
                getCSV(path)
            elif input == "n":
                print("Parsing current data for display.")
                parseCSV(path)


def getCSV(path):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("download.default_directory={path}")
    driver = webdriver.Chrome(chrome_options=options)
    
    try:
    	driver.get('https://www.datdota.com/players/performances?default=true') # Your Website Address
    	download_button = driver.find_element_by_xpath('//*[@id="DataTables_Table_0_wrapper"]/div[1]/div/a[2]')
    	download_button.click()
    	driver.quit()
        parseCSV(path)
    except:
    	driver.quit()
    	print("Faulty URL")


def parseCSV(path):
    playerList = []

    with open('_ datdota » Average Player Performances  .csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            playerList.append(DotAPlayer(row[0], row[7], row[8], row[9], row[14], row[15], row[17], row[18], row[19]))
    return playerList