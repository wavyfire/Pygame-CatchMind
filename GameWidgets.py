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
        mouseposition = pygame.mouse.get_pos()
        if mouseposition > self.rect.topleft and mouseposition < self.rect.bottomright:
            return True

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