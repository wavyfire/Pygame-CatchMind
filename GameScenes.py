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

    #다음 씬으로 넘어갈 때 현재 씬의 위젯들을 모두 제거
    @abstractmethod
    def killScene(self):
        pass

class Main(Scenes):

    def __init__(self):
        super().__init__()
        self.QuitButton = Button((1180,0), 'images/QuitButton.png')
        self.HelpButton = Button((0,0), 'images/HelpButton.png')
        self.StartButton = Button((700, 500), 'images/StartButton.png')
        self.Title = Font("Catch-Mind", (0,0,0), 170, (630, 150))

    def startScene(self, screen):

        self.QuitButton.draw(screen)
        self.HelpButton.draw(screen)
        self.StartButton.draw(screen)
        self.Title.draw(screen)

    def killScene(self):
        pass

class ReadyDraw(Scenes):

    def __init__(self):
        super().__init__()
        pass

    def startScene(self, screen ):
        pass

    def killScene(self):
        pass

class Drawing(Scenes):

    def __init__(self):
        super().__init__()
        pass

    def startScene(self,screen):
        pass

    def killScene(self):
        pass

class Guess(Scenes):

    def __init__(self):
        super().__init__()
        pass

    def startScene(self,screen):
        pass

    def killScene(self):
        pass

class Result(Scenes):

    def __init__(self):
        super().__init__()
        pass

    def startScene(self,screen):
        pass

    def killScene(self):
        pass
