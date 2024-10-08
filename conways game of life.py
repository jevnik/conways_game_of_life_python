import pygame
import time
import copy
tile = 20

def main():
    w,h = 25,25

    game_res = (w*tile,h*tile)

    game_state = [[0 for i in range(w)] for j in range(h)]

    disp_grid = []

    for x in range(w):
        for y in range(h):
            disp_grid.append(pygame.Rect(x*tile,y*tile,tile,tile))

    pygame.init()
    display = pygame.display.set_mode(game_res)

    while True:
        display.fill(pygame.Color("black"))
        
        for i_rect in disp_grid:
            pygame.draw.rect(display,(40,40,40),i_rect,1)

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x = mouse_x // tile
                mouse_y = mouse_y // tile
                if game_state[mouse_x][mouse_y] == 0:
                    game_state[mouse_x][mouse_y] = 1
                else:
                    game_state[mouse_x][mouse_y] = 0
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("enter pressed")
                    simulation(display, game_state)
        
        draw(game_state,display)
        pygame.display.flip()        


def num_neighbours(x,i,j):
    count = 0
    try:
        if x[i+1][j] == 1:
            count += 1
    except:
        pass
    try:
        if x[i+1][j+1] == 1:
            count +=1
    except:
        pass
    try:  
        if x[i][j+1] == 1:
            count +=1
    except:
        pass

    try:
        if i-1 > 0 and x[i-1][j+1] == 1:
            count +=1
    except:
        pass
    try:        
        if i-1 > 0 and x[i-1][j] == 1:
            count +=1
    except:
        pass        
    try:
        if i-1 > 0 and j-1 > 0 and x[i-1][j-1] == 1:
            count +=1
    except:
        pass
    try:
        if j-1 > 0 and x[i][j-1] == 1:
            count += 1
    except:
        pass
    try:
        if j-1 > 0 and x[i+1][j-1] == 1:
            count += 1
    except:
        pass

    return count

def destiny(x):
    if x == 3:
        return 1
    elif x < 2:
        return 0
    elif x > 3:
        return 0
    else:
        return 2


def simulation(display, game_state):
    clock = pygame.time.Clock()
    
    while True:
        game_state_temp = copy.deepcopy(game_state)
        for i in range(len(game_state)):
            for j in range(len(game_state[i])):
                num = num_neighbours(game_state,i,j)
                if destiny(num) == 1:
                    game_state_temp[i][j] = 1
                elif destiny(num) == 0:
                    game_state_temp[i][j] = 0
                else:
                    pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        game_state = copy.deepcopy(game_state_temp)
        
        draw(game_state,display)
        pygame.display.flip()
        clock.tick(5)         

def draw(x,display):
    for i in range(len(x)):
                for j in range(len(x[i])):
                    if x[i][j] == 1:
                        pygame.draw.rect(display,"white",pygame.Rect(i*tile,j*tile,tile-1,tile-1))
                    elif x[i][j] == 0:
                        pygame.draw.rect(display,"black",pygame.Rect(i*tile,j*tile,tile-1,tile-1))

if __name__ == "__main__":
    main()



    