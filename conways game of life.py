import pygame

w,h = 50,50
tile = 20
game_res = (w*tile,h*tile)
FPS = 10


grid = []
for x in range(w):
    for y in range(h):
        grid.append(pygame.Rect(x*tile,y*tile,tile,tile))

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode(game_res)

while True:
    display.fill(pygame.Color("black"))
    for rect in grid:
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()
    clock.tick(FPS)
    
