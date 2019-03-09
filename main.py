from GameSituation import GameSituation
from Functions import *

# Initialize Global Variables
listOfTeams = []

listOfRosters = create_roster_list()

write_roster_data(listOfRosters)

my_dir_path = '/Users/jordancripe/PycharmProjects/CollegeBaseballStats/Games_HTML/'

list_of_html_games = [


    'MOR_LOU_3_6_2019_15.html',

]


listOfFiles = []
for fileName in list_of_html_games:
    filePathString = my_dir_path + fileName
    listOfFiles.append(filePathString)

listOfFiles = get_absolute_file_paths('Games_HTML')

gameInfoList = load_game_info_list(listOfFiles)

masterJSON = []
for gameInfo in gameInfoList:

    # initialize home and away rosters
    awayRoster = get_roster_by_id(gameInfo.awayTeamId, listOfRosters)
    homeRoster = get_roster_by_id(gameInfo.homeTeamId, listOfRosters)

    # initialize game situation
    gameSituation = GameSituation(awayRoster, homeRoster)

    # set home and away lineups
    gameSituation.awayLineUp.setLineUp(gameInfo.awayPlayerList)
    gameSituation.homeLineUp.setLineUp(gameInfo.homePlayerList)

    # initialize first batter
    gameSituation.currentBatter = gameInfo.awayPlayerList[0]

    # initialize players in field
    gameSituation.loadField()

    prevInningOrder = -1
    for ev in gameInfo.eventList:
        # print('-------------------------------------------------------')
        # gameSituation.showState()
        # print(ev.curText)

        # remove suffix from all play by play text
        if " III" in ev.origText or " IV" in ev.origText or " II" in ev.origText or " Jr." in ev.origText:
            ev.origText = ev.origText.replace(" III", "").replace(" IV", "").replace(" II", "").replace(" Jr.", "")
            ev.curText = ev.origText.lower()

        ev.initializeGameInfo(gameInfo)
        ev.initializeGameSituationInfo(gameSituation)

        ev.curText = ev.parseRBI(ev.curText)
        ev.curText = ev.parseBallsStrikes(ev.curText)
        ev.curText = ev.parseSubstitution(ev.curText)
        ev.curText = ev.parseReview(ev.curText)

        if ev.substitution:
            gameSituation.analyzeSubstitution(ev.substitution)
            gameSituation.loadField()
            ev.result = 'SUB'
        else:
            ev.parseAppearance()
            ev.cleanBaseRunningList()
            ev = ev.setBaseRunnerPlayerInfo(gameSituation)
            print(ev.origText)
            ev = gameSituation.analyzeEvent(ev)

        # if curText includes currentBatter name
        # checks to see if the inning ended on a base running play
        if ev.hasName(ev.curText, gameSituation.currentBatter.firstName, gameSituation.currentBatter.lastName):
            gameSituation.nextBatter()
        else:
            # move to next batter if 3 outs
            if gameSituation.outs == 3:
                gameSituation.nextBatter()
                # move team that was batting's index back
                if gameSituation.isHomeBatting and ev.result == 'BR':
                    if gameSituation.awayIndex == 0:
                        gameSituation.awayIndex = 8
                    else:
                        gameSituation.awayIndex -= 1
                elif ev.result == 'BR':
                    if gameSituation.homeIndex == 0:
                        gameSituation.homeIndex = 8
                    else:
                        gameSituation.homeIndex -= 1
                else:
                    pass

        jsonData = ev.eventToJSON()
        if ev.result == 'SUB':
            pass
        elif ev.result == 'BR':
            jsonData['inningOrder'] = "{0:.1f}".format(prevInningOrder + 0.1)
            masterJSON.append(jsonData)
        else:
            masterJSON.append(jsonData)

        prevInningOrder = float(jsonData['inningOrder'])

finalJSON = dict()
finalJSON['Matchups'] = masterJSON

write_to_json_file("MatchupData.js", finalJSON, "matchupJSON")
print(len(masterJSON))


















