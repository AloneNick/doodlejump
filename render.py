from settings import *
from map import *
from movement import *


def out_map_sc(sc,Map):
    for i in range(len(Map)):
        sc.blit(PLATFORM2,(Map[i][0],Map[i][1]))

def out_player_sc(sc,PLAYER,PLAYER_POZ):
    sc.blit(PLAYER,(PLAYER_POZ[0],PLAYER_POZ[1]))
    if PLAYER_POZ[0]>WIDTH-PLAYER.get_rect().size[0]:
        sc.blit(PLAYER,(PLAYER_POZ[0]-WIDTH,PLAYER_POZ[1]))

def show_score(sc,score):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(str(int(score)), False, (0,0,0))
    textRect = text.get_rect()
    sc.blit(text,(WIDTH-textRect.size[0],0))

def BUT(sc,play,color_on,color_off,text):
    s_text = 18
    font = pygame.font.Font('freesansbold.ttf', s_text)
    Text = font.render(text, False, (150,150,150))
    mousex, mousey = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    if play[0]<=mousex<=play[0]+play[2] and play[1]<=mousey<=play[1]+play[3]:
        pygame.draw.rect(sc, color_on, pygame.Rect(play),  0, 15)#толщина, углы
        sc.blit(Text,(play[0]+play[2]//2-Text.get_rect().size[0]//2,play[1]+play[3]//2-Text.get_rect().size[1]//2))
        if pressed[0]:
            return True
    else:
        pygame.draw.rect(sc, color_off, pygame.Rect(play),  0, 15)
        sc.blit(Text,(play[0]+play[2]//2-Text.get_rect().size[0]//2,play[1]+play[3]//2-Text.get_rect().size[1]//2))
    