from BaseRunning import BaseRunning
from Substitution import Substitution
from Fielding import Fielding
from Player import Player
import json

class Event:

    def __init__(self):
        self.origText = ""
        self.curText = ""

        self.homeTeamId = ""
        self.awayTeamId = ""

        self.gameDay = ""
        self.gameYear = ""
        self.gameMonth = ""
        self.gameHour = ""

        self.batterId = ""
        self.batterFirstName = ""
        self.batterLastName = ""
        self.batterTeamId = ""

        self.pitcherId = ""
        self.pitcherFirstName = ""
        self.pitcherLastName = ""
        self.pitcherTeamId = ""

        self.inning = ""
        self.outs = ""
        self.menOnBase = ""
        self.inningOrder = ""

        self.batterTeamScore = ""
        self.pitcherTeamScore = ""
        self.starterReliever = ""

        self.result = ""
        self.direction = ""
        self.balls = ""
        self.strikes = ""
        self.pitchSequence = ""
        self.runsBattedIn = ""

        self.advancedMenOnBase = ""

        self.onFirst = None
        self.onSecond = None
        self.onThird = None
        self.substitution = None
        self.baseRunningList = []
        self.fieldingList = []

    def initializeGameInfo(self, gameInfo):
        self.homeTeamId = gameInfo.homeTeamId
        self.awayTeamId = gameInfo.awayTeamId

        self.gameDay = gameInfo.gameDay
        self.gameYear = gameInfo.gameYear
        self.gameMonth = gameInfo.gameMonth
        self.gameHour = gameInfo.gameHour

        return self

    def initializeGameSituationInfo(self, gameSituation):

        self.batterId = gameSituation.currentBatter.playerId
        self.batterFirstName = gameSituation.currentBatter.firstName
        self.batterLastName = gameSituation.currentBatter.lastName

        self.pitcherId = gameSituation.currentPitcher.playerId
        self.pitcherFirstName = gameSituation.currentPitcher.firstName
        self.pitcherLastName = gameSituation.currentPitcher.lastName

        self.inning = gameSituation.inning
        self.outs = gameSituation.outs
        self.inningOrder = gameSituation.inningOrder

        if gameSituation.isHomeBatting:
            self.batterTeamScore = gameSituation.homeScore
            self.pitcherTeamScore = gameSituation.awayScore

            self.batterTeamId = gameSituation.homeTeamId
            self.pitcherTeamId = gameSituation.awayTeamId

            if gameSituation.isAwayStarter:
                self.starterReliever = "S"
            else:
                self.starterReliever = "R"

        else:
            self.batterTeamScore = gameSituation.awayScore
            self.pitcherTeamScore = gameSituation.homeScore

            self.batterTeamId = gameSituation.awayTeamId
            self.pitcherTeamId = gameSituation.homeTeamId

            if gameSituation.isHomeStarter:
                self.starterReliever = "S"
            else:
                self.starterReliever = "R"

    def addBaseRunning(self, br):
        self.baseRunningList.append(br)

    def addFielding(self, play):
        self.fieldingList.append(play)

    def cleanString(self, text):
        return text.replace(" ", "").replace(".", "").replace(",", "")

    def identifyName(self, text):
        text = text.strip()
        nameSearch = text.split(" ")
        name = nameSearch[0]

        if len(name) == 1:
            name += " " + nameSearch[1]
        elif name[-1] == ",":
            name = name + " " + nameSearch[1]
        elif name[1] == ".":
            name = name + " " + nameSearch[1]
        elif len(nameSearch) > 1 and nameSearch[1][-1] == ",":
            if nameSearch[1] in ["scored,", "walked,", "homered,", "singled,", "doubled,", "tripled,"]:
                pass
            else:
                name =  name + " " + nameSearch[1] + " " + nameSearch[2]
        else:
            pass

        return name

    def removeName(self, text):
        text = text.strip()
        nameSearch = text.split(" ")
        name = nameSearch[0]
        if len(name) == 1:
            text = text.replace(name + " " + nameSearch[1], "")
        elif name[-1] == ",":
            text = text.replace(name + ", " +nameSearch[1], "")
        elif name[1] == ".":
            text = text.replace(name + ". " + nameSearch[1], "")
        elif len(nameSearch) > 1 and nameSearch[1][-1] == ",":
            if nameSearch[1] in ["scored,", "walked,", "homered,", "singled,", "doubled,", "tripled,"]:
                text = text.replace(name, "")
            else:
                text = text.replace(name + " " + nameSearch[1] + " " + nameSearch[2], "")
        else:
            text = text.replace(name, "")

        return text

    def hasName(self, text, firstName, lastName):
        if len(text) == 0:
            return False
        elif text[1] == ".":
            if text[3] == ".":
                text = text[5:]
            else:
                text = text[3:]

        if lastName.lower() in text:
            text = text.replace(lastName.lower(), "")

            if text[0] == ",":
                if firstName and len(firstName) > 2 and firstName.lower() in text:
                    text = text.replace(firstName.lower(), "")
                    text = text[3:]
                elif text[3] == ".":
                    text = text[5:]
                else:
                    text = text[4:]
            return True
        else:
            return False

    def parseBallsStrikes(self, text):
        if "(0-0" in text:
            self.balls = "0"
            self.strikes = "0"
            text = text.replace("(0-0", "")
        elif "(0-1" in text:
            self.balls = "0"
            self.strikes = "1"
            text = text.replace("(0-1", "")
        elif "(0-2" in text:
            self.balls = "0"
            self.strikes = "2"
            text = text.replace("(0-2", "")
        elif "(1-0" in text:
            self.balls = "1"
            self.strikes = "0"
            text = text.replace("(1-0", "")
        elif "(1-1" in text:
            self.balls = "1"
            self.strikes = "1"
            text = text.replace("(1-1", "")
        elif "(1-2" in text:
            self.balls = "1"
            self.strikes = "2"
            text = text.replace("(1-2", "")
        elif "(2-0" in text:
            self.balls = "2"
            self.strikes = "0"
            text = text.replace("(2-0", "")
        elif "(2-1" in text:
            self.balls = "2"
            self.strikes = "1"
            text = text.replace("(2-1", "")
        elif "(2-2" in text:
            self.balls = "2"
            self.strikes = "2"
            text = text.replace("(2-2", "")
        elif "(3-0" in text:
            self.balls = "3"
            self.strikes = "0"
            text = text.replace("(3-0", "")
        elif "(3-1" in text:
            self.balls = "3"
            self.strikes = "1"
            text = text.replace("(3-1", "")
        elif "(3-2" in text:
            self.balls = "3"
            self.strikes = "2"
            text = text.replace("(3-2", "")
        else:
            self.balls = "5"
            self.strikes = "5"

        if ")" in text and "(" not in text:
            endIndex = text.find(")") - 1
            pitchSequence = ""
            while text[endIndex] != " ":
                pitchSequence = text[endIndex] + pitchSequence
                endIndex -= 1
            text = text.replace(pitchSequence + ")", "")

            if pitchSequence != "":
                self.pitchSequence = pitchSequence

        return text

    def setBaseRunnerPlayerInfo(self, gameSituation):
        battingLineUp = None
        if gameSituation.isHomeBatting:
            battingLineUp = gameSituation.homeLineUp
        else:
            battingLineUp = gameSituation.awayLineUp

        for br in self.baseRunningList:
            tempPlayerInfo = battingLineUp.searchRoster(br.name)
            if tempPlayerInfo.playerId == "":
                raise ValueError('Blank Player ID')
            br.player = battingLineUp.getPlayer(tempPlayerInfo)


        self.onFirst = gameSituation.onFirst
        self.onSecond = gameSituation.onSecond
        self.onThird = gameSituation.onThird

        return self

    def parseRBI(self, text):
        if " 2 rbi" in text:
            text = text.replace("2 rbi", "")
            self.runsBattedIn = "2"
        elif " 3 rbi" in text:
            text = text.replace("3 rbi", "")
            self.runsBattedIn = "3"
        elif " 4 rbi" in text:
            text = text.replace("4 rbi", "")
            self.runsBattedIn = "4"
        elif " rbi" in text:
            text = text.replace("rbi", "")
            self.runsBattedIn = "1"
        else:
            self.runsBattedIn = "0"
        return text

    def parseDirection(self, text):

        infoArr = text.split(';')

        direction = ""
        textToReplace = ""

        if "down the rf line" in infoArr[0]:
            direction = "2.5"
            textToReplace = "down the rf line"
        elif "down the lf line" in infoArr[0]:
            direction = "4.5"
            textToReplace = "down the lf line"
        elif "through the left side" in infoArr[0]:
            direction = "5.5"
            textToReplace = "through the left side"
        elif "through the right side" in infoArr[0]:
            direction = "3.5"
            textToReplace = "through the right side"
        elif "up the middle" in infoArr[0]:
            direction = "6.5"
            textToReplace = "up the middle"
        elif "to left center" in infoArr[0]:
            direction = "7.5"
            textToReplace = "to left center"
        elif "to right center" in infoArr[0]:
            direction = "8.5"
            textToReplace = "to right center"
        elif "to pitcher" in infoArr[0]:
            direction = "1"
            textToReplace = "to pitcher"
        elif "to catcher" in infoArr[0]:
            direction = "2"
            textToReplace = "to catcher"
        elif "to first base" in infoArr[0]:
            direction = "3"
            textToReplace = "to first base"
        elif "to second base" in infoArr[0]:
            direction = "4"
            textToReplace = "to second base"
        elif "to third base" in infoArr[0]:
            direction = "5"
            textToReplace = "to third base"
        elif "to shortstop" in infoArr[0]:
            direction = "6"
            textToReplace = "to shortstop"
        elif "to left field" in infoArr[0]:
            direction = "7"
            textToReplace = "to left field"
        elif "to center field" in infoArr[0]:
            direction = "8"
            textToReplace = "to center field"
        elif "to right field" in infoArr[0]:
            direction = "9"
            textToReplace = "to right field"
        elif "to 1b unassisted" in infoArr[0]:
            direction = "3"
            textToReplace = "to 1b unassisted"
        else:
            positionKeys = [" p ", " c ", " 1b ", " 2b ", " 3b ", " ss ", " lf ", " cf ", " rf "]
            keysFound = []
            locations = []

            for key in positionKeys:
                if key in infoArr[0] or (key[:-1]+",") in infoArr[0]:
                    keysFound.append(key)
                    locations.append(infoArr[0].find(key))

            direction = ""
            while len(locations) > 0:
                minLoc = 500
                minIndex = 0
                i = 0
                for loc in locations:
                    if loc < minLoc:
                        minLoc = loc
                        minIndex = i
                    i += 1

                direction += self.getPositionInteger(keysFound[minIndex]) + "-"

                keysFound.pop(minIndex)
                locations.pop(minIndex)

            if direction != "":
                direction = direction[:-1]

        if direction != "":
            infoArr[0] = infoArr[0].replace(textToReplace, "")
            self.direction = direction

        parseText = ""
        for t in infoArr:
            parseText += t + ";"

        return parseText[:-1]

    def getPositionInteger(self, posText):
        posText = posText.strip()

        if posText == "p" or posText == "pitcher":
            return "1"
        elif posText == "c" or posText == "catcher":
            return "2"
        elif posText == "1b" or posText == "first base":
            return "3"
        elif posText == "2b" or posText == "second base":
            return "4"
        elif posText == "3b" or posText == "third base":
            return "5"
        elif posText == "ss" or posText == "shortstop":
            return "6"
        elif posText == "lf" or posText == "left field":
            return "7"
        elif posText == "cf" or posText == "center field":
            return "8"
        elif posText == "rf" or posText == "right field":
            return "9"

    def parseSubstitution(self, text):
        infoArr = text.split(";")
        hasNameIn = False
        hasNameOut = False
        textToReplace = ""
        positionIn = ""

        if "/" == infoArr[0][0]:
            #TODO: Assumption, only deals with player taken out of game, so nothing needs to be done
            infoArr[0] = ""
        elif "pinch hit for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "pinch hit for "
            positionIn = "PH"
        elif "pinch hit" in infoArr[0]:
            hasNameIn = True
            textToReplace = "pinch hit"
            positionIn = "PH"
        elif "pinch ran for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "pinch ran for "
            positionIn = "PR"
        elif "to 3b for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "to 3b for "
            positionIn = "5"
        elif "to cf for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "to cf for "
            positionIn = "8"
        elif "to lf for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "to lf for "
            positionIn = "7"
        elif "to rf for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "to rf for "
            positionIn = "9"
        elif "to 1b for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "to 1b for "
            positionIn = "3"
        elif "to 2b for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "to 2b for "
            positionIn = "4"
        elif "to ss for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "to ss for "
            positionIn = "6"
        elif "to dh for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "to dh for "
            positionIn = "10"
        elif "to dh" in infoArr[0]:
            hasNameIn = True
            textToReplace = "to dh"
            positionIn = "10"
        elif "to p for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "to p for "
            positionIn = "1"
        elif "to c for " in infoArr[0]:
            hasNameIn = True
            hasNameOut = True
            textToReplace = "to c for "
            positionIn = "2"
        elif "to c." in infoArr[0] and " out " not in infoArr[0] and " popped " not in infoArr[0]:
            hasNameIn = True
            textToReplace = "to c."
            positionIn = "2"
        elif "to p." in infoArr[0] and " out " not in infoArr[0] and " popped " not in infoArr[0]:
            hasNameIn = True
            textToReplace = "to p."
            positionIn = "1"
        elif "to 1b." in infoArr[0] and " out " not in infoArr[0] and " popped " not in infoArr[0]:
            hasNameIn = True
            textToReplace = "to 1b."
            positionIn = "3"
        elif "to 2b." in infoArr[0] and " out " not in infoArr[0] and " popped " not in infoArr[0]:
            hasNameIn = True
            textToReplace = "to 2b."
            positionIn = "4"
        elif "to 3b." in infoArr[0] and " out " not in infoArr[0] and " popped " not in infoArr[0]:
            hasNameIn = True
            textToReplace = "to 3b."
            positionIn = "5"
        elif "to ss." in infoArr[0] and " out " not in infoArr[0] and " popped " not in infoArr[0]:
            hasNameIn = True
            textToReplace = "to ss."
            positionIn = "6"
        elif "to lf." in infoArr[0] and " out " not in infoArr[0] and " popped " not in infoArr[0]:
            hasNameIn = True
            textToReplace = "to lf."
            positionIn = "7"
        elif "to cf." in infoArr[0] and " out " not in infoArr[0] and " popped " not in infoArr[0]:
            hasNameIn = True
            textToReplace = "to cf."
            positionIn = "8"
        elif "to rf." in infoArr[0] and " out " not in infoArr[0] and " popped " not in infoArr[0]:
            hasNameIn = True
            textToReplace = "to rf."
            positionIn = "9"


        if hasNameIn:
            self.substitution = Substitution()

            nameIn = self.identifyName(infoArr[0])

            infoArr[0] = infoArr[0].replace(nameIn, "")
            infoArr[0] = infoArr[0].strip()
            infoArr[0] = infoArr[0].replace(textToReplace, "")

            self.substitution.playerNameIn = nameIn.replace(".", "")
            self.substitution.positionIn = positionIn

            if hasNameOut:
                nameOut = self.identifyName(infoArr[0])
                infoArr[0] = infoArr[0].replace(nameOut, "")
                self.substitution.playerNameOut = nameOut.replace(".", "")

            return ""
        else:
            parseText = ""
            for t in infoArr:
                parseText += t + ";"

            return parseText[:-1]

    def parseReview(self, text):
        infoArr = text.split(";")

        if "no play" in infoArr[0].lower():
            infoArr[0] = ""
            return ""
        elif "under review" in infoArr[0].lower():
            infoArr[0] = ""
            return ""
        elif "call stands" in infoArr[0].lower() or "play stands as called" in infoArr[0].lower():
            infoArr[0] = ""
            return ""
        elif "ruled out" in infoArr[0].lower():
            infoArr[0] = ""
            return ""
        elif "ejected" in infoArr[0]:
            infoArr[0] = ""
            return ""
        else:
            return text

    def parseAppearance(self):

        infoArr = self.curText.split(";")
        name = ""
        hasDirection = True

        if "dropped foul ball" in infoArr[0]:

            self.result = "DFB"

        elif infoArr[0] != "":

            name = self.identifyName(infoArr[0])
            infoArr[0] = self.removeName(infoArr[0])

        if "bunt" in infoArr[0]:

            infoArr[0] = infoArr[0].replace("bunt", "")

            if "sac" in infoArr[0]:

                self.result = "SACB"
                infoArr[0] = infoArr[0].replace("sac", "")

                if "grounded out" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace("grounded out", "")
                elif "out at first" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace("out at first", "")
                elif "reached on a fielder's choice" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace("reached on a fielder's choice", "")
                    self.result = "SACBFC"
                elif "reached on an error" in infoArr[0]:
                    eStr = "reached on an error "
                    self.result = "SACBROE"

                    if eStr + "by p" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by p", "")
                        self.direction = "1"
                    elif eStr + "by cf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by cf", "")
                        self.direction = "8"
                    elif eStr + "by c " in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by c", "")
                        self.direction = "2"
                    elif eStr + "by 1b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 1b", "")
                        self.direction = "3"
                    elif eStr + "by 2b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 2b", "")
                        self.direction = "4"
                    elif eStr + "by 3b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 3b", "")
                        self.direction = "5"
                    elif eStr + "by ss" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by ss", "")
                        self.direction = "6"
                    elif eStr + "by lf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by lf", "")
                        self.direction = "7"
                    elif eStr + "by rf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by rf", "")
                        self.direction = "9"
                    else:
                        raise ValueError("Error parseAppearance muffed throw")

                elif "reached on a throwing error" in infoArr[0]:
                    eStr = "reached on a throwing error "
                    self.result = "SACBROE"

                    if eStr + "by p" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by p", "")
                        self.direction = "1"
                    elif eStr + "by cf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by cf", "")
                        self.direction = "8"
                    elif eStr + "by c" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by c", "")
                        self.direction = "2"
                    elif eStr + "by 1b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 1b", "")
                        self.direction = "3"
                    elif eStr + "by 2b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 2b", "")
                        self.direction = "4"
                    elif eStr + "by 3b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 3b", "")
                        self.direction = "5"
                    elif eStr + "by ss" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by ss", "")
                        self.direction = "6"
                    elif eStr + "by lf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by lf", "")
                        self.direction = "7"
                    elif eStr + "by rf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by rf", "")
                        self.direction = "9"
                    else:
                        raise ValueError("Error parseAppearance muffed throw")

                elif "reached on a fielding error" in infoArr[0]:
                    eStr = "reached on a fielding error "
                    self.result = "SACBROE"

                    if eStr + "by p" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by p", "")
                        self.direction = "1"
                    elif eStr + "by cf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by cf", "")
                        self.direction = "8"
                    elif eStr + "by c" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by c", "")
                        self.direction = "2"
                    elif eStr + "by 1b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 1b", "")
                        self.direction = "3"
                    elif eStr + "by 2b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 2b", "")
                        self.direction = "4"
                    elif eStr + "by 3b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 3b", "")
                        self.direction = "5"
                    elif eStr + "by ss" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by ss", "")
                        self.direction = "6"
                    elif eStr + "by lf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by lf", "")
                        self.direction = "7"
                    elif eStr + "by rf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by rf", "")
                        self.direction = "9"
                    else:
                        raise ValueError("Error parseAppearance fielding error SAC")

                    infoArr[0] = self.cleanString(infoArr[0])
                else:
                    pass

            elif "singled" in infoArr[0]:

                self.result = "BS"
                infoArr[0] = infoArr[0].replace("singled", "")

            elif "popped up" in infoArr[0]:

                self.result = "BO"
                infoArr[0] = infoArr[0].replace("popped up", "")

            elif "grounded out" in infoArr[0]:

                self.result = "BO"
                infoArr[0] = infoArr[0].replace("grounded out", "")

            elif "reached on an error" in infoArr[0]:
                eStr = "reached on an error "
                self.result = "BROE"

                if eStr + "by p" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace(eStr + "by p", "")
                    self.direction = "1"
                elif eStr + "by cf" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace(eStr + "by cf", "")
                    self.direction = "8"
                elif eStr + "by c " in infoArr[0]:
                    infoArr[0] = infoArr[0].replace(eStr + "by c", "")
                    self.direction = "2"
                elif eStr + "by 1b" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace(eStr + "by 1b", "")
                    self.direction = "3"
                elif eStr + "by 2b" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace(eStr + "by 2b", "")
                    self.direction = "4"
                elif eStr + "by 3b" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace(eStr + "by 3b", "")
                    self.direction = "5"
                elif eStr + "by ss" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace(eStr + "by ss", "")
                    self.direction = "6"
                elif eStr + "by lf" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace(eStr + "by lf", "")
                    self.direction = "7"
                elif eStr + "by rf" in infoArr[0]:
                    infoArr[0] = infoArr[0].replace(eStr + "by rf", "")
                    self.direction = "9"
                else:
                    raise ValueError("Error parseAppearance muffed throw")

            elif "fouled out" in infoArr[0]:

                self.result = "BO"
                infoArr[0] = infoArr[0].replace("fouled out", "")

            elif "reached on a fielder's choice" in infoArr[0]:

                self.result = "FC"
                infoArr[0] = infoArr[0].replace("reached on a fielder's choice", "")

            elif "struck out swinging" in infoArr[0]:

                self.result = "BKO"
                self.direction = "0"
                infoArr[0] = infoArr[0].replace("struck out swinging", "")

            elif "out at first" in infoArr[0]:

                self.result = "BO"
                self.direction = "3"
                infoArr[0] = infoArr[0].replace("out at first", "")

            elif "popped into double play" in infoArr[0]:

                self.result = "BO"
                infoArr[0] = infoArr[0].replace("popped into double play", "")

            elif "grounded into double play" in infoArr[0]:

                self.result = "BO"
                infoArr[0] = infoArr[0].replace("grounded into double play", "")

            else:
                print(infoArr[0])
                raise ValueError('ERROR parseAppeareance Missing bunt')


        elif "struck out" in infoArr[0]:

            infoArr[0] = infoArr[0].replace("struck out", "")

            if " looking" in infoArr[0]:

                self.result = "KL"
                self.direction = "0"
                infoArr[0] = infoArr[0].replace(" looking", "")

            elif " swinging" in infoArr[0]:

                self.result = "KS"
                self.direction = "0"
                infoArr[0] = infoArr[0].replace(" swinging", "")

                if "reached first on a wild pitch" in infoArr[0]:

                    infoArr[0] = infoArr[0].replace("reached first on a wild pitch", "")
                    self.result = self.result + "WP"

                elif "reached first on a passed ball" in infoArr[0]:

                    infoArr[0] = infoArr[0].replace("reached first on a passed ball", "")
                    self.result = self.result + "PB"

                elif "out at first" in infoArr[0]:

                    infoArr[0] = infoArr[0].replace("out at first", "")

                elif "reached first on a throwing error" in infoArr[0]:

                    eStr = "reached first on a throwing error "
                    self.result = "KSROE"

                    if eStr + "by p" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by p", "")
                        self.direction = "1"
                    elif eStr + "by cf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by cf", "")
                        self.direction = "8"
                    elif eStr + "by c" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by c", "")
                        self.direction = "2"
                    elif eStr + "by 1b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 1b", "")
                        self.direction = "3"
                    elif eStr + "by 2b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 2b", "")
                        self.direction = "4"
                    elif eStr + "by 3b" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by 3b", "")
                        self.direction = "5"
                    elif eStr + "by ss" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by ss", "")
                        self.direction = "6"
                    elif eStr + "by lf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by lf", "")
                        self.direction = "7"
                    elif eStr + "by rf" in infoArr[0]:
                        infoArr[0] = infoArr[0].replace(eStr + "by rf", "")
                        self.direction = "9"
                    else:
                        raise ValueError("Error parseAppearance muffed throw")

            else:
                raise ValueError('ERROR: parseAppearance() Neither Swinging Nor Looking?')

        elif "popped up" in infoArr[0]:

            if ", sf," in infoArr[0]:

                self.result = "SACF"
                infoArr[0] = infoArr[0].replace(", sf,", "").replace("popped up", "")

            else:

                self.result = "FO"
                infoArr[0] = infoArr[0].replace("popped up", "")

        elif "singled" in infoArr[0]:

            self.result = "1B"
            infoArr[0] = infoArr[0].replace("singled", "")

        elif "doubled" in infoArr[0]:

            if "ground-rule" in infoArr[0]:
                infoArr[0] = infoArr[0].replace("ground-rule", "")

            self.result = "2B"
            infoArr[0] = infoArr[0].replace("doubled", "")

        elif "tripled" in infoArr[0]:

            self.result = "3B"
            infoArr[0] = infoArr[0].replace("tripled", "")

        elif "homered" in infoArr[0]:

            self.result = "HR"
            infoArr[0] = infoArr[0].replace("homered", "")

            br = BaseRunning(Player())
            br.playType = "RS"
            br.name = name

            if 'unearned' in infoArr[0]:
                br.playType = "RS U"

            self.baseRunningList.append(br)

        elif "grounded out" in infoArr[0]:

            self.result = "GO"
            infoArr[0] = infoArr[0].replace("grounded out", "")

        elif "flied out" in infoArr[0]:

            if ", sf," in infoArr[0]:

                self.result = "SACF"
                infoArr[0] = infoArr[0].replace(", sf,", "").replace("flied out", "")

            else:

                self.result = "FO"
                infoArr[0] = infoArr[0].replace("flied out", "")

        elif "fouled out" in infoArr[0]:

            if ", sf," in infoArr[0]:

                self.result = "SACF"
                infoArr[0] = infoArr[0].replace(", sf,", "").replace("fouled out", "")

            else:

                self.result = "FO"
                infoArr[0] = infoArr[0].replace("fouled out", "")

        elif "lined out" in infoArr[0]:

            self.result = "LO"
            infoArr[0] = infoArr[0].replace("lined out", "")

        elif "infield fly" in infoArr[0]:

            self.result = "FO"
            infoArr[0] = infoArr[0].replace("infield fly", "")

        elif "out at first" in infoArr[0] and "picked off" not in infoArr[0]:

            if self.balls:

                self.result = "GO"
                infoArr[0] = infoArr[0].replace("out at first", "")

        elif "grounded into double play" in infoArr[0]:

            self.result = "GDP"
            infoArr[0] = infoArr[0].replace("grounded into double play", "")

        elif "hit into double play" in infoArr[0]:

            self.result = "LDP"
            infoArr[0] = infoArr[0].replace("hit into double play", "")

        elif "lined into double play" in infoArr[0]:

            self.result = "HDP"
            infoArr[0] = infoArr[0].replace("lined into double play", "")

        elif "flied into double play" in infoArr[0]:

            self.result = "FDP"
            infoArr[0] = infoArr[0].replace("flied into double play", "")

        elif "reached on a fielder's choice" in infoArr[0]:

            self.result = "FC"
            infoArr[0] = infoArr[0].replace("reached on a fielder's choice", "")

        elif "walked" in infoArr[0]:

            if "intentionally" in infoArr[0]:

                self.result = "IBB"
                infoArr[0] = infoArr[0].replace("intentionally", "")

            else:

                self.result = "BB"

            infoArr[0] = infoArr[0].replace("walked", "")

        elif "hit by pitch" in infoArr[0]:

            self.result = "HBP"
            infoArr[0] = infoArr[0].replace("hit by pitch", "")

        elif "reached on a dropped fly" in infoArr[0]:

            eStr = "reached on a dropped fly "
            self.result = "ROE"

            if eStr + "by p" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "to p", "")
                self.direction = "1"
            elif eStr + "by cf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "to cf", "")
                self.direction = "8"
            elif eStr + "by c " in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "to c", "")
                self.direction = "2"
            elif eStr + "by 1b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "to 1b", "")
                self.direction = "3"
            elif eStr + "by 2b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "to 2b", "")
                self.direction = "4"
            elif eStr + "by 3b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "to 3b", "")
                self.direction = "5"
            elif eStr + "by ss" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "to ss", "")
                self.direction = "6"
            elif eStr + "by lf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "to lf", "")
                self.direction = "7"
            elif eStr + "by rf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "to rf", "")
                self.direction = "9"
            else:
                raise ValueError("Error parseAppearance reached on an error")

        elif "reached on an error" in infoArr[0]:

            eStr = "reached on an error "
            self.result = "ROE"

            if eStr + "by p" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by p", "")
                self.direction = "1"
            elif eStr + "by cf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by cf", "")
                self.direction = "8"
            elif eStr + "by c " in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by c", "")
                self.direction = "2"
            elif eStr + "by 1b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 1b", "")
                self.direction = "3"
            elif eStr + "by 2b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 2b", "")
                self.direction = "4"
            elif eStr + "by 3b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 3b", "")
                self.direction = "5"
            elif eStr + "by ss" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by ss", "")
                self.direction = "6"
            elif eStr + "by lf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by lf", "")
                self.direction = "7"
            elif eStr + "by rf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by rf", "")
                self.direction = "9"
            else:
                raise ValueError("Error parseAppearance reached on an error")

        elif "reached on catcher's interference" in infoArr[0]:

            self.result = "CI"
            infoArr[0] = infoArr[0].replace("reached on catcher's interference", "")

            self.direction = "0"

        elif "reached on a throwing error" in infoArr[0]:

            eStr = "reached on a throwing error "
            self.result = "ROE"

            if eStr + "by p" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by p", "")
                self.direction = "1"
            elif eStr + "by cf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by cf", "")
                self.direction = "8"
            elif eStr + "by c " in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by c", "")
                self.direction = "2"
            elif eStr + "by 1b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 1b", "")
                self.direction = "3"
            elif eStr + "by 2b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 2b", "")
                self.direction = "4"
            elif eStr + "by 3b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 3b", "")
                self.direction = "5"
            elif eStr + "by ss" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by ss", "")
                self.direction = "6"
            elif eStr + "by lf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by lf", "")
                self.direction = "7"
            elif eStr + "by rf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by rf", "")
                self.direction = "9"
            else:
                raise ValueError("Error parseAppearance reach on throwing error")

        elif "reached on a fielding error" in infoArr[0]:

            eStr = "reached on a fielding error "
            self.result = "ROE"

            if eStr + "by p" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by p", "")
                self.direction = "1"
            elif eStr + "by cf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by cf", "")
                self.direction = "8"
            elif eStr + "by c " in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by c", "")
                self.direction = "2"
            elif eStr + "by 1b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 1b", "")
                self.direction = "3"
            elif eStr + "by 2b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 2b", "")
                self.direction = "4"
            elif eStr + "by 3b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 3b", "")
                self.direction = "5"
            elif eStr + "by ss" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by ss", "")
                self.direction = "6"
            elif eStr + "by lf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by lf", "")
                self.direction = "7"
            elif eStr + "by rf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by rf", "")
                self.direction = "9"
            else:
                raise ValueError("Error parseAppearance muffed throw")

        elif "reached on a muffed throw" in infoArr[0]:
            eStr = "reached on a muffed throw "
            self.result = "ROE"

            if eStr + "by p" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by p", "")
                self.direction = "1"
            elif eStr + "by cf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by cf", "")
                self.direction = "8"
            elif eStr + "by c " in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by c", "")
                self.direction = "2"
            elif eStr + "by 1b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 1b", "")
                self.direction = "3"
            elif eStr + "by 2b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 2b", "")
                self.direction = "4"
            elif eStr + "by 3b" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by 3b", "")
                self.direction = "5"
            elif eStr + "by ss" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by ss", "")
                self.direction = "6"
            elif eStr + "by lf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by lf", "")
                self.direction = "7"
            elif eStr + "by rf" in infoArr[0]:
                infoArr[0] = infoArr[0].replace(eStr + "by rf", "")
                self.direction = "9"
            else:
                raise ValueError("Error parseAppearance muffed throw")

        else:
            self.result = "BR"
            self.direction = "0"


        if infoArr[0] != '':
            br = BaseRunning(Player())
            infoArr[0] = br.parseBaseRunning(infoArr[0])
            if name != "":
                br.name = name
                self.baseRunningList.append(br)


        if self.direction == '':
            infoArr[0] = self.parseDirection(infoArr[0])

        if infoArr[0] != '':
            fld = Fielding()
            infoArr[0] = fld.parseFielding(infoArr[0])
            self.fieldingList.append(fld)

        i = 1
        while i < len(infoArr):
            infoArr[i] = infoArr[i].strip()
            name = self.identifyName(infoArr[i])
            infoArr[i] = self.removeName(infoArr[i])

            if name != "":
                br = BaseRunning(Player())
                infoArr[i] = br.parseBaseRunning(infoArr[i])
                br.name = name
                self.baseRunningList.append(br)


            fld = Fielding()
            infoArr[i] = fld.parseFielding(infoArr[i])
            self.fieldingList.append(fld)

            i += 1

        #check to see if info in fielding about direction
        if self.direction == "":
            for f in self.fieldingList:
                if f.position != "":
                    self.direction = f.position[0]

        # direction info is not available
        if self.direction == "":
            self.direction = "-1"

        return self

    def parseMenOnBase(self, gameSituation):
        self.onFirst = gameSituation.onFirst
        self.onSecond = gameSituation.onSecond
        self.onThird= gameSituation.onThird

    def cleanBaseRunningList(self):
        i = 0
        while(i < len(self.baseRunningList)):
            if self.baseRunningList[i].playType == "":
                self.baseRunningList.pop(i)
            elif self.baseRunningList[i].name == "":
                raise ValueError('Missing name')
            else:
                i+=1
        return self

    def eventToJSON(self):

        jsonData = {}

        jsonData['awayTeamId'] = self.awayTeamId
        jsonData['homeTeamId'] = self.homeTeamId

        jsonData['gameDay'] = self.gameDay
        jsonData['gameMonth'] = self.gameMonth
        jsonData['gameYear'] = self.gameYear
        jsonData['gameHour'] = self.gameHour

        jsonData['result'] = self.result
        jsonData['direction'] = self.direction

        jsonData['balls'] = self.balls
        jsonData['strikes'] = self.strikes
        jsonData['inning'] = self.inning
        jsonData['outs'] = self.outs

        jsonData['rbi'] = self.runsBattedIn

        if self.menOnBase == '':
            jsonData['menOnBase'] = '0'
        else:
            jsonData['menOnBase'] = self.menOnBase

        if self.advancedMenOnBase == '':
            jsonData['advancedMenOnBase'] = '0'
        else:
            jsonData['advancedMenOnBase'] = self.advancedMenOnBase

        jsonData['batterId'] = self.batterId
        jsonData['batterFirstName'] = self.batterFirstName
        jsonData['batterLastName'] = self.batterLastName
        jsonData['batterTeam'] = self.batterTeamId
        jsonData['batterTeamScore'] = self.batterTeamScore

        jsonData['pitcherId'] = self.pitcherId
        jsonData['pitcherFirstName'] = self.pitcherFirstName
        jsonData['pitcherLastName'] = self.pitcherLastName
        jsonData['pitcherTeam'] = self.pitcherTeamId
        jsonData['pitcherTeamScore'] = self.pitcherTeamScore
        jsonData['starterReliever'] = self.starterReliever
        jsonData['inningOrder'] = self.inningOrder

        i = 1
        jsonData['baseRunners'] = []
        for br in self.baseRunningList:
            runnerData = {}

            runnerData['result'] = br.playType
            runnerData['runScored'] = br.runs
            runnerData['playerId'] = br.player.playerId
            runnerData['firstName'] = br.player.firstName
            runnerData['lastName'] = br.player.lastName
            runnerData['pitcherResponsible'] = br.pitcherResponsible.playerId

            jsonData['baseRunners'].append(runnerData)
            i += 1

        return jsonData






