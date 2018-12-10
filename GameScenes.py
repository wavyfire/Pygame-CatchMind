from GameWidgets import Button, Font
import WordDB
import ScoreDB
import pygame
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
        self.StartButton = Button((800, 300), 'images/StartButton.png')
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

    def addScene(self, screen, playerNum):
        if playerNum == 2:
            self.SelectPlayerPanel = Button((400, 300), 'images/Check.png')
            self.SelectPlayerPanel.draw(screen)
        if playerNum == 3:
            self.SelectPlayerPanel = Button((510, 300), 'images/Check.png')
            self.SelectPlayerPanel.draw(screen)
        if playerNum == 4:
            self.SelectPlayerPanel = Button((620, 300), 'images/Check.png')
            self.SelectPlayerPanel.draw(screen)

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

        self.WordText = None

        self.Trigger = False
        self.Trigger_ScoreBoard = False
        self.Trigger_Message = False

        self.WordHandler = WordDB.FileHandler()

        #시작 시 첫번째 턴으로 설정
        ScoreHandler.setTurn()

    def startScene(self, screen):
        self.QuitButton.draw(screen)
        self.GetWordButton.draw(screen)
        self.ReadyButton.draw(screen)
        self.RegetWordButton.draw(screen)
        self.ScoreBoard.draw(screen)

    def setScoreBoard(self):
        self.ScoreTextList = []
        text = ScoreHandler.getScore().split('.')

        y = 150
        for scoretext in text:
            self.ScoreTextList.append(Font((scoretext), (0,0,0), 30, (120, y)))
            y += 50

    def printScoreBoard(self, screen):
        for text in self.ScoreTextList:
            text.draw(screen)

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
        self.DrawBackGround = pygame.image.load('images/DrawBackGround.png')
        self.SketchBook = Button((150, 0), 'images/SketchBook.png')
        self.PickRed = Button((10, 680), 'images/PickRed.png')
        self.PickBlue = Button((50, 680), 'images/PickBlue.png')
        self.PickBlack = Button((90, 680), 'images/PickBlack.png')
        self.DotSize1 = Button((1100, 680), 'images/DotSize1.png')
        self.DotSize2 = Button((1140, 680), 'images/DotSize2.png')
        self.DotSize3 = Button((1180, 680), 'images/DotSize3.png')
        self.Eraser = Button((1138, 640), 'images/Eraser.png')
        self.DoneButton = Button((0, 0), 'images/Done.png')
        self.QuitButton = Button((1180, 0), 'images/QuitButton.png')



        self.Trigger = 0

    def startScene(self,screen):
        screen.blit(self.DrawBackGround, (0, 0))
        self.SketchBook.draw(screen)
        self.PickRed.draw(screen)
        self.PickBlue.draw(screen)
        self.PickBlack.draw(screen)
        self.DotSize1.draw(screen)
        self.DotSize2.draw(screen)
        self.DotSize3.draw(screen)
        self.Eraser.draw(screen)
        self.DoneButton.draw(screen)
        self.QuitButton.draw(screen)
        self.DisplayTurn()
        self.NowDrawing.draw(screen)

    def clickCheck(self):
        if self.SketchBook.clickChecker():
            return 'SketchBook'
        if self.PickRed.clickChecker():
            return 'PickRed'
        if self.PickBlue.clickChecker():
            return 'PickBlue'
        if self.PickBlack.clickChecker():
            return 'PickBlack'
        if self.DotSize1.clickChecker():
            return 'DotSize1'
        if self.DotSize2.clickChecker():
            return 'DotSize2'
        if self.DotSize3.clickChecker():
            return 'DotSize3'
        if self.Eraser.clickChecker():
            return 'Eraser'
        if self.DoneButton.clickChecker():
            return 'Done'
        if self.QuitButton.clickChecker():
            return 'Quit'

    def Sketch(self, screen, color, size, mouseX, mouseY):
            for i in range(0, size*2):
                for j in range(0, size*2):
                    pixelArray = pygame.PixelArray(screen)
                    pixelArray[mouseX + i][mouseY + j] = color
                    del pixelArray  # 화면이 Lock 되는것을 막기 위함

    def addScene(self, screen, color, dotsize):
        if dotsize == 1:
            self.DotCheck = Button((1100, 680), 'images/DotCheck.png')
            self.CheckRemover = Button((1100,680), 'images/CheckRemover.png')
            self.CheckRemover.draw(screen)
            self.DotCheck.draw(screen)

        if dotsize == 2:
            self.DotCheck = Button((1140, 680), 'images/DotCheck.png')
            self.CheckRemover = Button((1100, 680), 'images/CheckRemover.png')
            self.CheckRemover.draw(screen)
            self.DotCheck.draw(screen)

        if dotsize == 3:
            self.DotCheck = Button((1180, 680), 'images/DotCheck.png')
            self.CheckRemover = Button((1100, 680), 'images/CheckRemover.png')
            self.CheckRemover.draw(screen)
            self.DotCheck.draw(screen)

    def DisplayTurn(self):
        # 누가 그림을 그리고 있는지 알려주는 메시지
        self.NowDrawing = Font('Player ' + str(ScoreHandler.getTurn()) + ' \'s Drawing!', (0, 0, 0), 50, (630, 50))

    def On(self):
        self.Trigger = True

    def Off(self):
        self.Trigger = False


