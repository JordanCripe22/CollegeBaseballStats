from Player import Player

class Substitution:

    def __init__(self):

        self.playerNameIn = ""
        self.playerNameOut = ""
        self.positionIn = ""

        self.playerIn = Player()
        self.playerOut = Player()

    def show(self):
        print("In:", end=" ")
        print(self.playerNameIn)
        print("Out:", end=" ")
        print(self.playerNameOut)
        print("Pos:", end=" ")
        print(self.positionIn)

    def editLineUp(self, LineUp):

        playerInfoIn = None

        if self.playerNameIn != "":
            playerInfoIn = LineUp.searchRoster(self.playerNameIn)
            #print('player in')
            #print(self.playerNameIn)
            #playerInfoIn.show()

        playerInfoOut = None
        if self.playerNameOut != "":
            playerInfoOut = LineUp.searchRoster(self.playerNameOut)
            #print('player out')
            #playerInfoOut.show()

        isBenchPlayerIn = False
        i = 0
        if playerInfoIn:
            while i < len(LineUp.benchPlayers) and not isBenchPlayerIn:

                benchPlayer = LineUp.benchPlayers[i]

                if benchPlayer.playerId == playerInfoIn.playerId:
                    isBenchPlayerIn = True
                    self.playerIn = LineUp.benchPlayers.pop(i)

                i += 1


        isPositionPlayerIn = False
        positionPlayerInIndex = -1

        if not isBenchPlayerIn:
            i = 0
            while i < len(LineUp.positionPlayers) and not isPositionPlayerIn:

                positionPlayer = LineUp.positionPlayers[i]

                if positionPlayer.playerId == playerInfoIn.playerId:
                    isPositionPlayerIn = True
                    positionPlayerInIndex = i
                    self.playerIn = positionPlayer

                i += 1

        i = 0
        positionPlayerOutIndex = -1

        if playerInfoOut:

            while i < len(LineUp.positionPlayers) and positionPlayerOutIndex < 0:

                positionPlayer = LineUp.positionPlayers[i]
                if positionPlayer.playerId == playerInfoOut.playerId:
                    positionPlayerOutIndex = i
                    self.playerOut = LineUp.positionPlayers.pop(i)
                i += 1

        if isPositionPlayerIn and positionPlayerOutIndex > -1:
            #print('Case: position player out')
            if self.playerIn.curPosition == '1' or self.playerIn.curPosition == '10':
                if positionPlayerInIndex > positionPlayerOutIndex:
                    positionPlayerInIndex -= 1
                else:
                    positionPlayerOutIndex -= 1
                self.playerIn = LineUp.positionPlayers.pop(positionPlayerInIndex)
                LineUp.positionPlayers.insert(positionPlayerOutIndex, self.playerIn)

            if self.positionIn == self.playerIn.curPosition:
                pass
            else:
                self.playerIn.curPosition = self.positionIn
        elif isPositionPlayerIn and positionPlayerOutIndex < 0:
            #Position Change
            #print('Case: position change')
            if self.positionIn == self.playerIn.curPosition:
                pass
            else:
                self.playerIn.curPosition = self.positionIn
                if self.playerIn.curPosition == '1' and len(LineUp.positionPlayers) == 10:
                    LineUp.positionPlayers.pop()

        elif isBenchPlayerIn and positionPlayerOutIndex > -1:
            #Regular Sub
            #print('Case: regular sub 1')
            self.playerIn.curPosition = self.positionIn
            LineUp.positionPlayers.insert(positionPlayerOutIndex, self.playerIn)
        else:
            #print('Case: regular sub 2')
            #print(self.playerNameIn)
            #print(self.playerNameOut)

            self.playerIn.curPosition = self.positionIn
            LineUp.positionPlayers.insert(len(LineUp.positionPlayers), self.playerIn)
            #print(positionPlayerOutIndex)

        #LineUp.show()
        return LineUp
