import pygame
import GameScenes
import ScoreDB
import WordDB

class SceneLoader:

    #생성될 때 모든 씬을 로드
    def __init__(self):
        self.Main = GameScenes.Main()
        self.ReadyDraw = GameScenes.ReadyDraw()
        self.Drawing = GameScenes.Drawing()
        self.Guess = GameScenes.Guess()
        self.Result = GameScenes.Result()

    #실제 게임 구동 함수
    def GameLoop(self):
        pygame.init()
        screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('CatchMind')

        done = False
        clock = pygame.time.Clock()

        while not done:

            clock.tick(30)
            screen.fill((255,255,255))
            self.Main.startScene(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            pygame.display.flip()

    pygame.quit()

start = SceneLoader()
start.GameLoop()

