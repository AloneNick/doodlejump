from settings import *
from map import *
from render import *
from map import *

def collis(PLAYER,PLAYER_POZ,Map,F):
    ind_map = len(Map)-1
    
    while Map[ind_map][1]<PLAYER_POZ[1]+PLAYER.get_rect().size[1]:
        if ind_map>0:
            ind_map-=1
        else:
            break
    coll_gor2=False
    coll_gor = max(Map[ind_map][0],PLAYER_POZ[0])<min(Map[ind_map][0]+PLATFORM2.get_rect().size[0],PLAYER_POZ[0]+PLAYER.get_rect().size[0])
    if PLAYER_POZ[0]+PLAYER.get_rect().size[0]>WIDTH:
        coll_gor2=PLAYER_POZ[0]+PLAYER.get_rect().size[0]-WIDTH>Map[ind_map][0]
    col_ver = PLAYER_POZ[1]+PLAYER.get_rect().size[1]+abs(F) >= Map[ind_map][1]>=(PLAYER_POZ[1]+PLAYER.get_rect().size[1])-abs(F)
    if (coll_gor or coll_gor2) and col_ver:
        return False
    else:
        return True


def trans_disp(keys,map):
    if keys[pygame.K_w]:
        mov_map(map,2)

def mov_player_gor(keys,PLAYER_POZ,poz):
    if keys[pygame.K_a]:
        poz=1
        PLAYER_POZ[0]-=5.0
        if PLAYER_POZ[0]<0:
            PLAYER_POZ[0]+=WIDTH
    if keys[pygame.K_d]:
        poz=0
        PLAYER_POZ[0]+=5.0
        if PLAYER_POZ[0]>WIDTH:
            PLAYER_POZ[0]-=WIDTH
    return poz

def game_end(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#выход из приложения
            pygame.quit()
    return running
    
