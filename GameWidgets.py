import pygame

#버튼 생성 클래스
class Button(pygame.sprite.Sprite):

    def __init__(self, loaction, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = loaction

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)

    def clickChecker(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        center = self.rect.center
        w = self.rect.width
        h = self.rect.height
        if (center[0] <= mouseX < center[0] + (w) and center[1]<= mouseY < center[1] + h):
            # 이미지 생성 위치와 이미지 크기가 안맞아서 이렇게 해야합니다.
            return True
        else:
            return False

#글자 생성 클래스
class Font:

    def __init__(self, text, color, size, location):
        self.text = text
        self.color = color
        self.size = size
        self.location = location

        pygame.font.init()
        self.font = pygame.font.SysFont("Bree Serif", self.size)
        self.textObj = self.font.render(self.text, True, self.color)
        self.textRect = self.textObj.get_rect()
        self.textRect.center = location
        pygame.font.quit()

    def draw(self, screen):
        screen.blit(self.textObj, self.textRect)

    def guessInput(self, name):
        pygame.font.init()
        f1 = pygame.font.SysFont("comicsansms", 24)
        text = f1.render(name, True, (0,0,0))
        pygame.font.quit()
        return text