class Guess(Scenes):

    def __init__(self):
        super().__init__()
        self.BackToDraw = Button((10, 70), 'images/BackToDraw.png')
        self.DrawBackGround = pygame.image.load('images/GuessBackGround.png')
        self.QuitButton = Button((1180, 0), 'images/QuitButton.png')
        self.InputAnswer = Button((140, 630), 'images/InputAnswer.png')
        self.AnswerRemover = Button((140, 630), 'images/AnswerRemover.png')
        self.WrongCheck = Button((420, 640), 'images/WrongMark.png')
        self.CorrectMark = Button((420,640), 'images/CorrectMark.png')

        # PlayerButton 자체는 startScene() 에서 생성 : 플레이어 수가 정해지고 나서 버튼 수가 결정되기 때문
        self.PlayerButtonList = []

        self.Trigger_PlayerCheck = 0

        self.Trigger = 0

    def startScene(self,screen):
        screen.blit(self.DrawBackGround, (0, 0))
        self.BackToDraw.draw(screen)
        self.QuitButton.draw(screen)
        self.InputAnswer.draw(screen)

        # Player수, Turn에 따른 버튼 출력과 check 표시를 용이하게 하기 위해 튜플로 번호 및 좌표 관리
        # Player수에 맞춰서 버튼 생성
        y_plus = 100
        y = 200
        for playernumber in range(1, ScoreHandler.getPlayers() + 1):
            playername = 'Player ' + str(playernumber)
            path = 'images/Player' + str(playernumber) + 'Button.png'
            self.PlayerButtonList.append(( Button((10, y + y_plus), path), playernumber , (10, y + y_plus), playername))
            y = y + y_plus

        # 그림을 그리고 있는 player는 버튼 출력이 되지 않음
        for playerbutton in self.PlayerButtonList:
            if playerbutton[1] <= ScoreHandler.getPlayers():
                if playerbutton[1] == ScoreHandler.getTurn():
                    continue
                playerbutton[0].draw(screen)

    # plyaer 가 check 되었을 때 체크 표시
    def addScene(self, screen, playernumber):
        for playerbutton in self.PlayerButtonList:
            if playerbutton[1] == playernumber:
                playercheckpannel = Button(playerbutton[2], 'images/PlayerCheck.png')
                playercheckpannel.draw(screen)

    def clickCheck(self):
        if self.BackToDraw.clickChecker():
            return 'BackToDraw'
        if self.QuitButton.clickChecker():
            return 'Quit'
        for playerbutton in self.PlayerButtonList:
            if playerbutton[0].clickChecker():
                return playerbutton[3]
        if self.InputAnswer.clickChecker():
            return 'InputAnswer'

    def Input(self, name):
        text = Font.guessInput(self, name)
        return text

    def DrawInput(self, input, screen):
        txt = Font(input, (0, 0, 0), 50, (420, 660))
        self.AnswerRemover.draw(screen)
        txt.draw(screen)

    def DicCheck(self, name):
        Dic = WordDB.FileHandler.CorrectInput(self)
        if name in Dic:
            return True

    def Wrong(self, screen):
        self.WrongCheck.draw(screen)

    def Correct(self, screen):
        self.CorrectMark.draw(screen)

    def NextTrun(self):
        ScoreHandler.changeTurn()

    def AddScore(self, player):
        ScoreHandler.raiseScore(player, 1)

    def LimitCheck(self):
        ScoreHandler.makeLimit()

    def NowQuizNum(self):
        return ScoreHandler.NowQuizNum()

    def NowQuizLimit(self):
        return ScoreHandler.QuizLimit()

    def NowPlaying(self):
        return ScoreHandler.NowPlaying

    def On(self):
        self.Trigger = True

    def Off(self):
        self.Trigger = False


class Result(Scenes):

    def __init__(self):
        super().__init__()
        self.QuitButton = Button((1180, 0), 'images/QuitButton.png')

        self.Trigger_ScoreBoard = 0
        self.Trigger = 0

    def startScene(self, screen):
        self.QuitButton.draw(screen)

    def setScoreBoard(self):
        self.ScoreTextList = []
        text = ScoreHandler.getScore().split('.')

        y = 300
        for scoretext in text:
            self.ScoreTextList.append(Font((scoretext), (0,0,0), 30, (600, y)))
            y += 50

    def printScoreBoard(self, screen):
        for text in self.ScoreTextList:
            text.draw(screen)


    def clickCheck(self):
        if self.QuitButton.clickChecker():
            return "Quit"

    def WinnerCheck(self,screen):
        winner = ScoreHandler.Winner()
        text = winner + " Is WIN!"
        self.Title = Font(winner + " Is WIN!", (255, 0, 0), 170, (630, 150))
        self.Title.draw(screen)

    def On(self):
        self.Trigger = True

    def Off(self):
        self.Trigger = False

