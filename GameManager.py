import pygame
import GameScenes

class SceneLoader:

    def __init__(self):

        # Scene Load
        self.Main = GameScenes.Main()
        self.Help = GameScenes.Help()
        self.ReadyDraw = GameScenes.ReadyDraw()
        self.Drawing = GameScenes.Drawing()
        self.Guess = GameScenes.Guess()
        self.Result = GameScenes.Result()

        # 배경 이미지
        self.background = pygame.image.load('images/background.png')

    #실제 게임 구동 함수
    def GameLoop(self):
        pygame.init()
        screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('CatchMind')

        done = False

        ## 따로 DrawDB를 만들어서 빼도 되는데, 일단은 없어서 분류하기가 애매해서, GameManager로 분류했습니다.
        mouseflag = False # Drawing을 위한 변수
        size = 1 # Drawing을 위한 변수....
        color = (0,0,0) # Drawing을 위한 변수...
        clock = pygame.time.Clock()

        # Main Scene은 첫 실행때 무조건 출력
        self.Main.Trigger = True

        screen.fill((255, 255, 255))
        screen.blit(self.background, (0, 0))

        while not done:
            mouseX, mouseY = pygame.mouse.get_pos()

            clock.tick(60)

            # Trigger가 True일 때, 해당 Scene이 출력
            if self.Main.Trigger:
                self.Main.startScene(screen)
                self.Main.addScene(screen, GameScenes.ScoreHandler.PlayerNumbers) # addScene은 체크표시 같은 추가 화면을 표현해줍니다.
                # Player 수가 선택되지 않고 스타트를 눌렀을 때의 경고메시지
                if self.Main.Trigger_Message:
                    self.Main.printMessage(screen)

            if self.Help.Trigger:
                self.Help.startScene(screen)

            if self.ReadyDraw.Trigger:
                self.ReadyDraw.startScene(screen)
                # 랜덤 단어를 창에 표시
                if self.ReadyDraw.Trigger_Message:
                    self.ReadyDraw.printMessage(screen)

            if self.Drawing.Trigger:
                self.Drawing.addScene(screen, color, size) # 마찬가지의 AddScene. 순서가 바뀌면 그려지는 순서가 달라져서 버그발생.
                self.Drawing.startScene(screen)
                if 150 <= mouseX and mouseX <= 1140 and 0 <= mouseY and mouseY <= 600 and mouseflag == True:
                    self.Drawing.Sketch(screen, color, size, mouseX, mouseY) # Mouseflag는 아래 Event에서 전환됩니다.

            if self.Guess.Trigger:
                self.Guess.startScene(screen)

            if self.Result.Trigger:
                self.Result.startScene(screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONUP:
                    mouseflag = False # 그림판 기능 때문에 추가된 줄.

                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouseflag = True # 그림판 기능 때문에 추가된 줄.

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

                    # ReadyDraw Scene Click Event
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
                        if self.Drawing.clickCheck() == 'PickRed':
                            color = (255, 0 ,0)
                        if self.Drawing.clickCheck() == 'PickBlue':
                            color = (61, 183, 204)
                        if self.Drawing.clickCheck() == 'PickBlack':
                            color = (0, 0 ,0)
                        if self.Drawing.clickCheck() == 'DotSize1':
                            size = 1
                        if self.Drawing.clickCheck() == 'DotSize2':
                            size = 2
                        if self.Drawing.clickCheck() == 'DotSize3':
                            size = 3
                        if self.Drawing.clickCheck() == 'Eraser':
                            screen.blit(self.background, (0, 0)) # 화면 저장 기능이 없어서 덮어버려야합니다.
                        if self.Drawing.clickCheck() == 'Quit':
                            done = True
                        if self.Drawing.clickCheck() == 'Done':
                            self.Drawing.Off()
                            self.Guess.On()

                    # Guess Scene Click Event
                    if self.Guess.Trigger:
                        if self.Guess.clickCheck() == 'BackToDraw':
                            self.Guess.Off()
                            self.Drawing.On()

                    # Result Scene Click Event
                    if self.Result.Trigger:
                        pass

            pygame.display.flip()



    pygame.quit()

start = SceneLoader()
start.GameLoop()

