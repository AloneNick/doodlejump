import pygame
from settings import *
from movement import *
from map import *
from render import *
poz = 1
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))#,pygame.FULLSCREEN
pygame.display.set_caption('DOODLEJUMP')

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('GeeksForGeeks', True, (0,0,0), (255,255,255))
#clock = pygame.time.Clock()
running = True



while running:
    while True:
        game_end(running)
        sc.blit(BACKGROUND,(0,0))
        play = (WIDTH//2-WIDTH//8,HEIGHT//2-HEIGHT//12,WIDTH//4,HEIGHT//12)
        sett = (WIDTH//2-WIDTH//8,play[1]+play[3]+10,WIDTH//4,HEIGHT//12)
        if BUT(sc,sett,WHITE,BLACK,"Настройки"):
            print("press settings")
        if BUT(sc,play,WHITE,BLACK,"Играть"):
            game_over = False
            Map=create_map()
            PLAYER_POZ = [WIDTH//2-PLAYER[0].get_rect().size[0]//2,HEIGHT-(PLAYER[0].get_rect().size[1]+PLATFORM.get_rect().size[1]+1)]
            v = 6
            m = 1
            score = 0
            break   
    
        pygame.display.flip()

    #сам процесс игры
    
    #game_over = False
    while game_over == False:
        sc.blit(BACKGROUND,(0,0))#BACKGROUND
        keys = pygame.key.get_pressed()
        poz = mov_player_gor(keys,PLAYER_POZ,poz)
        out_map_sc(sc,Map)#отрисовка карты
        out_player_sc(sc,PLAYER[poz],PLAYER_POZ)#отрисовка игрока
        show_score(sc,score)#отрисовка счета
        pygame.display.flip()#обновление дисплея"""
        running = game_end(running)#функция выхода из программы
        pygame.time.delay(1000//MAX_FPS)#функция задержки

        if game_over==False:
            F =((1 / 2)*m*(v**2))//1
            if PLAYER_POZ[1]>=HEIGHT//3 or F<0:
                PLAYER_POZ[1]-= F
            else:
                mov_map(Map,F,RANDOM_SIZE)
                score+=F
            v = v-0.2
            if v<0:
                m =-1
            if (collis(PLAYER[poz],PLAYER_POZ,Map,F)== False and v<=0.2): #or PLAYER_POZ[1]+PLAYER[poz].get_rect().size[1] >= HEIGHT: #or v ==-11:
                v = 6
                m = 1
        if PLAYER_POZ[1]+PLAYER[poz].get_rect().size[1] >= HEIGHT:
            while game_over == False:
                font = pygame.font.Font('freesansbold.ttf', 30)
                text_score = font.render(str(int(score)), False, (0,0,0))
                text_score_inp = font.render("Счет", False, (0,0,0))

                
                end_game = (WIDTH//10,HEIGHT//5,WIDTH*0.8,HEIGHT*0.6)
                but_reload = (end_game[0]+end_game[2]//20,end_game[1]+end_game[3]-50-end_game[3]//20,end_game[2]//2-(end_game[2]//10),50)
                but_exit = (end_game[0]+end_game[2]//20+but_reload[2]+end_game[2]//10,end_game[1]+end_game[3]-50-end_game[3]//20,end_game[2]//2-(end_game[2]//10),50)
                pygame.draw.rect(sc, (255, 165, 0), pygame.Rect(end_game),  0, 15)
                sc.blit(text_score_inp,(WIDTH//2-text_score_inp.get_rect().size[0]//2,HEIGHT//3-32))
                sc.blit(text_score,(WIDTH//2-text_score.get_rect().size[0]//2,HEIGHT//3))
                if BUT(sc,but_exit,WHITE,BLACK,"Выход"):
                    game_over = True
                    break
                if BUT(sc,but_reload,WHITE,BLACK,"Сначала"):
                    Map=create_map()
                    PLAYER_POZ = [WIDTH//2-PLAYER[0].get_rect().size[0]//2,HEIGHT-(PLAYER[0].get_rect().size[1]+PLATFORM.get_rect().size[1]+1)]
                    score=0
                    break
                game_end(running)
                pygame.display.flip()
        
        
    
pygame.quit()