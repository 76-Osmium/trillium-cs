"""A tiny Pygame game that also runs in the browser.

Run it in the browser (this is the normal way in a codespace):
    pygbag --port 3000 pygame-starter
then open the forwarded port 3000 when the notification appears.

The only rule for browser-friendly Pygame: the game loop is `async` and
calls `await asyncio.sleep(0)` once per frame. Everything else is ordinary
Pygame. On a real desktop the same file runs with `python main.py`.
"""
# this file draws a black screen on the browser with a set number of pixels, sets the tick speed, and refreshes the screen. The variables used are: (Width:X pixels,Height:Y pixels,Screen:
import asyncio 
# only here for sleep comand.
import pygame 
# allows for draw commands
import crashscreen  
# shows errors on the game screen and in the terminal
WIDTH, HEIGHT = 640, 400
# pixels on the screen
async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Trillium starter")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False   

        screen.fill((225, 225, 225))
        # fills screen with chosen color (black)
        pygame.display.flip()
        # resets the screen
        clock.tick(60)
        # tick every 60 milliseconds
        await asyncio.sleep(0)  

    pygame.quit()

asyncio.run(crashscreen.guard(main))

