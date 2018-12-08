import pygame
from GameWidgets import Button, Font
from abc import *

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

class Main(Scenes):

    def __init__(self):
        super().__init__()
        self.QuitButton = Button((1180,0), 'images/QuitButton.png')
        self.HelpButton = Button((0,0), 'images/HelpButton.png')
        self.StartButton = Button((700, 300), 'images/StartButton.png')
        self.Title = Font("Catch-Mind", (0,0,0), 170, (630, 150))
        self.GameDiscription = Font("Numbers of players : 2 ~ 4", (0,0,0), 50, (650, 500))
        self.Trigger = False

    def startScene(self, screen):

        self.QuitButton.draw(screen)
        self.HelpButton.draw(screen)
        self.StartButton.draw(screen)
        self.Title.draw(screen)
        self.GameDiscription.draw(screen)

    def clickCheck(self):

        if self.QuitButton.clickChecker():
            return 'Quit'
        if self.HelpButton.clickChecker():
            return 'Help'
        if self.StartButton.clickChecker():
            return 'Next'

class ReadyDraw(Scenes):

    def __init__(self):
        super().__init__()
        self.QuitButton = Button((1180,0), 'images/QuitButton.png')
        self.Trigger = False

    def startScene(self, screen):
        self.QuitButton.draw(screen)

    def clickCheck(self):
        pass

class Drawing(Scenes):

    def __init__(self):
        super().__init__()
        self.Trigger = 0
        pass

    def startScene(self,screen):
        pass

    def clickCheck(self):
        pass

class Guess(Scenes):

    def __init__(self):
        super().__init__()
        self.Trigger = 0
        pass

    def startScene(self,screen):
        pass

    def clickCheck(self):
        pass

class Result(Scenes):

    def __init__(self):
        super().__init__()
        self.Trigger = 0
        pass

    def startScene(self,screen):
        pass

    def clickCheck(self):
        pass
