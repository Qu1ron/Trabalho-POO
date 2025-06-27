from settings import *

class jogo:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Turn Rpg')

    def run(self):
        while True:
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
            #logica do jogo
            pygame.display.update()

if __name__ == '__main__':
    jogo = jogo()
    jogo.run()