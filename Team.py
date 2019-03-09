

class Team:

    def __init__(self, team_abbreviation, college, mascot):

        self.teamId = team_abbreviation
        self.college = college
        self.mascot = mascot

        self.listOfPlayers = []
        self.listOfRosters = []

    def _has_roster(self, year):
        for roster_obj in self.listOfRosters:
            if year == roster_obj.year:
                return True
        return False

    def _has_player(self, player_id):
        for player_obj in self.listOfPlayers:
            if player_id == player_obj.playerId:
                return True
        return False

    def add_roster(self, roster_object):
        self.listOfRosters.append(roster_object)

    def add_player(self, player_obj):
        if not self._has_player(player_obj.playerId):
            self.listOfPlayers.append(player_obj)


