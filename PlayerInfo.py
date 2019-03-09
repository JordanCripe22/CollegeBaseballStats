class PlayerInfo:

    def __init__(self, player_id, team_id, last_name, first_name, bats, throws):

        self.playerId = player_id
        self.teamId = team_id
        self.lastName = last_name
        self.firstName = first_name
        self.bats = bats
        self.throws = throws
        self.freshmanYear = ""

    def show(self):
        print(self.playerId, end=' ')
        print(self.teamId, end=' ')
        print(self.firstName, end=' ')
        print(self.lastName)





