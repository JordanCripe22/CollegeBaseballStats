class Player:

    def __init__(self):
        self.positions = []
        self.curPosition = ""

        self.playerId = ""
        self.teamId = ""
        self.lastName = ""
        self.firstName = ""
        self.batHand = ""
        self.throwHand = ""
        self.freshmanYear = ""


    def convertToIntegerPosition(self, strPos):
        strPos = strPos.lower()
        if strPos == 'p':
            return '1'
        elif strPos == 'c':
            return '2'
        elif strPos == '1b':
            return '3'
        elif strPos == '2b':
            return '4'
        elif strPos == '3b':
            return '5'
        elif strPos == 'ss':
            return '6'
        elif strPos == 'lf':
            return '7'
        elif strPos == 'cf':
            return '8'
        elif strPos == 'rf':
            return '9'
        elif strPos == 'dh':
            return '10'
        elif strPos == 'ph':
            return 'PH'
        elif strPos == 'pr':
            return 'PR'
        else:
            raise ValueError('PLAYER Missing Positon ' + strPos)

    def show(self):
        print(self.playerId, end=' ')
        print(self.teamId, end=' ')
        print(self.firstName, end=' ')
        print(self.lastName)
        