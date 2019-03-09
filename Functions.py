from GameInfo import GameInfo
from Event import Event
from Roster import Roster
from PlayerInfo import PlayerInfo

import os
import json
import csv


    
    
def init_file_path_list(directory, file_paths):

    list_of_files = []

    for f in file_paths:
        file_path = directory + f
        list_of_files.append(file_path)

    return list_of_files

    
def show_list(list_of_objects):
    for obj in list_of_objects:
        obj.show()

    
def read_csv(str_file_path):

    with open(str_file_path) as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        csv_data = [r for r in reader]
    return csv_data

    
def create_roster_list():

    roster_list = _init_rosters()
    batter_data = read_csv('CSV/Batters.csv')
    pitcher_data = read_csv('CSV/Pitchers.csv')
    player_data_2019 = read_csv('CSV/Players_2019.csv')

    for batter in batter_data:
        i=0
        while i < len(roster_list):
            if batter[1] == roster_list[i].college and not roster_list[i].hasPlayerId(batter[0]):
                temp_player = PlayerInfo(batter[0], batter[1], batter[2], batter[3], batter[4], batter[5])
                roster_list[i].addPlayer(temp_player)
                i = len(roster_list) + 1
            else:
                i += 1

    for pitcher in pitcher_data:
        i = 0
        while i < len(roster_list):
            if pitcher[1] == roster_list[i].college and not roster_list[i].hasPlayerId(pitcher[0]):
                temp_player = PlayerInfo(pitcher[0], pitcher[1], pitcher[2], pitcher[3], pitcher[4], pitcher[5])
                roster_list[i].addPlayer(temp_player)
                i = len(roster_list) + 1
            else:
                i += 1

    for player in player_data_2019:
        i = 0
        while i < len(roster_list):
            if player[1] == roster_list[i].college and not roster_list[i].hasPlayerId(player[0]):
                temp_player = PlayerInfo(player[0], player[1], player[2], player[3], player[4], player[5])
                roster_list[i].addPlayer(temp_player)
                i = len(roster_list) + 1
            else:
                i += 1

    return roster_list


# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
def _init_rosters():
    roster_data = read_csv('CSV/Teams.csv')

    # initialize return variable
    roster_list = []

    # initialize roster basic info
    for data in roster_data:
        temp_roster = Roster(data[0], data[1], data[2])
        roster_list.append(temp_roster)

    return roster_list


# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

def get_absolute_file_paths(directory):
    list_of_files = []
    for dir_path, _, file_names in os.walk(directory):
        for f in file_names:
            list_of_files.append(os.path.abspath(os.path.join(dir_path, f)))
    return list_of_files


# -------------------------------------------------------------------------------------------
# returns a list of GameInfo Objects
# -------------------------------------------------------------------------------------------

def load_game_info_list(file_paths):
    game_info_list = []

    for file in file_paths:
        print('Scraping ' + file)
        game_info = GameInfo()
        game_info.scrapeBoxScore(file)

        for dp in game_info.dataPointList:

            dp.cleanText()

            if dp.level == 2:

                player = game_info.parsePlayer(dp.text)
                game_info.awayPlayerList.append(player)

            elif dp.level == 3:

                player = game_info.parsePlayer(dp.text)
                game_info.homePlayerList.append(player)

            elif dp.level > 5 and dp.level < (int(game_info.innings) * 2 + 6):
                ev = Event()
                ev.origText = dp.text
                ev.curText = dp.text.lower()
                ev.inning = int((dp.level - 4) / 2)

                ev.awayTeam = game_info.awayTeamId
                ev.homeTeam = game_info.homeTeamId

                if dp.level % 2 == 0:
                    ev.batterTeam = game_info.awayTeamId
                    ev.pitcherTeam = game_info.homeTeamId
                    game_info.eventList.append(ev)
                else:
                    ev.batterTeam = game_info.homeTeamId
                    ev.pitcherTeam = game_info.awayTeamId
                    game_info.eventList.append(ev)
            else:
                pass
        print('Scraping Successful')
        game_info_list.append(game_info)

    return game_info_list


# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

def write_to_json_file(file_path, data, variable_name):
    with open(file_path, 'w') as outfile:
        outfile.write('var ' + variable_name + ' = ')
        json.dump(data, outfile)
        outfile.write(';')


# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

def get_roster_by_id(team_id, roster_list):
    for roster in roster_list:
        if team_id == roster.teamId:
            return roster
    raise ValueError('#team is not in #rosterList: ' + team_id)


# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

def write_roster_data(roster_list):
    roster_json = {}

    for roster in roster_list:
        roster_json[roster.teamId] = roster.player_list_to_json()

    write_to_json_file('RosterData.js', roster_json, 'rosterData')

