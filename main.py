import pygame, asyncio, random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

player_image = pygame.image.load("assets/player.png").convert_alpha()
player_image = pygame.transform.scale(
    player_image,
    (50, 50)
)
cupcake_image = pygame.image.load(
    "assets/cupcake.png"
).convert_alpha()

cupcake_image = pygame.transform.scale(
    cupcake_image,
    (30, 30)
)

platforms = [
    pygame.Rect(0, 350, 600, 50),
    pygame.Rect(100, 270, 150, 20),
    pygame.Rect(350, 220, 150, 20)
]
cupcakes = [
    pygame.Rect(150, 230, 30, 30),
    pygame.Rect(400, 180, 30, 30),
    pygame.Rect(520, 310, 30, 30)
]


async def main():
    player_x = 50
    player_y = 300
    player_dy = 0
    gravity = 0.5
    jump_speed = -10
    score = 0
    on_ground = True
    time = 60
    running = True
    while running and time > 0:
        time -= 1/60
        if len(cupcakes) == 0:
            cupcakes.append(pygame.Rect(random.randint(50, 550), random.randint(150, 250), 30, 30))
        player_rect = pygame.Rect(
            player_x,
            player_y,
            50,
            50
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        on_ground = False
        for plat in platforms:
            if player_x + 50 > plat.bottomleft[0] and player_x < plat.bottomright[0] and plat.topleft[1] - (player_y + 50) < 2 and plat.bottomleft[1] > player_y + 50:
                player_y = plat.topleft[1] - 50
                player_dy = 0
                on_ground = True

        if keys[pygame.K_LEFT]:
            player_x -= 5
        if keys[pygame.K_RIGHT]:
            player_x += 5
        if keys[pygame.K_UP] and on_ground:
            player_dy = jump_speed
            on_ground = False
        if not on_ground:
            player_dy += gravity
        player_y += player_dy

        for cupcake in cupcakes[:]:
            if player_rect.colliderect(cupcake):
                cupcakes.remove(cupcake)
                score += 1

        for plat in platforms:
            if player_rect.colliderect(plat) and player_y >= plat.topleft[1]:
                    player_y = plat.bottomleft[1]
                    player_dy = 0

        screen.fill((0,0,0))
        screen.blit(player_image, (player_x, player_y))
        for platform in platforms:
            pygame.draw.rect(
                screen,
                (100, 180, 100),
                platform
            )
        for cupcake in cupcakes:
            screen.blit(
                cupcake_image,
                (cupcake.x, cupcake.y)
            )
        font = pygame.font.Font(None, 50)
        text_surface = font.render("score: " + str(score), False, (255, 255, 255))
        screen.blit(text_surface, (0, 0))
        text_surface = font.render("0:" + str(int(time)), False, (255, 255, 255))
        screen.blit(text_surface, (525, 0))
        pygame.display.flip()

        await asyncio.sleep(1/60)


    

asyncio.run(main())

