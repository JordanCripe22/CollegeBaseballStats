
class Roster:

    def __init__(self, team_abbreviation, college, mascot):
        
        self.teamId = team_abbreviation
        self.college = college
        self.mascot = mascot

        self.playerList = []

    def show(self):
        print(self.teamId + ' ' + self.college + ' ' + self.mascot)
        for p in self.playerList:
            p.show()

    def player_list_to_json(self):
        player_list = []
        for player in self.playerList:
            player_json = dict()

            player_json['playerId'] = player.playerId
            player_json['teamId'] = player.teamId
            player_json['lastName'] = player.lastName
            player_json['firstName'] = player.firstName
            player_json['bats'] = player.bats
            player_json['throws'] = player.throws

            player_list.append(player_json)

        return player_list

    @staticmethod
    def parseNameFromStr(name_str):
        name_array = []
        first_name = ""
        last_name = ""

        split_name_str = name_str.split(" ")

        if len(split_name_str) == 1:
            split_comma = split_name_str[0].split(',')

            last_name = split_comma[0]

            if len(split_comma) == 2:
                first_name = split_comma[1]

            elif len(split_comma) == 1:
                pass
            else:
                raise ValueError('Unable to identify ' + name_str)

        elif len(split_name_str) == 2:
            if split_name_str[0][-1] == ",":
                last_name = split_name_str[0][:-1]
                first_name = split_name_str[1]
            else:
                first_name = split_name_str[0]
                last_name = split_name_str[1]
        elif len(split_name_str) == 3:

            if split_name_str[0][-1] == ",":
                last_name = split_name_str[0][:-1]
                if split_name_str[1] == "":
                    first_name = split_name_str[2]
                else:
                    # case of 2 first names
                    first_name = split_name_str[1] + " " + split_name_str[2]
            elif split_name_str[1][-1] == ",":
                last_name = split_name_str[0] + " " + split_name_str[1]
                first_name = split_name_str[2]
            else:
                raise ValueError('ERROR 2 parseNameArray' + str(split_name_str))
        else:
            raise ValueError('ERROR 3 parseNameArray', name_str)

        if "." in first_name:
            first_name = first_name.replace('.', '')

        name_array.append(first_name)
        name_array.append(last_name)

        return name_array

    def hasPlayerId(self, player_id):
        for player in self.playerList:
            if player.playerId == player_id:
                return True
        return False

    def addPlayer(self, player):
        self.playerList.append(player)

    def _getPlayerIndex(self, player):

        player_matched_index = -1
        cur_index = 0

        last_name_matched = 0
        last_name_first_initial_matched = 0

        for p in self.playerList:

            if player.lastName.lower() == p.lastName.lower():

                if len(player.firstName) > 0:

                    if player.firstName.lower() == p.firstName.lower():
                        return cur_index
                    elif player.firstName.lower()[0] == p.firstName.lower()[0]:
                        last_name_first_initial_matched += 1
                        player_matched_index = cur_index

                if last_name_matched == 0:
                    player_matched_index = cur_index

                last_name_matched += 1

            cur_index += 1

        if last_name_matched == 1 or last_name_first_initial_matched == 1:
            return player_matched_index
        else:
            self.show()

            if last_name_matched == 0:
                raise ValueError(
                    'ERROR #1: Reference SolutionManual.txt' + '\n' + 'Missing In Roster: ' +
                    player.lastName + ', ' + player.firstName + ' ' + self.teamId
                )

            if last_name_first_initial_matched > 1:
                raise ValueError(
                    'ERROR #2: Reference SolutionManual.txt' + '\n' + 'Unable to CONFIRM correct player' + '\n'
                                                                                                           'There are multiple players on ' + self.teamId + ' with the Last Name = ' + player.lastName +
                    'and the FIRST INITIAL = ' + player.firstName[0] + '\n' +
                    'Occurances: ' + str(last_name_first_initial_matched)
                )

            if last_name_matched > 1:
                raise ValueError(
                    'ERROR #3: Reference SolutionManual.txt' + '\n' + 'Unable to CONFIRM correct player' + '\n' +
                    'There are multiple players on ' + self.teamId + ' with the LAST NAME = ' + player.lastName + '\n' +
                    'Occurances: ' + str(last_name_matched)
                )

    def getPlayerInfo(self, player):
        player_index = self._getPlayerIndex(player)
        return self.playerList[player_index]

