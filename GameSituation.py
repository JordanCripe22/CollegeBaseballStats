from LineUp import LineUp
from Player import Player
from BaseRunning import BaseRunning

class GameSituation:

    def __init__(self, away_roster, home_roster):

        self.awayTeamId = away_roster.teamId
        self.homeTeamId = home_roster.teamId

        self.homePlayersJSON = []
        self.awayPlayersJSON = []

        self.awayLineUp = LineUp(away_roster)
        self.homeLineUp = LineUp(home_roster)

        self.currentBatter = Player()

        self.currentPitcher = Player()
        self.currentCatcher = Player()
        self.currentFirst = Player()
        self.currentSecond = Player()
        self.currentShort = Player()
        self.currentThird = Player()
        self.currentLeft = Player()
        self.currentCenter = Player()
        self.currentRight = Player()
        self.currentDH = Player()

        self.inning = 1
        self.outs = 0

        self.onFirst = None
        self.onSecond = None
        self.onThird = None

        self.homeIndex = -1
        self.awayIndex = 0

        self.homeScore = 0
        self.awayScore = 0

        self.isHomeBatting = False
        self.inningOrder = 0

        self.isHomeStarter = True
        self.isAwayStarter = True

    def showState(self):
        if self.onFirst:
            print("1st: "+ self.onFirst.player.lastName, end=" ")
        else:
            print("1st: empty" , end=" ")

        if self.onSecond:
            print("2nd: "+ self.onSecond.player.lastName, end=" ")
        else:
            print("2nd: empty" , end=" ")

        if self.onThird:
            print("3rd: "+ self.onThird.player.lastName, end=" ")
        else:
            print("3rd: empty" , end=" ")

        print("outs: " + str(self.outs))
        print("At Bat: " + self.currentBatter.lastName, end=" ")
        print("Pitching: " + self.currentPitcher.lastName)

    def nextBatter(self):
        if self.outs == 3:
            if self.isHomeBatting:
                self.inning+=1
            self.outs = 0
            self.isHomeBatting = not self.isHomeBatting
            self.clearBases()
            self.loadField()
            self.inningOrder = 0
        else:
            self.inningOrder += 1

        if self.isHomeBatting:
            if self.homeIndex < 8:
                self.homeIndex += 1
            else:
                self.homeIndex = 0
        else:
            if self.awayIndex < 8:
                self.awayIndex += 1
            else:
                self.awayIndex = 0

        self.setCurBatter()

    def setCurBatter(self):
        if self.isHomeBatting:
            self.currentBatter = self.homeLineUp.positionPlayers[self.homeIndex]
        else:
            self.currentBatter = self.awayLineUp.positionPlayers[self.awayIndex]
        return self

    def addRun(self):
        if self.isHomeBatting:
            self.homeScore += 1
        else:
            self.awayScore += 1

    def moveToSecond(self, br):
        if self.onFirst and br.player.playerId == self.onFirst.player.playerId:
            br.pitcherResponsible = self.onFirst.pitcherResponsible
            self.onFirst = None

        self.onSecond = br
        return self

    def moveToThird(self, br):

        if self.onFirst and br.player.playerId == self.onFirst.player.playerId:
            br.pitcherResponsible = self.onFirst.pitcherResponsible
            self.onFirst = None
        elif self.onSecond and br.player.playerId == self.onSecond.player.playerId:
            br.pitcherResponsible = self.onSecond.pitcherResponsible
            self.onSecond = None

        self.onThird = br
        return self

    def removeFromBases(self, br):

        if self.onFirst and br.player.playerId == self.onFirst.player.playerId:
            br.pitcherResponsible = self.onFirst.pitcherResponsible
            self.onFirst = None
        elif self.onSecond and br.player.playerId == self.onSecond.player.playerId:
            br.pitcherResponsible = self.onSecond.pitcherResponsible
            self.onSecond = None
        elif self.onThird and br.player.playerId == self.onThird.player.playerId:
            br.pitcherResponsible = self.onThird.pitcherResponsible
            self.onThird = None
        else:
            raise ValueError('Player is not on base' + br.player.playerId)

        return self

    def clearBases(self):
        self.onFirst = None
        self.onSecond = None
        self.onThird = None
        return self

    def loadField(self):
        fieldLineUp = None
        self.setCurBatter()

        if self.isHomeBatting:
            fieldLineUp = self.awayLineUp
        else:
            fieldLineUp = self.homeLineUp

        for player in fieldLineUp.positionPlayers:
            if player.curPosition == "1":
                self.currentPitcher = player
            elif player.curPosition == "2":
                self.currentCatcher = player
            elif player.curPosition == "3":
                self.currentFirst = player
            elif player.curPosition == "4":
                self.currentSecond = player
            elif player.curPosition == "5":
                self.currentThird = player
            elif player.curPosition == "6":
                self.currentShort = player
            elif player.curPosition == "7":
                self.currentLeft = player
            elif player.curPosition == "8":
                self.currentCenter = player
            elif player.curPosition == "9":
                self.currentRight = player
            elif player.curPosition == "10":
                self.currentDH = player
            elif player.curPosition == "PR":
                pass
            elif player.curPosition == "PH":
                pass
            else:
                print("GAME SITUATION loadField Missing position:" + player.curPosition + " Player:" + player.lastName)

    def analyzeSubstitution(self, sub):
        lineUp1 = None
        lineUp2 = None
        isHomeLineup1 = None
        if self.isHomeBatting:

            if sub.positionIn == "1":
                if self.isAwayStarter:
                    self.isAwayStarter = False

            if sub.positionIn == "PH" or sub.positionIn == "PR":
                lineUp1 = self.homeLineUp
                lineUp2 = self.awayLineUp
                isHomeLineup1 = True
            else:
                lineUp1 = self.awayLineUp
                lineUp2 = self.homeLineUp
                isHomeLineup1 = False
        else:

            if sub.positionIn == "1":
                if self.isHomeStarter:
                    self.isHomeStarter = False

            if sub.positionIn == "PH" or sub.positionIn == "PR":
                lineUp1 = self.awayLineUp
                lineUp2 = self.homeLineUp
                isHomeLineup1 = False
            else:
                lineUp1 = self.homeLineUp
                lineUp2 = self.awayLineUp
                isHomeLineup1 = True

        try:

            lineUp1 = sub.editLineUp(lineUp1)
            if isHomeLineup1:
                self.homeLineUp = lineUp1
            else:
                self.awayLineUp = lineUp1

        except Exception:
            lineUp2 = sub.editLineUp(lineUp2)
            if isHomeLineup1:
                self.awayLineUp = lineUp2
            else:
                self.homeLineUp = lineUp2


        if sub.positionIn == "PR":

            if self.onFirst and self.onFirst.player.playerId == sub.playerOut.playerId:
                pinchRunner = BaseRunning(sub.playerIn)
                pinchRunner.pitcherResponsible = self.onFirst.pitcherResponsible
                self.onFirst = pinchRunner

            elif self.onSecond and self.onSecond.player.playerId == sub.playerOut.playerId:

                pinchRunner = BaseRunning(sub.playerIn)
                pinchRunner.pitcherResponsible = self.onSecond.pitcherResponsible
                self.onSecond = pinchRunner

            elif self.onThird and self.onThird.player.playerId == sub.playerOut.playerId:
                pinchRunner = BaseRunning(sub.playerIn)
                pinchRunner.pitcherResponsible = self.onThird.pitcherResponsible
                self.onThird = pinchRunner

            else:
                raise ValueError('pinch runner out not on base' + sub.playerOut.playerId)

        return self

    def analyzeEvent(self, event):
        if self.onFirst:
            event.menOnBase += "1"

        if self.onSecond:
            event.menOnBase += "2"

        if self.onThird:
            event.menOnBase += "3"

        batterBaseRunner = None
        batterBase = None
        batterAssigned = False

        resultInOut = ["FO", "GO", "LO", "BO", "KL", "KS", "GDP", "LDP", "FDP", "HDP", "SACB", "SACF", "BKO"]

        resultInOnFirst = [
            "KSROE", "KSWP", "KSPB", "1B", "BS", "BROE", "BB", "HBP", "IBB", "FC",
            "ROE", "SACBFC", "SACBROE", "CI"
        ]


        result = event.result

        if result in resultInOut:
            self.outs += 1
        elif result in resultInOnFirst:
            batterBaseRunner = BaseRunning(self.currentBatter)
            batterBaseRunner.pitcherResponsible = self.currentPitcher
            batterBase = 1
            #print('base runner to temp first: ' + event.batterLastName)
        elif result == '2B':
            batterBaseRunner = BaseRunning(self.currentBatter)
            batterBaseRunner.pitcherResponsible = self.currentPitcher
            batterBase = 2
            #print('base runner to temp second: ' + event.batterLastName)
        elif result == '3B':
            batterBaseRunner = BaseRunning(self.currentBatter)
            batterBaseRunner.pitcherResponsible = self.currentPitcher
            batterBase = 3
            #print('base runner to temp third: ' + event.batterLastName)
        elif result == 'HR':
            batterBaseRunner = BaseRunning(self.currentBatter)
            batterBaseRunner.pitcherResponsible = self.currentPitcher
            batterBaseRunner.playType = "RS"

            for br in event.baseRunningList:
                if br.player.playerId == self.currentBatter.playerId:
                    batterBaseRunner.playType = "RS U"

            batterBase = 4

        elif result == 'BR':
            #print('BR Result')
            pass
        else:
            raise ValueError("Missing Result: " + event.result)

        event.baseRunningList.reverse()
        for br in event.baseRunningList:
            playType = br.playType
            splitPlayType = playType.split(' ')

            i = 0
            while i < len(splitPlayType):
                if splitPlayType[i] == 'RS':

                    if self.onFirst:
                        if self.onFirst.player.playerId == br.player.playerId:
                            br.pitcherResponsible = self.onFirst.pitcherResponsible

                    elif self.onSecond:
                        if self.onSecond.player.playerId == br.player.playerId:
                            br.pitcherResponsible = self.onSecond.pitcherResponsible

                    elif self.onThird:
                        if self.onThird.player.playerId == br.player.playerId:
                            br.pitcherResponsible = self.onThird.pitcherResponsible

                    elif self.currentBatter.playerId == br.player.playerId:
                        br.pitcherResponsible = self.currentPitcher

                    else:
                        raise ValueError('Player Scored is not on base: ' + br.player.playerId)

                    splitPlayType[i] = "A4"
                    br.runs = '1'
                    self.addRun()
                    i += 1

                elif splitPlayType[i] == "U":
                    splitPlayType.pop(i)
                    br.runs = '1.1'
                    self.addRun()

                else:
                    i += 1



            br.playType = ""
            for pt in splitPlayType:
                br.playType += pt + " "

            br.playType = br.playType[:-1]

            runningOutResults = [
                "TO1", "TO2", "TO3", "TO4", "O1", "O2", "O3", "O4", "OOP", "PO", "CS",
                "PO TO1", "PO TO2", "PO TO3", "PO TO4",
                "CS PO O2", "CS PO O3", "CS PO O4", "CS PO TO1",
                "CS O2", "CS O3", "CS O4",
                "PB3 TO4", "A3 TO4", "A2 TO2", "A2 TO3", "CS OOP", "A3 TO3", "WP2 TO3", "AFE2 TO2"
            ]

            toSecondList = [
                "A2", "PB2", "AT2", "ATE2", "WP2", "BLK2", "AFE2", "SB2",
                "FPO ATE2", "SB2 FPO", "FPO AFE2"
            ]

            toThirdList = [
                "A3", "PB3", "AT3", "ATE3", "WP3", "BLK3", "AFE3", "SB3",
                "SB2 A3", "ATE2 PB3", "WP2 ATE3", "A2 A3", "FPO ATE2 PB3",
                "AFE2 A3", "A2 ATE3", "FPO AFE3", "SB2 ATE3", "ATE2 A3", "FPO ATE2 A3",
                "A2 AFE3", "SB3 FPO", "FPO AFE2 A3", "SB2 WP3", "AT2 ATE3", "AT2 A3", "A2 AT3",
                "FPO ATE3"
            ]

            toHomeList = [
                "A4", "PB4", "AT4", "ATE4", "WP4", "BLK4", "AFE4", "SB4 A4", "SB4 A4 FPO",
                "SB3 A4", "PB3 A4", "A4 WP4", "AFE2 AFE3 A4", "SB3 A4 WP4", "A3 A4",
                "SB4 FPO", "A4 PB4", "A4 BLK4", "FPO A4 ATE4", "A3 A4 ATE4", "SB3 A4 ATE4",
                "A4 ATE4", "AFE2 A4", "ATE2 A4 ATE4"
            ]

            play = br.playType

            if br.player.playerId == self.currentBatter.playerId:
                if batterBaseRunner:
                    if batterBase == 1:
                        self.onFirst = batterBaseRunner
                        batterAssigned = True
                    elif batterBase == 2:
                        self.onSecond = batterBaseRunner
                        batterAssigned = True
                    elif batterBase == 3:
                        self.onThird = batterBaseRunner
                        batterAssigned = True
                    elif batterBase == 4:
                        self.onFirst = batterBaseRunner
                        batterAssigned = True
                else:
                    br.player.show()
                    print(self.currentBatter.playerId)
                    raise ValueError('Base runner is batter but is not on base')


            if play in runningOutResults:
                self.outs += 1
                self.removeFromBases(br)
                #print('player out, remove from bases: ' + br.player.lastName)
            elif play in toSecondList:
                self.moveToSecond(br)
                #print('player to second: ' + br.player.lastName)
            elif play in toThirdList:
                self.moveToThird(br)
                #print('player to third: ' + br.player.lastName)
            elif play in toHomeList:
                self.removeFromBases(br)
                #print('player scored, remove from bases: ' + br.player.lastName)
            else:
                raise ValueError('Missing Base Running Play' + br.playType)

        if not batterAssigned:
            if batterBase == 1:
                self.onFirst = batterBaseRunner
                #print('batter to first: ' + batterBaseRunner.player.lastName)
            elif batterBase == 2:
                self.onSecond = batterBaseRunner
                #print('batter to second: ' + batterBaseRunner.player.lastName)
            elif batterBase == 3:
                self.onThird = batterBaseRunner
                #print('batter to third: ' + batterBaseRunner.player.lastName)
            elif batterBase == 4:
                pass
                #print('batter scored: ' + batterBaseRunner.player.lastName)

        event.baseRunningList.reverse()
        for br in event.baseRunningList:
            if br.player.playerId != self.currentBatter.playerId:
                if br.playType in ["A2", "A2 TO2", "A2 TO3", "A2 A3", "A2 ATE3", "A2 AFE3"]:
                    event.advancedMenOnBase += "2"
                elif br.playType in ["A3", "A3 TO4", "A3 TO3", "A3 A4", "A3 A4 ATE4"]:
                    event.advancedMenOnBase += "3"
                elif br.playType in ["A4"]:
                    event.advancedMenOnBase += "4"

        for fld in event.fieldingList:
            play = fld.playType
            if play == "":
                pass
            elif play == "TE":
                pass
            elif play == "A-6":
                pass
            elif play == "A-5":
                pass
            elif play == "FE":
                pass
            elif play == "E5":
                pass
            elif play == "E3":
                pass
            elif play == "E2":
                pass
            else:
                print("Missing Fielding play: " + play)
        return event




