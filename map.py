import random
from settings import *

def create_map():
    Map = [[WIDTH//2-PLATFORM2.get_rect().size[0]//2,HEIGHT-PLATFORM2.get_rect().size[1]]]
    while Map[len(Map)-1][1]>=0:
        Map.append([random.randint(0,WIDTH-PLATFORM2.get_rect().size[0]),Map[-1][1]-random.randint(180//RANDOM_SIZE[0],180//RANDOM_SIZE[1])])
    return Map

def mov_map(map,mov,RANDOM_SIZE):
    for i in range(len(map)):
        map[i][1]=map[i][1]+mov
    if map[0][1]>HEIGHT:
        map.pop(0)
    if map[-1][1]>=0:
        range_rand = random.randint(int(180//RANDOM_SIZE[0]),int(180//RANDOM_SIZE[1])-1)
        #print(range_rand)
        map.append([random.randint(0,WIDTH-PLATFORM2.get_rect().size[0]),map[-1][1]-range_rand])