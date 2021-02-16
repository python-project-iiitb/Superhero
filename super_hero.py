import pygame

class super_hero:
    def __init__(self):
        pygame.init()   #initialising pygame
        pygame.display.set_caption("SUPER HERO")

        #creating the screen
        self.screen=pygame.display.set_mode((1200,800))
        self.bg_color=(67,47,117)



    def run_sh(self):
        run=True
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__=="__main__":
    sh=super_hero()
    sh.run_sh()
        

