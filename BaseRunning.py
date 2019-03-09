from Player import Player
from PlayerInfo import PlayerInfo
class BaseRunning:

    def __init__(self, player):

        self.player = player
        self.name = ""
        self.playType = ""
        self.runs = ""
        self.pitcherResponsible = None

    def show(self):

        if self.player and type(self.player) == type(PlayerInfo("","","","","","")):
            raise ValueError('wrong type')
        elif self.player:
            print(self.player.playerId, end=" ")
            print(self.player.lastName, end=" ")
            print(self.playType)
        else:
            print('empty')

    def parseBaseRunning(self, text):
        parseText = text
        if "caught stealing" in text:
            self.playType = "CS "
            parseText = parseText.replace("caught stealing", "")

            if ", picked off" in parseText:
                parseText = parseText.replace(", picked off", "")
                self.playType = self.playType + "PO "

            if "out at second" in parseText:
                parseText = parseText.replace("out at second", "")
                self.playType = self.playType + "O2 "

            elif "out at third" in parseText:
                parseText = parseText.replace("out at third", "")
                self.playType = self.playType + "O3 "

            elif "out at home" in parseText:
                parseText = parseText.replace("out at home", "")
                self.playType = self.playType + "O4 "

        elif ", picked off" in parseText:
            parseText = parseText.replace(", picked off", "")
            self.playType = "PO "
        elif "stole second" in parseText:
            parseText = parseText.replace("stole second", "")
            self.playType = self.playType + "SB2 "
        elif "stole third" in parseText:
            parseText = parseText.replace("stole third", "")
            self.playType = self.playType + "SB3 "
        elif "stole home" in parseText:
            parseText = parseText.replace("stole home", "")
            self.playType = self.playType + "SB4 RS "
        if ", failed pickoff attempt" in parseText:
            parseText = parseText.replace(", failed pickoff attempt", "")
            self.playType = self.playType + "FPO "
        if "advanced to second on a wild pitch" in parseText:
            parseText = parseText.replace("advanced to second on a wild pitch", "")
            self.playType = self.playType + "WP2 "
        elif "advanced to second on a throwing error by p" in parseText:
            #parseText = parseText.replace("advanced to second on a throwing error by p", "")
            self.playType = self.playType + "ATE2 "
        elif "advanced to second on a throwing error by cf" in parseText:
            #parseText = parseText.replace("advanced to second on a throwing error by cf", "")
            self.playType = self.playType + "ATE2 "
        elif "advanced to second on a throwing error by c" in parseText:
            #parseText = parseText.replace("advanced to second on a throwing error by c", "")
            self.playType = self.playType + "ATE2 "
        elif "advanced to second on a throwing error by 1b" in parseText:
            #parseText = parseText.replace("advanced to second on a throwing error by 1b", "")
            self.playType = self.playType + "ATE2 "
        elif "advanced to second on a throwing error by 2b" in parseText:
            #parseText = parseText.replace("advanced to second on a throwing error by 2b", "")
            self.playType = self.playType + "ATE2 "
        elif "advanced to second on a throwing error by 3b" in parseText:
            #parseText = parseText.replace("advanced to second on a throwing error by 3b", "")
            self.playType = self.playType + "ATE2 "
        elif "advanced to second on a throwing error by ss" in parseText:
            #parseText = parseText.replace("advanced to second on a throwing error by ss", "")
            self.playType = self.playType + "ATE2 "
        elif "advanced to second on a throwing error by lf" in parseText:
            #parseText = parseText.replace("advanced to second on a throwing error by lf", "")
            self.playType = self.playType + "ATE2 "
        elif "advanced to second on a throwing error by rf" in parseText:
            #parseText = parseText.replace("advanced to second on a throwing error by rf", "")
            self.playType = self.playType + "ATE2 "

        elif "advanced to second on a fielding error by p" in parseText:
            #parseText = parseText.replace("advanced to second on a fielding error by p", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a fielding error by cf" in parseText:
            #parseText = parseText.replace("advanced to second on a fielding error by cf", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a fielding error by c" in parseText:
            #parseText = parseText.replace("advanced to second on a fielding error by c", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a fielding error by 1b" in parseText:
            #parseText = parseText.replace("advanced to second on a fielding error by 1b", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a fielding error by 2b" in parseText:
            #parseText = parseText.replace("advanced to second on a fielding error by 2b", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a fielding error by 3b" in parseText:
            #parseText = parseText.replace("advanced to second on a fielding error by 3b", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a fielding error by ss" in parseText:
            #parseText = parseText.replace("advanced to second on a fielding error by ss", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a fielding error by lf" in parseText:
            #parseText = parseText.replace("advanced to second on a fielding error by lf", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a fielding error by rf" in parseText:
            #parseText = parseText.replace("advanced to second on a fielding error by rf", "")
            self.playType = self.playType + "AFE2 "

        elif "advanced to second on a muffed throw by p" in parseText:
            #parseText = parseText.replace("advanced to second on a muffed throw by p", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a muffed throw by cf" in parseText:
            #parseText = parseText.replace("advanced to second on a muffed throw by cf", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a muffed throw by c" in parseText:
            #parseText = parseText.replace("advanced to second on a muffed throw by c", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a muffed throw by 1b" in parseText:
            #parseText = parseText.replace("advanced to second on a muffed throw by 1b", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a muffed throw by 2b" in parseText:
            #parseText = parseText.replace("advanced to second on a muffed throw by 2b", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a muffed throw by 3b" in parseText:
            #parseText = parseText.replace("advanced to second on a muffed throw by 3b", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a muffed throw by ss" in parseText:
            #parseText = parseText.replace("advanced to second on a muffed throw by ss", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a muffed throw by lf" in parseText:
            #parseText = parseText.replace("advanced to second on a muffed throw by lf", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on a muffed throw by rf" in parseText:
            #parseText = parseText.replace("advanced to second on a muffed throw by rf", "")
            self.playType = self.playType + "AFE2 "

        elif "advanced to second on an error by p" in parseText:
            #parseText = parseText.replace("advanced to second on an error by p", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on an error by cf" in parseText:
            #parseText = parseText.replace("advanced to second on an error by cf", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on an error by c" in parseText:
            #parseText = parseText.replace("advanced to second on an error by c", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on an error by 1b" in parseText:
            #parseText = parseText.replace("advanced to second on an error by 1b", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on an error by 2b" in parseText:
            #parseText = parseText.replace("advanced to second on an error by 2b", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on an error by 3b" in parseText:
            #parseText = parseText.replace("advanced to second on an error by 3b", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on an error by ss" in parseText:
            #parseText = parseText.replace("advanced to second on an error by ss", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on an error by lf" in parseText:
            #parseText = parseText.replace("advanced to second on an error by lf", "")
            self.playType = self.playType + "AFE2 "
        elif "advanced to second on an error by rf" in parseText:
            #parseText = parseText.replace("advanced to second on an error by rf", "")
            self.playType = self.playType + "AFE2 "

        elif "advanced to second on the throw" in parseText:
            parseText = parseText.replace("advanced to second on the throw", "")
            self.playType = self.playType + "AT2 "
        elif "advanced to second on a balk" in parseText:
            parseText = parseText.replace("advanced to second on a balk", "")
            self.playType = self.playType + "BLK2 "
        elif "advanced to second on a passed ball" in parseText:
            parseText = parseText.replace("advanced to second on a passed ball", "")
            self.playType = self.playType + "PB2 "
        elif "advanced to second on the error" in parseText:
            parseText = parseText.replace("advanced to second on the error", "")
            self.playType = self.playType + "A2 "
        elif "advanced to second" in parseText:
            parseText = parseText.replace("advanced to second", "")
            self.playType = self.playType + "A2 "

        parseText = parseText.replace("advanced to second", "")


        if "advanced to third on a wild pitch" in parseText:
            parseText = parseText.replace("advanced to third on a wild pitch", "")
            self.playType = self.playType + "WP3 "
        elif "advanced to third on a throwing error by p" in parseText:
            #parseText = parseText.replace("advanced to third on a throwing error by p", "")
            self.playType = self.playType + "ATE3 "
        elif "advanced to third on a throwing error by cf" in parseText:
            #parseText = parseText.replace("advanced to third on a throwing error by cf", "")
            self.playType = self.playType + "ATE3 "
        elif "advanced to third on a throwing error by c" in parseText:
            #parseText = parseText.replace("advanced to third on a throwing error by c", "")
            self.playType = self.playType + "ATE3 "
        elif "advanced to third on a throwing error by 1b" in parseText:
            #parseText = parseText.replace("advanced to third on a throwing error by 1b", "")
            self.playType = self.playType + "ATE3 "
        elif "advanced to third on a throwing error by 2b" in parseText:
            #parseText = parseText.replace("advanced to third on a throwing error by 2b", "")
            self.playType = self.playType + "ATE3 "
        elif "advanced to third on a throwing error by 3b" in parseText:
            #parseText = parseText.replace("advanced to third on a throwing error by 3b", "")
            self.playType = self.playType + "ATE3 "
        elif "advanced to third on a throwing error by ss" in parseText:
            #parseText = parseText.replace("advanced to third on a throwing error by ss", "")
            self.playType = self.playType + "ATE3 "
        elif "advanced to third on a throwing error by lf" in parseText:
            #parseText = parseText.replace("advanced to third on a throwing error by lf", "")
            self.playType = self.playType + "ATE3 "
        elif "advanced to third on a throwing error by rf" in parseText:
            #parseText = parseText.replace("advanced to third on a throwing error by rf", "")
            self.playType = self.playType + "ATE3 "

        elif "advanced to third on a fielding error by p" in parseText:
            #parseText = parseText.replace("advanced to third on a fielding error by p", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a fielding error by cf" in parseText:
            #parseText = parseText.replace("advanced to third on a fielding error by cf", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a fielding error by c" in parseText:
            #parseText = parseText.replace("advanced to third on a fielding error by c", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a fielding error by 1b" in parseText:
            #parseText = parseText.replace("advanced to third on a fielding error by 1b", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a fielding error by 2b" in parseText:
            #parseText = parseText.replace("advanced to third on a fielding error by 2b", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a fielding error by 3b" in parseText:
            #parseText = parseText.replace("advanced to third on a fielding error by 3b", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a fielding error by ss" in parseText:
            #parseText = parseText.replace("advanced to third on a fielding error by ss", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a fielding error by lf" in parseText:
            #parseText = parseText.replace("advanced to third on a fielding error by lf", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a fielding error by rf" in parseText:
            #parseText = parseText.replace("advanced to third on a fielding error by rf", "")
            self.playType = self.playType + "AFE3 "

        elif "advanced to third on a muffed throw by p" in parseText:
            #parseText = parseText.replace("advanced to third on a muffed throw by p", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a muffed throw by cf" in parseText:
            #parseText = parseText.replace("advanced to third on a muffed throw by cf", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a muffed throw by c" in parseText:
            #parseText = parseText.replace("advanced to third on a muffed throw by c", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a muffed throw by 1b" in parseText:
            #parseText = parseText.replace("advanced to third on a muffed throw by 1b", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a muffed throw by 2b" in parseText:
            #parseText = parseText.replace("advanced to third on a muffed throw by 2b", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a muffed throw by 3b" in parseText:
            #parseText = parseText.replace("advanced to third on a muffed throw by 3b", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a muffed throw by ss" in parseText:
            #parseText = parseText.replace("advanced to third on a muffed throw by ss", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a muffed throw by lf" in parseText:
            #parseText = parseText.replace("advanced to third on a muffed throw by lf", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a muffed throw by rf" in parseText:
            #parseText = parseText.replace("advanced to third on a muffed throw by rf", "")
            self.playType = self.playType + "AFE3 "

        elif "advanced to third on an error by p" in parseText:
            #parseText = parseText.replace("advanced to third on an error by p", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on an error by cf" in parseText:
            #parseText = parseText.replace("advanced to third on an error by cf", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on an error by c" in parseText:
            #parseText = parseText.replace("advanced to third on an error by c", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on an error by 1b" in parseText:
            #parseText = parseText.replace("advanced to third on an error by 1b", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on an error by 2b" in parseText:
            #parseText = parseText.replace("advanced to third on an error by 2b", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on an error by 3b" in parseText:
            #parseText = parseText.replace("advanced to third on an error by 3b", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on an error by ss" in parseText:
            #parseText = parseText.replace("advanced to third on an error by ss", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on an error by lf" in parseText:
            #parseText = parseText.replace("advanced to third on an error by lf", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on an error by rf" in parseText:
            #parseText = parseText.replace("advanced to third on an error by rf", "")
            self.playType = self.playType + "AFE3 "
        elif "advanced to third on a passed ball" in parseText:
            parseText = parseText.replace("advanced to third on a passed ball", "")
            self.playType = self.playType + "PB3 "
        elif "advanced to third on the throw" in parseText:
            parseText = parseText.replace("advanced to third on the throw", "")
            self.playType = self.playType + "AT3 "
        elif "advanced to third on a balk" in parseText:
            parseText = parseText.replace("advanced to third on a balk", "")
            self.playType = self.playType + "BLK3 "
        elif "advanced to third on the error" in parseText:
            parseText = parseText.replace("advanced to third on the error", "")
            self.playType = self.playType + "A3 "
        elif "advanced to third" in parseText:
            parseText = parseText.replace("advanced to third", "")
            self.playType = self.playType + "A3 "
        elif "reached first on a passed ball" in parseText:
            parseText = parseText.replace("reached first on a passed ball", "")

        parseText = parseText.replace("advanced to third", "")

        if "scored" in parseText:
            parseText = parseText.replace("scored", "")
            self.playType = self.playType + "RS "
            if ", unearned" in parseText:
                parseText = parseText.replace(", unearned", "")
                self.playType = self.playType + "U "

            if "on a passed ball" in parseText:
                self.playType = self.playType + "PB4 "
                parseText = parseText.replace("on a passed ball", "")

            elif "on the error" in parseText:
                parseText = parseText.replace("on the error", "")

            elif "on a wild pitch" in parseText:
                self.playType = self.playType + "WP4 "
                parseText = parseText.replace("on a wild pitch", "")

            elif "on a balk" in parseText:
                self.playType = self.playType + "BLK4 "
                parseText = parseText.replace("on a balk", "")

            elif "on a throwing error" in parseText:
                self.playType = self.playType + "ATE4 "
                parseText = parseText.replace("on a throwing error", "")


        if "out on the play" in parseText:
            parseText = parseText.replace("out on the play", "")
            self.playType = self.playType + "OOP "

        if "out at first" in parseText:
            parseText = parseText.replace("out at first", "")
            self.playType = self.playType + "TO1 "

        if "out at second" in parseText:
            parseText = parseText.replace("out at second", "")
            self.playType = self.playType + "TO2 "

        if "out at third" in parseText:
            parseText = parseText.replace("out at third", "")
            self.playType = self.playType + "TO3 "

        if "out at home" in parseText:
            parseText = parseText.replace("out at home", "")
            self.playType = self.playType + "TO4 "

        self.playType = self.playType[:-1]
        return parseText

