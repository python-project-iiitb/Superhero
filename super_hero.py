import pygame
import math
import functions
from pygame import mixer


class super_hero:
    logo_img = pygame.image.load("logo.png")

    def __init__(self):
        mixer.init()
        # background music
        mixer.music.load("background_music.flac")
        mixer.music.play(-1)

        # initialising pygame
        pygame.init()
        pygame.display.set_caption("SUPER HERO")

        # displaying the screen
        self.screen = pygame.display.set_mode((1200, 920))
        self.bg_color = (120, 220, 220)
        self.lost = 0
        self.score = 0
        self.start = 0
        self.user_name = ''
        self.sh_img_x = 25
        self.sh_img_y = 880
        self.win = 0

    def run_sh(self):
        run = True

        # dictionary of lines containing its coordinates and moving speed
        lines = {
            'l1': [200, 820, 1000, 820, 1, 1], 'l2': [100, 720, 500, 720, 1, 1],
            'l3': [600, 720, 1100, 720, 1, 1], 'l4': [100, 620, 350, 620, 1, 1],
            'l5': [450, 620, 700, 620, 1, 1], 'l6': [800, 620, 1050, 620, 1, 1],
            'p1': [200, 100, 1000, 100, 1, 1], 'p2': [100, 200, 500, 200, 1, 1],
            'p3': [600, 200, 1100, 200, 1, 1], 'p4': [100, 300, 350, 300, 1, 1],
            'p5': [450, 300, 700, 300, 1, 1], 'p6': [800, 300, 1050, 300, 1, 1]
        }

        # dictionary of coins with their coordinates as value to the keys
        coins = {
                'c1': [300, 785], 'c2': [600, 785], 'c3': [900, 785], 'c4': [300, 685], 'c5': [550, 685], 'c6': [800, 685],
            'c7': [225, 585], 'c8': [575, 585],
            'c9': [925, 585], 'c10': [300, 65], 'c11': [600, 65], 'c12': [900, 65], 'c13': [300, 165],
            'c14': [550, 165], 'c15': [800, 165], 'c16': [225, 265],
            'c17': [575, 265], 'c18': [925, 265], 'c19': [25, 785], 'c20': [1140, 785], 'c21': [1140, 685],
            'c22': [27, 705], 'c23': [1140, 165],
            'c24': [30, 165], 'c25': [1140, 65], 'c26': [25, 65]
        }

        # loading all the required images(superhero,dragon,fire,cactus,coin)
        sh_img = pygame.image.load("sh2.png")
        drg_img = pygame.image.load("dragon.png")
        fire_img = pygame.image.load("fire.png")
        cactus_img = pygame.image.load("cactus32.png")
        c_img = pygame.image.load("cn.png")
        flag_img = pygame.image.load("flag.png")
        gunman_img=pygame.image.load("gunman.png")
        bullet_img=pygame.image.load("bullet.png")
        f_coin = pygame.image.load("flatcoin.png")

        # setting the coodinates of all required images and planks
        sh_img_ch_x = 0
        sh_img_ch_y = 0
        fire_img_x = 1050
        bullet_img_x=150

        # SCORE
        font = pygame.font.Font('game_over.ttf', 65)
        textX = 50
        textY = 35
        def show_score(x, y):
            score = font.render("Score :" + " " + str(self.score), True, (0, 0, 0))
            self.screen.blit(score, (x, y))

        # an infinite loop to keep the screeen active
        count=0
        while run:
            if((self.win and self.score == 26) or self.lost != 0):
                run = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        sh_img_ch_y = -1
                    if event.key == pygame.K_DOWN:
                        sh_img_ch_y = +1
                    if event.key == pygame.K_LEFT:
                        sh_img_ch_x = -1
                    if event.key == pygame.K_RIGHT:
                        sh_img_ch_x = +1
                if event.type == pygame.KEYUP:
                    if (
                            event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT
                    ):
                        sh_img_ch_x = 0
                        sh_img_ch_y = 0
            self.screen.fill(self.bg_color)
            self.sh_img_x += sh_img_ch_x
            self.sh_img_y += sh_img_ch_y
            functions.sh(self.sh_img_x, self.sh_img_y, sh_img, self.screen)

            # keeping super_hero within screen limits
            if (self.sh_img_x <= 0):
                self.sh_img_x = 0
            elif (self.sh_img_x >= 1160):
                self.sh_img_x = 1160
            elif (self.sh_img_y <= 8):
                self.sh_img_y = 8
            elif (self.sh_img_y >= 870):
                self.sh_img_y = 870

            # losing the game when touched by cactus
            if (functions.cactus_out(self.sh_img_x, self.sh_img_y)):
                self.lost += 1
                run = False

            # making all the planks move
            x=0.5
            for i in lines.values():
                pygame.draw.line(self.screen, (0, 0, 0), [i[0], i[1]], [i[2], i[3]], 5)
                i[0] += i[4]
                i[2] += i[5]
                if (i[2] == 1200):
                    i[4] = -1
                    i[5] = -1
                if (i[0] == 0):
                    i[4] = 1
                    i[5] = 1

            # collecting coins
            for i in coins.values():
                x = functions.collect(i[0], i[1], self.sh_img_x, self.sh_img_y)
                if x:
                    self.score += 1
                    i[0] = 2000
                    i[1] = 2000

            # displaying all coins
            if(count>=0 and count<100):
                for i in coins.values():
                    functions.coin(i[0], i[1], c_img, self.screen)
            elif(count>=100 and count<200):
                for i in coins.values():
                    functions.coin(i[0], i[1], f_coin, self.screen)

            if(count==200):
                count=0
            count+=1     
                    


            # losing the game when touched by planks
            for i in lines.values():
                if functions.line_out(i[0], i[1], i[2], i[3], self.sh_img_x, self.sh_img_y):
                    self.lost += 1
                    run = False

            # displaying the images 
            self.screen.blit(gunman_img,(10,360))
            self.screen.blit(drg_img, (1050, 460))
            self.screen.blit(drg_img, (1050, 360))
            self.screen.blit(flag_img, (1050, -5))
            for i in range(0, 920, 40):
                self.screen.blit(cactus_img, (3, i))
                self.screen.blit(cactus_img, (1170, i))

            #bullets by gunman
            bullet_img_x+=1
            functions.shoot(bullet_img_x,400,bullet_img,self.screen)
            functions.shoot(bullet_img_x,460,bullet_img,self.screen)

            # fire by dragon
            fire_img_x -= 1
            functions.fire(fire_img_x, 490, fire_img, self.screen)
            functions.fire(fire_img_x, 390, fire_img, self.screen)
        

            # bringing fire and bullets back to the dragon mouth and gun once reaches end of the screen
            if (fire_img_x == 0):
                fire_img_x = 1050
            if(bullet_img_x == 1200):
                bullet_img_x = 150

            # losing the game when burnt due to fire
            if (functions.fire_out(self.sh_img_x, self.sh_img_y, fire_img_x, 490)):
                self.lost += 1
                run = False
            if (functions.fire_out(self.sh_img_x, self.sh_img_y, fire_img_x, 390)):
                self.lost += 1
                run = False

            #losing game when shot by bullet
            if (functions.bullet_out(self.sh_img_x, self.sh_img_y, bullet_img_x, 400)):
                print("you are lost")
                self.lost += 1
                run = False
            if (functions.bullet_out(self.sh_img_x, self.sh_img_y, bullet_img_x, 460)):
                print("you are lost")
                self.lost += 1
                run = False


            # losing the game when super_hero touches dragon
            if (functions.drag_out(self.sh_img_x, self.sh_img_y, 1050, 460) and self.sh_img_y > 440 and self.sh_img_y < 560):
                print("you are lost")
                self.lost += 1
                run = False
            if (functions.drag_out(self.sh_img_x, self.sh_img_y, 1050, 360) and self.sh_img_y > 340 and self.sh_img_y < 440):
                print("you are lost")
                self.lost += 1
                run = False

            #losing game when super_hero touches gunman
            if (functions.gunman_out(self.sh_img_x, self.sh_img_y, 10, 400) and self.sh_img_y > 440 and self.sh_img_y < 560):
                print("you are lost")
                self.lost += 1
                run = False
            if (functions.gunman_out(self.sh_img_x, self.sh_img_y, 10, 460) and self.sh_img_y > 340 and self.sh_img_y < 440):
                print("you are lost")
                self.lost += 1
                run = False



            c = (self.sh_img_x - 1050)**2 + (self.sh_img_y + 5)**2 - 50**2
            if(c < 0):
                self.win = 1
            show_score(textX, textY)

            pygame.display.update()

    def win_screen(self):
        run = True
        while run:
            mixer.init()
            # background music
            winner_sound = mixer.Sound("winner_sound.wav")
            winner_sound.play()
            trophy=pygame.image.load("trophy.png")
            flowers=pygame.image.load("flowers.png")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.screen.fill(self.bg_color)
            font1 = pygame.font.Font('logo.ttf',100)
            congo = font1.render("Congratulations!!",True,(255,0,0))
            font = pygame.font.Font(None, 100)
            winner = font.render("YOU WIN!", True, (0, 0, 0))
            self.screen.blit(flowers,(0,0))
            self.screen.blit(winner, (400, 60))
            self.screen.blit(congo,(250,160))
            self.screen.blit(trophy,(350,310))
            pygame.display.update()

    def lost_screen(self):
        run = True
        while run:
            if(self.win and self.score == 26):
                run = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # print("you are lost")
            # print("score = ",self.score)
            self.screen.fill(self.bg_color)
            font = pygame.font.Font(None, 70)
            textX = 250
            textY = 200

            def show_score(x, y):
                sorry = font.render("GAME OVER!!! ", True, (0, 0, 0))
                lost = font.render("TRY AGAIN  "+str(self.user_name), True, (0, 0, 0))
                score = font.render("SCORE : " +str(self.score), True, (0, 0, 0))
                #text_surface = font.render(self.user_name, True, (0, 0, 0))
                #self.screen.blit(text_surface,  (x-100, y + 200))
                self.screen.blit(score, (x-100, y-100))
                self.screen.blit(lost, (x-100, y+300))
                self.screen.blit(sorry, (x-100, y+100))

            show_score(250, 200)
            cry_img = pygame.image.load("cry.png")
            self.screen.blit(cry_img, (700, 100))
            mixer.init()
            cry_sound = mixer.Sound("cry_sound.wav")  # cry sound
            cry_sound.play()
            pygame.display.update()

    def front_screen(self):
        run = True
        while run:
            if(self.win and self.score == 26):
                run = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_name = self.user_name[:-1]
                    else:
                        self.user_name += event.unicode
                    if event.key == pygame.K_SPACE:
                        self.start = 1
                        run = False
            font1 = pygame.font.Font('logo.ttf',100)            
            self.screen.fill(self.bg_color)
            self.screen.blit(super_hero.logo_img,(700,200))
            font = pygame.font.Font(None, 70)


            def show_details(x, y):
                welcome = font.render(
                    "Welcome to Super Hero ", True, (0, 0, 0))
                Instruction = font.render(
                    "Press SPACE bar to start the game", True, (0, 0, 0))
                name = font.render("Enter your name: ", True, (0, 0, 0))
                base_font = pygame.font.Font(None, 70)
                logo = font1.render("SUPER HERO",True,(255,20,10))
                #user_name = 'Hello '
                # if event.type == pygame.KEYDOWN:
                #user_name += event.unicode
                text_surface = base_font.render(self.user_name, True, (0, 0, 0))
                self.screen.blit(welcome, (x+20,y - 300))
                self.screen.blit(Instruction, (x - 150, y + 400))
                self.screen.blit(name, (x - 180, y - 180))
                self.screen.blit(text_surface, (x+230 , y - 180))
                self.screen.blit(logo,(x-170,y+50))
    

            show_details(300, 350)
            pygame.display.update()


if __name__ == "__main__":
    sh = super_hero()
    sh.front_screen()
    if (sh.start == 1):
        sh.run_sh()
    if (sh.lost != 0):
        sh.lost_screen()
    if(sh.win and sh.score == 26):
        sh.win_screen()
