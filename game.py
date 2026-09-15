import pygame, asyncio

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

player_image = pygame.image.load("assets/player.png").convert_alpha()
player_image = pygame.transform.scale(
    player_image,
    (50, 50)
)


async def main():
    player_x = 50
    player_y = 300
    player_dy = 0
    gravity = 0.5
    jump_speed = -10
    on_ground = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_x -= 5

        if keys[pygame.K_RIGHT]:
            player_x += 5
        if keys[pygame.K_UP] and on_ground:
            player_dy = jump_speed
            on_ground = False
        player_dy += gravity
        player_y += player_dy
        if player_y >= 300:
            player_y = 300
            player_dy = 0
            on_ground = True

        screen.fill((0,0,0))
        screen.blit(player_image, (player_x, player_y))
        pygame.display.flip()

        await asyncio.sleep(1/60)

asyncio.run(main())

