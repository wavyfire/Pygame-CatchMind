
class ScoreHandler:

    def __init__(self):

        self.PlayerNumbers = 0
        self.NowPlaying = 0
        self.ScoreRecord = []
        self.Limit = 0
        self.NowQuizNumber = 0

    #Player 수를 결정
    def setPlayers(self, playernumbers):

        self.PlayerNumbers = int(playernumbers)
        for i in range(1, self.PlayerNumbers+1):
            dict = {}
            dict['player' + str(i)] = 0
            self.ScoreRecord.append(dict)

    def getPlayers(self):
        return self.PlayerNumbers

    # 처음 턴 세팅
    def setTurn(self):

        self.NowPlaying = 1

    def getTurn(self):

        return self.NowPlaying

    # 턴을 넘길 때 사용
    def changeTurn(self):
        try:
            if self.NowPlaying < self.PlayerNumbers:
                self.NowPlaying += 1
            else:
                self.NowPlaying = 1

        except:
            print("Set PlayerNumbers First!")
            # 해당 Player에게 점수

    def raiseScore(self, scoredplayer, score):
        for player in self.ScoreRecord:
            print(player)
            for key, value in player.items():
                if key == scoredplayer:
                    person = key
                    player[person] += score

        self.NowQuizNumber += 1
        print(self.ScoreRecord)  # Debug

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
                text += key + ' : '+ str(value) +'.'
        return text

    def makeLimit(self):
        if self.PlayerNumbers == 2:
            self.Limit = 4  # 0부터라 실상은 홀수.
        if self.PlayerNumbers == 3:
            self.Limit = 6
        if self.PlayerNumbers == 4:
            self.Limit = 8

    def NowQuizNum(self):
        return self.NowQuizNumber

    def QuizLimit(self):
        return self.Limit

    def Winner(self):
        othervalue = 0
        otherplayer = ""
        for player in self.ScoreRecord:
            for key, value in player.items():
                if value > othervalue:
                    othervalue = value
                    otherplayer = key
        return otherplayer








