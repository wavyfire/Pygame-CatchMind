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

        keyInput = False  # Key가 여러개 입력되는 것을 방지하기 위한 Bool
        guessword = ""  # text가 입력되면서 저장될 값

        reDraw = False # Guess -> ReadyDraw 로 씬 전환.

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
                self.Main.addScene(screen, GameScenes.ScoreHandler.getPlayers()) # addScene은 체크표시 같은 추가 화면을 표현해줍니다.
                # Player 수가 선택되지 않고 스타트를 눌렀을 때의 경고메시지
                if self.Main.Trigger_Message:
                    self.Main.printMessage(screen)

            if self.Help.Trigger:
                self.Help.startScene(screen)

            if self.ReadyDraw.Trigger:
                self.ReadyDraw.startScene(screen)
                if self.ReadyDraw.Trigger_ScoreBoard:
                    self.ReadyDraw.printScoreBoard(screen)
                # 랜덤 단어를 창에 표시
                if self.ReadyDraw.Trigger_Message:
                    self.ReadyDraw.printMessage(screen)

            if self.Drawing.Trigger:
                self.Drawing.addScene(screen, color, size) # 마찬가지의 AddScene. 순서가 바뀌면 그려지는 순서가 달라져서 버그발생.
                self.Drawing.startScene(screen)
                self.Drawing.DisplayTurn()
                if 150 <= mouseX and mouseX <= 1140 and 0 <= mouseY and mouseY <= 600 and mouseflag == True:
                    self.Drawing.Sketch(screen, color, size, mouseX, mouseY) # Mouseflag는 아래 Event에서 전환됩니다.

            if self.Guess.Trigger:
                self.Guess.startScene(screen)
                if self.Guess.Trigger_PlayerCheck == 1:
                    self.Guess.addScene(screen, 1)
                if self.Guess.Trigger_PlayerCheck == 2:
                    self.Guess.addScene(screen, 2)
                if self.Guess.Trigger_PlayerCheck == 3:
                    self.Guess.addScene(screen, 3)
                if self.Guess.Trigger_PlayerCheck == 4:
                    self.Guess.addScene(screen, 4)

            if self.Result.Trigger:
                self.Result.startScene(screen)


            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONUP:
                    mouseflag = False # 그림판 기능 때문에 추가된 줄.

                if pygame.key.get_focused() and keyInput == True and event.type == pygame.KEYDOWN: # Guess에서, 키보드 입력을 받기 위한 구문.
                    press = pygame.key.get_pressed()
                    for i in range(0, len(press)):
                        if press[i] == 1:
                            name = pygame.key.name(i)
                            print("Input " + name)  # Debug
                            if self.Guess.DicCheck(name) :
                                guessword += name
                                print("GuessWord = " + guessword)  # Debug
                                self.Guess.DrawInput(guessword, screen)
                            elif name == 'backspace':
                                try :
                                    guessword = guessword.rstrip(guessword[-1])
                                    self.Guess.DrawInput(guessword, screen)
                                except :
                                    print("Bug")
                            elif name == 'return':
                                if guessword == self.ReadyDraw.WordHandler.answer:  # 맞았을 때
                                    a = self.Guess.NowQuizNum()
                                    b = self.Guess.NowQuizLimit()
                                    if a < b :
                                        self.Guess.Correct(screen)
                                        print(" $$$" , self.Guess.Trigger_PlayerCheck)
                                        print(" $$$", self.Guess.NowPlaying())
                                        c = self.Guess.NowPlaying()
                                        d = str("player" + str(c))
                                        self.Guess.AddScore(d)
                                        reDraw = True
                                        keyInput = False
                                        self.Guess.NextTrun()
                                    elif a >= b :
                                        reDraw = True
                                        keyInput = False
                                        self.Guess.Off()
                                        self.Result.On()
                                        screen.blit(self.background, (0, 0))
                                        pygame.display.flip()

                                elif guessword != self.ReadyDraw.WordHandler.answer:  # 틀렸을 때
                                    self.Guess.Wrong(screen)
                                    keyInput = False


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
                                self.Guess.LimitCheck()  # 실행될 때 Limit값을 생성함.
                            else:
                                self.Main.Trigger_Message = True

                        elif self.Main.clickCheck() == '2 Players':
                            self.Main.setPlayers(2)
                            self.ReadyDraw.setScoreBoard()
                            screen.blit(self.background, (0, 0))

                        elif self.Main.clickCheck() == '3 Players':
                            self.Main.setPlayers(3)
                            self.ReadyDraw.setScoreBoard()
                            screen.blit(self.background, (0, 0))

                        elif self.Main.clickCheck() == '4 Players':
                            self.Main.setPlayers(4)
                            self.ReadyDraw.setScoreBoard()
                            screen.blit(self.background, (0, 0))

                    if self.Help.Trigger:
                        if self.Help.clickCheck() == 'Quit':
                            done = True

                        elif self.Help.clickCheck() == 'Back':
                            self.Main.On()
                            self.Help.Off()
                            screen.blit(self.background, (0,0))
                            pygame.display.flip()

                    # ReadyDraw Scene Click Event
                    if self.ReadyDraw.Trigger:

                        if self.ReadyDraw.clickCheck() == 'Quit':
                            done = True
                        elif self.ReadyDraw.clickCheck() == 'GetWord':
                            self.ReadyDraw.getWord()
                            self.ReadyDraw.setWordText()
                            self.ReadyDraw.Trigger_Message = True
                            self.ReadyDraw.setScoreBoard()
                            self.ReadyDraw.Trigger_ScoreBoard = True
                        elif self.ReadyDraw.clickCheck() == 'Next':
                            self.ReadyDraw.Off()
                            self.Drawing.On()
                            screen.blit(self.background, (0, 0))
                            pygame.display.flip()

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
                            keyInput = False
                        if self.Guess.clickCheck() == 'Player 1':
                            self.Guess.Trigger_PlayerCheck = 1
                        if self.Guess.clickCheck() == 'Player 2':
                            self.Guess.Trigger_PlayerCheck = 2
                        if self.Guess.clickCheck() == 'Player 3':
                            self.Guess.Trigger_PlayerCheck = 3
                        if self.Guess.clickCheck() == 'Player 4':
                            self.Guess.Trigger_PlayerCheck = 4
                        if self.Guess.clickCheck() == 'Quit':
                            done = True
                        if self.Guess.clickCheck() == 'InputAnswer':
                            guessword =""
                            keyInput = True
                        if event.type == pygame.MOUSEBUTTONDOWN and reDraw == True and self.Guess.Trigger == True:
                            self.Guess.Off()
                            self.Drawing.Off()
                            self.ReadyDraw.On()
                            self.ReadyDraw.getWord()
                            self.ReadyDraw.setWordText()
                            self.ReadyDraw.Trigger_Message = True
                            reDraw = False
                            screen.blit(self.background, (0, 0))
                            pygame.display.flip()


                    # Result Scene Click Event
                    if self.Result.Trigger:
                        if self.Result.clickCheck() == "ScoreBoard":
                            self.Result.WinnerCheck(screen)
                        if self.Result.clickCheck() == "Quit":
                            done = True

            pygame.display.flip()



    pygame.quit()

start = SceneLoader()
start.GameLoop()

