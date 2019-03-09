from DataPoint import DataPoint
from Player import Player

from bs4 import BeautifulSoup
from Utils import Utils


class GameInfo:

    def __init__(self):

        self.awayTeamId = ""
        self.homeTeamId = ""
        self.gameMonth = 0
        self.gameDay = 0
        self.gameYear = 0
        self.gameHour = 0
        self.start = ""
        self.innings = 0

        self.dataPointList = []

        self.awayPlayerList = []
        self.homePlayerList = []

        self.eventList = []



    def setBasicInfo(self, info):
        self.awayTeamId = info[0]
        self.homeTeamId = info[1]
        self.gameMonth = info[2]
        self.gameDay = info[3]
        self.gameYear = info[4][2:4]
        self.gameHour = info[5][:-5]

    def scrapeBoxScore(self, file_path):

        # initialize beautiful soup variable
        html_doc = open(file_path, "r")
        soup = BeautifulSoup(html_doc, 'html.parser')

        # load basic info
        split_path = file_path.split("/")[-1].split("_")
        self.setBasicInfo(split_path)

        table_arr = soup.find_all('table')
        inning_scores = []

        table_no = 0
        for table in table_arr:

            for child1 in table.contents:

                if child1.name == "tbody":
                    for child2 in child1:

                        if child2.name == "tr":
                            for child3 in child2:
                                if child3.name == "th":
                                    # create DataPoint object
                                    temp_data_point = DataPoint(table_no, child3.text)
                                    self.dataPointList.append(temp_data_point)
                                elif child3.name == "td":
                                    if table_no == 0:
                                        inning_scores.append(child3.text)
                                    pass
                                elif child3.name:
                                    raise ValueError(child3.name)
                        elif child2.name:
                            pass

                elif child1.name == "caption":

                    if child1.text == "Team Score By Innings":
                        pass
                    elif child1.text == "Scoring Summary":
                        pass
                    elif "Top" in child1.text:
                        pass
                    elif "Bottom" in child1.text:
                        pass
                    elif "Composite Stats" in child1.text:
                        pass
                    elif "Pitching Stats" in child1.text:
                        pass
                    else:
                        pass

                elif child1.name == "thead":
                    pass
                elif child1.name == "tfoot":
                    pass
                elif child1.name:
                    raise ValueError("Missing", child1.name)

            table_no += 1

        self.innings = int(len(inning_scores) / 2 - 3)
        return self


    def parsePlayer(self, info_str):

        player = Player()

        # 4 spaces (Indent) represents this player came in as a substitute
        if info_str[0:4] == "    ":
            player.positions.append('be')
            info_str = info_str[4:]

        info_arr = info_str.split(' ')
        player_position_list = info_arr[0].split('/')

        for pos in player_position_list:
            int_pos = player.convertToIntegerPosition(pos.lower())
            player.positions.append(int_pos)

        player.curPosition = player.positions.pop(0)

        name_str = ""
        for word in info_arr[1:]:
            name_str = name_str + word + " "

        name_str = name_str[:-1]
        name_arr = Utils.parse_name_from_str(name_str)

        player.firstName = name_arr[0]
        player.lastName = name_arr[1]

        return player

    def arrayToString(self, arr):
        str_ans = ""
        for word in arr:
            if word != "":
                str_ans = str_ans + word + " "
        return str_ans[:-1]