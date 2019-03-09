
class Fielding:

    def __init__(self):
        self.position = ""
        self.playType = ""

    def show(self):
        print(self.position, end=" ")
        print(self.playType)

    def cleanString(self, text):
        return text.replace(" ", "").replace(".", "").replace(",", "")

    def parseFielding(self, text):

        parseText = text
        if "on a throwing error" in text or "on a fielding error" in text or "on a muffed throw" in text or "on an error" in text or "dropped foul ball" in text:
            if "on a throwing error" in text:
                parseText = parseText.replace("on a throwing error", "")
                self.playType = "TE"
            elif "reached on an error" in text:
                parseText = parseText.replace("reached on an error", "")
                self.playType = "FE"
            elif "on a fielding error" in text:
                parseText = parseText.replace("on a fielding error", "")
                self.playType = "FE"
            elif "on a muffed throw" in text:
                parseText = parseText.replace("on a muffed throw", "")
                self.playType = "FE"
            elif "on an error" in text:
                parseText = parseText.replace("on an error", "")
                self.playType = "FE"
            elif "dropped foul ball" in text:
                parseText = parseText.replace("dropped foul ball", "")
                parseText = self.cleanString(parseText)
                self.playType = parseText.upper()
                parseText = ""

            if "by pitcher" in parseText or "by p" in parseText:
                parseText = parseText.replace("by pitcher", "").replace("by p", "")
                self.position = self.position + "1"

            elif "by first base" in parseText or "by 1b" in parseText:
                parseText = parseText.replace("by first base", "").replace("by 1b", "")
                self.position = self.position + "3"
            elif "by second base" in parseText or "by 2b" in parseText:
                parseText = parseText.replace("by second base", "").replace("by 2b", "")
                self.position = self.position + "4"
            elif "by third base" in parseText or "by 3b" in parseText:
                parseText = parseText.replace("by third base", "").replace("by 3b", "")
                self.position = self.position + "5"
            elif "by shortstop" in parseText or "by ss" in parseText:
                parseText = parseText.replace("by shortstop", "").replace("by ss", "")
                self.position = self.position + "6"
            elif "by left field" in parseText or "by lf" in parseText:
                parseText = parseText.replace("by left field", "").replace("by lf", "")
                self.position = self.position + "7"
            elif "by center field" in parseText or "by cf" in parseText:
                parseText = parseText.replace("by center field", "").replace("by cf", "")
                self.position = self.position + "8"
            elif "by right field" in parseText or "by rf" in parseText:
                parseText = parseText.replace("by right field", "").replace("by rf", "")
                self.position = self.position + "9"
            elif "by catcher" in parseText or "by c" in parseText:
                parseText = parseText.replace("by catcher", "").replace("by c", "")
                self.position = self.position + "2"
            elif parseText == "":
                pass
            else:
                raise ValueError("Error parseFielding Missing: error by" + parseText)

        else:
            parseText = parseText.replace("unassisted", "")
            parseText = parseText.replace("interference", "")
            parseText = parseText.replace("on a fielder's choice", "")
            parseText = parseText.replace("no advance", "")

            if "assist by p" in parseText:
                parseText = parseText.replace("assist by p", "")
                self.playType = self.playType + "A-1"
            elif "assist by cf" in parseText:
                parseText = parseText.replace("assist by cf", "")
                self.playType = self.playType + "A-8"
            elif "assist by c" in parseText:
                parseText = parseText.replace("assist by c", "")
                self.playType = self.playType + "A-2"
            elif "assist by 1b" in parseText:
                parseText = parseText.replace("assist by 1b", "")
                self.playType = self.playType + "A-3"
            elif "assist by 2b" in parseText:
                parseText = parseText.replace("assist by 2b", "")
                self.playType = self.playType + "A-4"
            elif "assist by 3b" in parseText:
                parseText = parseText.replace("assist by 3b", "")
                self.playType = self.playType + "A-5"
            elif "assist by ss" in parseText:
                parseText = parseText.replace("assist by ss", "")
                self.playType = self.playType + "A-6"
            elif "assist by lf" in parseText:
                parseText = parseText.replace("assist by lf", "")
                self.playType = self.playType + "A-7"
            elif "assist by rf" in parseText:
                parseText = parseText.replace("assist by rf", "")
                self.playType = self.playType + "A-9"

            parseText = self.cleanString(parseText)
            parseText = parseText.replace("shortstop", "ss")
            positions = parseText.split("to")
            parseText = parseText.replace("to", "")
            for pos in positions:
                if pos == "":
                    pass
                elif pos == "p" or pos == "pitcher":
                    self.position = self.position + "1-"
                    parseText = parseText.replace("pitcher", "").replace("p", "")
                elif pos == "1b" or pos == "firstbase":
                    self.position = self.position + "3-"
                    parseText = parseText.replace("firstbase", "").replace("1b", "")
                elif pos == "2b" or pos == "secondbase":
                    self.position = self.position + "4-"
                    parseText = parseText.replace("secondbase", "").replace("2b", "")
                elif pos == "3b" or pos == "thirdbase":
                    self.position = self.position + "5-"
                    parseText = parseText.replace("thirdbase", "").replace("3b", "")
                elif pos == "ss" or pos == "shortstop":
                    self.position = self.position + "6-"
                    parseText = parseText.replace("shortstop", "").replace("ss", "")
                elif pos == "lf" or pos == "leftfield":
                    self.position = self.position + "7-"
                    parseText = parseText.replace("leftfield", "").replace("lf", "")
                elif pos == "cf" or pos == "centerfield":
                    self.position = self.position + "8-"
                    parseText = parseText.replace("centerfield", "").replace("cf", "")
                elif pos == "c" or pos == "catcher":
                    self.position = self.position + "2-"
                    parseText = parseText.replace("catcher", "").replace("c", "")
                elif pos == "rf" or pos == "rightfield":
                    self.position = self.position + "9-"
                    parseText = parseText.replace("rightfield", "").replace("rf", "")
                else:
                    self.position = self.position + " "

            self.position = self.position[:-1]
        return parseText