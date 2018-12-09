from GameWidgets import Button, Font
import WordDB
import ScoreDB
from abc import *

ScoreHandler = ScoreDB.ScoreHandler()

class Scenes(metaclass=ABCMeta):

    #생성시 해당 씬에서 사용되는 모든 위젯의 객체를 생성
    @abstractmethod
    def __init__(self):
        pass

    #GameManager에서 해당 씬의 차례일때, 모든 생성자에서 만든 위젯을 게임판에 표시
    @abstractmethod
    def startScene(self, screen):
        pass

    #어떤 버튼이 클릭되었는지 확인
    @abstractmethod
    def clickCheck(self):
        pass

    def On(self):
        pass

    def Off(self):
        pass

class Main(Scenes):

    def __init__(self):
        super().__init__()
        self.QuitButton = Button((1180,0), 'images/QuitButton.png')
        self.HelpButton = Button((0,0), 'images/HelpButton.png')
        self.StartButton = Button((730, 300), 'images/StartButton.png')
        self.Title = Font("Catch-Mind", (0,0,0), 170, (630, 150))
        self.GameDiscription = Font("Numbers of players : 2 ~ 4", (0,0,0), 50, (620, 500))
        self.PlayerNumbers2 = Button((400,300), 'images/2.png')
        self.PlayerNumbers3 = Button((510,300), 'images/3.png')
        self.PlayerNumbers4 = Button((620,300), 'images/4.png')
        self.Alarm = Font("Choose Player Number", (255,0,0), 50, (620, 430))

        self.Trigger_Message = False

        self.Trigger = False

    def startScene(self, screen):

        self.QuitButton.draw(screen)
        self.HelpButton.draw(screen)
        self.StartButton.draw(screen)
        self.Title.draw(screen)
        self.GameDiscription.draw(screen)
        self.PlayerNumbers2.draw(screen)
        self.PlayerNumbers3.draw(screen)
        self.PlayerNumbers4.draw(screen)

    def printMessage(self, screen):

        self.Alarm.draw(screen)

    def checkPlayers(self):
        if ScoreHandler.playerCheck():
            return True
        else:
            return False

    def setPlayers(self, players):
        ScoreHandler.setPlayers(players)

    def clickCheck(self):

        if self.QuitButton.clickChecker():
            return 'Quit'
        if self.HelpButton.clickChecker():
            return 'Help'
        if self.StartButton.clickChecker():
            return 'Next'
        if self.PlayerNumbers2.clickChecker():
            return '2 Players'
        if self.PlayerNumbers3.clickChecker():
            return '3 Players'
        if self.PlayerNumbers4.clickChecker():
            return '4 Players'

    def On(self):
        self.Trigger = True

    def Off(self):
        self.Trigger = False

class Help(Scenes):

    def __init__(self):
        super().__init__()
        self.QuitButton = Button((1180, 0), 'images/QuitButton.png')
        self.BackButton = Button((0,0), 'images/BackSpace.png')
        self.Title = Font("Need Help?", (0, 0, 0), 170, (630, 150))
        self.Help = Font("Catch-Mind is ~ ", (0, 0, 0), 50, (200, 300))

        self.Trigger = False

    def startScene(self, screen):

        self.QuitButton.draw(screen)
        self.BackButton.draw(screen)
        self.Title.draw(screen)
        self.Help.draw(screen)

    def clickCheck(self):

        if self.QuitButton.clickChecker():
            return 'Quit'
        if self.BackButton.clickChecker():
            return 'Back'

    def On(self):
        self.Trigger = True

    def Off(self):
        self.Trigger = False

class ReadyDraw(Scenes):

    def __init__(self):
        super().__init__()
        self.QuitButton = Button((1180,0), 'images/QuitButton.png')
        self.GetWordButton = Button((420, 70), 'images/GetWord.png')
        self.ReadyButton = Button((510,500), 'images/ReadyButton.png')
        self.RegetWordButton = Button((0,0), 'images/RegetWord.png')
        self.ScoreBoard = Button((0,100), 'images/ScoreBoard.png')
        self.ScoreBoardText = Font(ScoreHandler.getScore(), (0,0,0), 50, (20, 100))

        self.WordText = None

        self.Trigger = False
        self.Trigger_Message = False

        self.WordHandler = WordDB.FileHandler()

    def startScene(self, screen):
        self.QuitButton.draw(screen)
        self.GetWordButton.draw(screen)
        self.ReadyButton.draw(screen)
        self.RegetWordButton.draw(screen)
        self.ScoreBoard.draw(screen)
        self.ScoreBoardText.draw(screen)

    def printMessage(self, screen):
        self.WordText.draw(screen)

    def getWord(self):
        self.WordHandler.randFromDB()

    def setWordText(self):
        word = '\"' + self.WordHandler.answer + '\"'
        self.WordText = Font(word, (0, 0, 0), 70, (640, 170))

    def clickCheck(self):
        if self.QuitButton.clickChecker():
            return 'Quit'
        if self.GetWordButton.clickChecker():
            return 'GetWord'
        if self.ReadyButton.clickChecker():
            return 'Next'

    def On(self):
        self.Trigger = True

    def Off(self):
        self.Trigger = False


class Drawing(Scenes):

    def __init__(self):
        super().__init__()
        self.Trigger = 0
        pass

    def startScene(self,screen):
        pass

    def clickCheck(self):
        pass

    def On(self):
        self.Trigger = True

    def Off(self):
        self.Trigger = False


class Guess(Scenes):

    def __init__(self):
        super().__init__()
        self.Trigger = 0
        pass

    def startScene(self,screen):
        pass

    def clickCheck(self):
        pass

    def On(self):
        self.Trigger = True

    def Off(self):
        self.Trigger = False


class Result(Scenes):

    def __init__(self):
        super().__init__()
        self.Trigger = 0
        pass

    def startScene(self,screen):
        pass

    def clickCheck(self):
        pass

    def On(self):
        self.Trigger = True

    def Off(self):
        self.Trigger = False

