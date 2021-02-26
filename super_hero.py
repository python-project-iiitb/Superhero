import pygame
import math


class super_hero:
    def __init__(self):
        pygame.init()   #initialising pygame
        pygame.display.set_caption("SUPER HERO")

        #creating the screen
        self.screen=pygame.display.set_mode((1200,920))
        self.bg_color=(170,255,255)

        

    def run_sh(self):
        run=True
        lines={
                'l1':[200,820,1000,820,1,1],
                'l2':[100,720,500,720,1,1],
                'l3':[600,720,1100,720,1,1],
                'l4':[100,620,350,620,1,1],
                'l5':[450,620,700,620,1,1],
                'l6':[800,620,1050,620,1,1],
                'p1':[200,100,1000,100,1,1],
                'p2':[100,200,500,200,1,1],
                'p3':[600,200,1100,200,1,1],
                'p4':[100,300,350,300,1,1],
                'p5':[450,300,700,300,1,1],
                'p6':[800,300,1050,300,1,1]
                }
        coins={
                'c1':[300,785],
                'c2':[600,785],
                'c3':[900,785],
                'c4':[300,685],
                'c5':[550,685],
                'c6':[800,685],
                'c7':[225,585],
                'c8':[575,585],
                'c9':[925,585],
                'c10':[300,65],
                'c11':[600,65],
                'c12':[900,65],
                'c13':[300,165],
                'c14':[550,165],
                'c15':[800,165],
                'c16':[225,265],
                'c17':[575,265],
                'c18':[925,265]
                }            
        sh_img=pygame.image.load("sh2.png")
        drg_img=pygame.image.load("dragon.png")
        sh_img_x = 25
        sh_img_y = 880
        sh_img_ch_x=0
        sh_img_ch_y=0
        fire_img_x=1050
        c_img = pygame.image.load("cn.png")                                #including coin image.
        grass_img=pygame.image.load("grass.png")
        fire_img=pygame.image.load("fire.png")
        
        def sh(x,y,sh_img):
            self.screen.blit(sh_img,(x,y))
        def fire(x,y,f_img):
            self.screen.blit(fire_img,(x,y))
        def fire_out(s_x,s_y,f_x,f_y):
            d=math.sqrt(pow(s_x-f_x,2)+pow(s_y-f_y,2))
            if(d<20):
                return True
            else:
                return False            

        def line_out(x1,y1,x2,y2,sh_x,sh_y):
            m = (y2-y1)/(x2-x1)               
            d =-1*((m*sh_x)-(sh_y)+(y1-m*x1))/math.sqrt(1+m*m)            #line eq is m*x-y+(y1-m*x1)
            if(sh_x > x1 and sh_x < x2):
                if(d<(3) and d>-50):
                    print("you are lost")
                    exit(1)

        
        def coin(x,y,c_image):
            self.screen.blit(c_image,(x,y))

        
        def collect(c_x,c_y,s_x,s_y):
            d = math.sqrt(pow((c_x-s_x),2)+pow((c_y-s_y),2))
            if (d < 35):
                c_x = 2000
                c_y = 2000
                return True
            else:
                return False
            
            

                
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(score)
                    run=False
                if event.type==pygame.KEYDOWN:    
                    if event.key == pygame.K_UP:
                        sh_img_ch_y = -1
                    if event.key == pygame.K_DOWN:
                        sh_img_ch_y = +1
                    if event.key == pygame.K_LEFT:
                        sh_img_ch_x = -1
                    if event.key == pygame.K_RIGHT:
                        sh_img_ch_x = +1
                if event.type==pygame.KEYUP:
                    if(event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                        sh_img_ch_x=0
                        sh_img_ch_y=0
            self.screen.fill(self.bg_color)
        
            sh_img_x += sh_img_ch_x
            sh_img_y += sh_img_ch_y
            sh(sh_img_x,sh_img_y,sh_img)
           # print(str(sh_img_x) + " " + str(sh_img_y))

            if(sh_img_x<=0):
                sh_img_x=0
            elif(sh_img_x>=1160):
                sh_img_x=1160
            elif(sh_img_y<=8):
                sh_img_y=8
            elif(sh_img_y>=870):
                sh_img_y=870

            if(sh_img_x==0 and sh_img_y>=0):
                print("lost")
                exit(0)
            if(sh_img_x==1160 and sh_img_y>=0):
                print('lost')
                exit(0)        

            for i in lines.values():
                pygame.draw.line(self.screen,(0,0,0),[i[0],i[1]],[i[2],i[3]],5)
                i[0]+=i[4]
                i[2]+=i[5]
                if(i[2]==1200):
                    i[4]=-1
                    i[5]=-1
                if(i[0]==0):
                    i[4]=1
                    i[5]=1
            

           

            
            score = 0
            for i in coins.values():
                x = collect(i[0],i[1],sh_img_x,sh_img_y)
                if x:
                    score += 1
                    i[0] = 2000
                    i[1] = 2000
                

            for i in coins.values():
                coin(i[0],i[1],c_img)

            for i in lines.values():
                line_out(i[0],i[1],i[2],i[3],sh_img_x,sh_img_y)
            
            self.screen.blit(drg_img,(1050,460))
            self.screen.blit(drg_img,(1050,360))

            fire_img_x-=1
            fire(fire_img_x,490,fire_img)
            fire(fire_img_x,390,fire_img)
            
            if(fire_img_x==0):
                fire_img_x=1050
            if(fire_out(sh_img_x,sh_img_y,fire_img_x,490)):
                print("you are lost")
                exit(0)
            if(fire_out(sh_img_x,sh_img_y,fire_img_x,390)):
                print("you are lost")
                exit(0)    
            

    
            pygame.display.update()


if __name__=="__main__":
    sh=super_hero()
    sh.run_sh()        

