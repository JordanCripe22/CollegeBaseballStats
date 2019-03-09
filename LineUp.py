from Utils import Utils
class LineUp:

    def __init__(self, roster):

        self.positionPlayers = []
        self.benchPlayers = []
        self.Roster = roster

    def show(self):
        print("on field:")
        for posPlayer in self.positionPlayers:
            posPlayer.show()

        print("on bench:")
        for bePlayer in self.benchPlayers:
            bePlayer.show()
        print("")

    def searchRoster(self, name):
        name_arr = Utils.parse_name_from_str(name)
        for player in self.Roster.playerList:

            splitName = name.split(' ')
            if len(splitName) == 1 and "," in splitName[0]:
                splitName = splitName[0].split(',')
                if splitName[0].lower() == player.lastName.lower() and splitName[1].lower() == player.firstName[0].lower():

                    return player
            elif len(splitName) == 3:
                if splitName[0][-1] == ",":
                    if splitName[0][:-1].lower() == player.lastName.lower():
                        return player
                elif splitName[1][-1] == ",":
                    if splitName[0].lower() + " " + splitName[1][:-1].lower() == player.lastName.lower():
                        return player
            elif splitName[0].lower() == player.lastName.lower():
                if len(splitName) == 1:
                    return player
                else:
                    continue
            elif splitName[0].lower()[:-1] == player.lastName.lower():
                if splitName[1][-1] == ".":
                    if splitName[1][0].lower() == player.firstName[0].lower():
                        return player
                    else:
                        continue
                else:
                    if len(splitName[1]) > 1 and '.' not in splitName[1]:
                        if splitName[1].lower() == player.firstName.lower():
                            return player
                        else:
                            pass
                    elif splitName[1][0].lower() == player.firstName[0].lower():
                        return player
                    else:
                        continue
            elif len(splitName[0]) == 1 and splitName[1].lower() == player.lastName.lower():
                if splitName[0].lower() == player.firstName[0].lower():
                    #print('Found case 4')
                    return player
                else:
                    continue
            elif splitName[0][-1] == "." and splitName[1].lower() == player.lastName.lower():
                if splitName[0][0].lower() == player.firstName[0].lower():
                    #print('Found case 5')
                    return player
                else:
                    continue
        print('searching for: ' + name)
        self.Roster.show()
        raise ValueError('Unable to find in Roster 1:' + name)

    def getPlayer(self, playerInfo):
        for posPlayer in self.positionPlayers:
            if playerInfo.playerId == posPlayer.playerId:
                return posPlayer

        for bePlayer in self.benchPlayers:
            if playerInfo.playerId == bePlayer.playerId:
                return bePlayer

        print('searching for:')
        playerInfo.show()
        self.show()
        raise ValueError('Could Not find Player in Lineup From Player Info: ' )

    def setLineUp(self, playerList):
        for player in playerList:
            playerInfo = self.Roster.getPlayerInfo(player)
            player.playerId = playerInfo.playerId
            player.firstName = playerInfo.firstName
            player.lastName = playerInfo.lastName
            if player.curPosition == 'be':
                self.benchPlayers.append(player)
            else:
                self.positionPlayers.append(player)
        return self




