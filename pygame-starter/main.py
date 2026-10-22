"""A tiny Pygame game that also runs in the browser.

Run it in the browser (this is the normal way in a codespace):
    pygbag --port 3000 pygame-starter
then open the forwarded port 3000 when the notification appears.

The only rule for browser-friendly Pygame: the game loop is `async` and
calls `await asyncio.sleep(0)` once per frame. Everything else is ordinary
Pygame. On a real desktop the same file runs with `python main.py`.
"""
import asyncio
import pygame
wow = True
WIDTH, HEIGHT = 6400, 4000
global screen

def off():
    pygame.draw.circle(screen,(0,0,0),(WIDTH // 2,HEIGHT // 2),30)

async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Trillium starter")
    clock = pygame.time.Clock()
    x, y, speed = WIDTH // 20, HEIGHT // 20, 40
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if wow == False:
            off()       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_PERIOD]:
            wow = not wow
        

        screen.fill((125, 225, 125))
        clock.tick(600)
        await asyncio.sleep(0)  # hands control to the browser once per frame

    pygame.quit()


asyncio.run(main())

