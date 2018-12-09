import pygame
import GameScenes

class SceneLoader:

    def __init__(self):

        #Scene Load
        self.Main = GameScenes.Main()
        self.Help = GameScenes.Help()
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
                #Player 수가 선택되지 않고 스타트를 눌렀을 때의 경고메시지
                if self.Main.Trigger_Message:
                    self.Main.printMessage(screen)

            if self.Help.Trigger:
                self.Help.startScene(screen)

            if self.ReadyDraw.Trigger:
                self.ReadyDraw.startScene(screen)
                #랜덤 단어를 창에 표시
                if self.ReadyDraw.Trigger_Message:
                    self.ReadyDraw.printMessage(screen)

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
                            self.Main.Off()
                            self.Help.On()
                            screen.blit(self.background, (0,0))

                        elif self.Main.clickCheck() == 'Next':
                            if self.Main.checkPlayers():
                                self.Main.Off()
                                self.ReadyDraw.Trigger = True
                                screen.blit(self.background, (0,0))
                            else:
                                self.Main.Trigger_Message = True

                        elif self.Main.clickCheck() == '2 Players':
                            self.Main.setPlayers(2)

                        elif self.Main.clickCheck() == '3 Players':
                            self.Main.setPlayers(3)

                        elif self.Main.clickCheck() == '4 Players':
                            self.Main.setPlayers(4)

                    if self.Help.Trigger:
                        if self.Help.clickCheck() == 'Quit':
                            done = True

                        elif self.Help.clickCheck() == 'Back':
                            self.Main.On()
                            self.Help.Off()
                            screen.blit(self.background, (0,0))

                    #ReadyDraw Scene Click Event
                    if self.ReadyDraw.Trigger:

                        if self.ReadyDraw.clickCheck() == 'Quit':
                            done = True
                        elif self.ReadyDraw.clickCheck() == 'GetWord':
                            self.ReadyDraw.getWord()
                            self.ReadyDraw.setWordText()
                            self.ReadyDraw.Trigger_Message = True
                        elif self.ReadyDraw.clickCheck() == 'Next':
                            self.ReadyDraw.Off()
                            self.Drawing.On()
                            screen.blit(self.background, (0, 0))

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

