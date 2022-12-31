import pygame, sys, time, random

# check error game
check_errors = pygame.init()
if check_errors[1] > 0:
    print("[!] {check_errors} error game")
else:
    print("[+] Game succes install")

# window game
size_x = 720
size_y = 480

# title game
pygame.display.set_caption("MY ULAR")
screen = pygame.display.set_mode((size_x, size_y))

# variabel game color 
black = pygame.Color (0,0,0)
white = pygame.Color (255,255,255,255)
green = pygame.Color (0,255,0)
red   = pygame.Color (255,0,0)

# variabel snake
snake_pos = [100,50]
snake_body = [snake_pos,snake_pos,snake_pos]

# variabel arah ular
change_to = "RIGHT"
direction = "RIGHT"

# food
food_pos = [random.randrange(1, size_x // 10) * 10 , random.randrange(1, size_y // 10) * 10]
food_spawn = True

# background color
screen.fill(white)

# running window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"

    # update screen color again
    screen.fill(white)
    
    # create snake
    for pos in snake_body:
        pygame.draw.ellipse(screen, green, pygame.Rect(pos[0],pos[1],10,10))
    snake_body.insert(0, snake_pos[:])

    # snake run (tidak bisa mundur)
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    if direction == "RIGHT":
        snake_pos[0] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10

    # snake over window
    if snake_pos[0] > size_x:
        snake_pos[0] = 1
    if snake_pos[0] < 1:
        snake_pos[0] = size_x
    if snake_pos[1] > size_y:
        snake_pos[1] = 1
    if snake_pos[1] < 1:
        snake_pos[1] = size_y

    # draw food
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # snake eating food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False 
    else:
        snake_body.pop()

    # logic food spawn
    if not food_spawn:
        food_pos = [random.randrange(1, size_x // 10) * 10 , random.randrange(1, size_y // 10) * 10]
    food_spawn = True
    # level run
    pygame.time.Clock().tick(10)

    # update screen
    pygame.display.update()