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

        #배경 이미지
        self.background = pygame.image.load('images/background.png')

    #실제 게임 구동 함수
    def GameLoop(self):
        pygame.init()
        screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('CatchMind')

        done = False
        clock = pygame.time.Clock()

        #Main Scene은 첫 실행때 무조건 출력
        self.Main.Trigger = True

        while not done:

            clock.tick(30)
            screen.fill((255,255,255))
            screen.blit(self.background, (0,0))

            #Trigger가 True일 때, 해당 Scene이 출력
            if self.Main.Trigger:
                self.Main.startScene(screen)
            if self.ReadyDraw.Trigger:
                self.ReadyDraw.startScene(screen)
            if self.Drawing.Trigger:
                self.Drawing.startScene(screen)
            if self.Guess.Trigger:
                self.Guess.startScene(screen)
            if self.Result.Trigger:
                self.Result.startScene(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.MOUSEBUTTONDOWN:

                    #Main Scene Click Event
                    if self.Main.Trigger:
                        if self.Main.clickCheck() == 'Quit':
                            done = True
                        elif self.Main.clickCheck() == 'Help':
                            pass
                        elif self.Main.clickCheck() == 'Next':
                            self.Main.Trigger = False
                            self.ReadyDraw.Trigger = True
                            screen.blit(self.background, (0,0))

                    #ReadyDraw Scene Click Event
                    if self.ReadyDraw.Trigger:
                        pass

                    # Drawing Scene Click Event
                    if self.Drawing.Trigger:
                        pass

                    # Guess Scene Click Event
                    if self.Guess.Trigger:
                        pass

                    # Result Scene Click Event
                    if self.Result.Trigger:
                        pass

            pygame.display.flip()

    pygame.quit()

start = SceneLoader()
start.GameLoop()

