
class ScoreHandler:

    def __init__(self):

        self.PlayerNumbers = 0
        self.ScoreRecord = []

    #Player 수를 결정
    def setPlayers(self, playernumbers):

        self.PlayerNumbers = int(playernumbers)
        for i in range(1, self.PlayerNumbers+1):
            dict = {}
            dict['player' + str(i)] = 0
            self.ScoreRecord.append(dict)

    #해당 Player에게 점수
    def raiseScore(self, playernumber, score):

        player = self.ScoreRecord[playernumber]
        player['player'] += score

    #player 수가 결정되었는지를 검사
    def playerCheck(self):

        if self.PlayerNumbers == 0:
            return False
        else:
            return True

    #ScoreBoard에 표시하기 위해 문자열 형태로 정리해서 반환
    def getScore(self):

        text = ''
        for player in self.ScoreRecord:
            for key, value in player.items():
                text += key + ' : '+ str(value) +'\n'
        return text





