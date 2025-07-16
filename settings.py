import pygame

WIDTH = 400
HEIGHT = 600

#img
#BACKGROUND
BACKGROUND = pygame.image.load('img/background/background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND,(WIDTH,HEIGHT))
#PLATFORM
SKINS_PLATFORM = [pygame.image.load('img/platform.png'),pygame.image.load('img/porey.png')]
PLATFORM = SKINS_PLATFORM[0]
SIZE_PLATFORM = 40
PLATFORM2 = pygame.transform.scale(PLATFORM,(PLATFORM.get_rect().size[0]*((HEIGHT/SIZE_PLATFORM)/PLATFORM.get_rect().size[1]),HEIGHT/SIZE_PLATFORM))
#PLAYER
SKINS_PLAYER = [pygame.image.load('img/jumper.png'),pygame.image.load('img/miku.png')]
PLAYER = [SKINS_PLAYER[0],pygame.transform.flip(SKINS_PLAYER[0],True,False)]
SIZE_PLAYER = 10
PLAYER[0] = pygame.transform.scale(PLAYER[0],(PLAYER[0].get_rect().size[0]*((HEIGHT/SIZE_PLAYER)/PLAYER[0].get_rect().size[1]),HEIGHT/SIZE_PLAYER))
PLAYER[1] = pygame.transform.scale(PLAYER[1],(PLAYER[1].get_rect().size[0]*((HEIGHT/SIZE_PLAYER)/PLAYER[1].get_rect().size[1]),HEIGHT/SIZE_PLAYER))

#PLAYER_POZ = [WIDTH//2-PLAYER[0].get_rect().size[0]//2,HEIGHT-(PLAYER[0].get_rect().size[1]+PLATFORM.get_rect().size[1]+1)]
RANDOM_SIZE = [8,4]
#FPS
MAX_FPS = 60

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
