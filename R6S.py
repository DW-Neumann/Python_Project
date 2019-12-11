import asyncio
import r6sapi as api


class R6Player:
    name = ''
    kills = 0
    deaths = 0
    assists = 0
    accuracy = 0.0
    revives = 0
    winRate = 0.0
    score = 0.0

    def __init__(self, inName, inKill, inDeath, inAssist, inAccuracy, inRevive, inWinrate):
        self.name = inName
        self.kills = inKill
        self.deaths = inDeath
        self.assists = inAssist
        self.accuracy = inAccuracy
        self.winRate = inWinrate


# function to start async function
def start():
    return asyncio.get_event_loop().run_until_complete(stats())


async def stats():
    playerList = []
    proPlayers = []

    # open text file and read each line into list
    statFile = open('R6ProPlayers.txt')
    for line in statFile:
        playerList.append(line.replace('\n', ''))

    # begin r6api byt opening with Ubisoft email and password, account is a throwaway account used for the project only
    auth = api.Auth("r6statsemail@gmail.com", "PythonProject")

    # collect stats and initialize object with them
    for name in playerList:
        try:
            player = await auth.get_player(name, api.Platforms.UPLAY)
            await player.load_general()
            kills = player.kills
            deaths = player.deaths
            assists = player.kill_assists
            accuracy = (player.bullets_hit / player.bullets_fired)
            revives = player.revives
            winRate = (player.matches_won / player.matches_played)
            proPlayers.append(R6Player(name, kills, deaths, assists, accuracy, revives, winRate))


        except:
            continue
    # close api and return object list
    await auth.close()
    return proPlayers

