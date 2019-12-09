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
    filepath = os.path.join(path,"_ datdota » Average Player Performances  .csv")

    if os.path.exists(filepath):
        x = True

        while x == True:
            print("An old data file has been found, would you like to seek new data?(Y/N)")
            dotainput = input().lower()

            if dotainput == "y":
                os.remove(filepath)
                print("Old data file removed, now seeking new data.")
                x = False
                getCSV(path)
            elif dotainput == "n":
                print("Parsing current data for display.")
                x = False
                parseCSV(path)
    else:
        getCSV(path)


def getCSV(path):
    driverpath = os.path.join(path, 'chromedriver.exe')
    print(driverpath)
    options = webdriver.ChromeOptions()
    preferences = {"download.default_directory": path, "safebrowsing.enabled": "false",}
    options.add_experimental_option("prefs", preferences)
    #running headless not possible due to cloudflare on the site.
    #options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options, executable_path=driverpath)
    
    driver.get('https://www.datdota.com/players/performances?default=true&__cf_chl_jschl_tk__=60ada4abcfa961a13c2851c463bae9f528378618-1575860334-0-AVRENwezfU_Rh7WClR5JGucRkzwODotwJiZ7rXRFJjcWO-wm5luuThoJbEBV346Wvzol6GEHtLfl3zZ4_GKl9Cq0FygbEAu4P-bjaBsJrz9xfWovYTTi4PpB956xYpqGXkF4nYf5N7Z1EM1mi6YFm1GJTAMqnUDJTrXEbzqwV5LMimSWfQ1TU2saNEDo1FVALD0gHxt66u-PH-qSBz0iVd5JoQxy6tUJg-Mf8GbMnhw9uaglOZEEh9xI6p3q0MynxKV4Y3EaOYkZfL4aCbZibWbNE_IRfGOLL3GIyBZhKZgXKg8ESIkNu19jJP8cC7drhA')
    #sleeps required to bypass cloudflare anti scrape/DDOS services
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="DataTables_Table_0_wrapper"]/div[1]/div/a[2]/span').click()
    time.sleep(5)
    driver.quit()
    parseCSV(path)


def parseCSV(path):
    playerList = []
    temppath = os.path.join(path, '_ datdota » Average Player Performances  .csv')
    #_ datdota » Average Player Performances  .csv
    with open(temppath, 'r', encoding='utf-8', errors='ignore') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            playerList.append(DotAPlayer(row[0], row[7], row[8], row[9], row[14], row[15], row[17], row[18], row[19]))
    for player in playerList[:50]:
        print(player.name)
    return playerList