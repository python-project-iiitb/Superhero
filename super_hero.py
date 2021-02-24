import pygame


class super_hero:
    def __init__(self):
        pygame.init()   #initialising pygame
        pygame.display.set_caption("SUPER HERO")

        #creating the screen
        self.screen=pygame.display.set_mode((1200,600))
        self.bg_color=(255,253,240)

        

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
        sh_img=pygame.image.load("sh2.png")
        sh_img_x = 25
        sh_img_y = 880
        sh_img_ch_x=0
        sh_img_ch_y=0
        def sh(x,y,sh_img):
            self.screen.blit(sh_img,(x,y))


        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                if event.type==pygame.KEYDOWN:    
                    if event.key == pygame.K_UP:
                        sh_img_ch_y = -0.5
                    if event.key == pygame.K_DOWN:
                        sh_img_ch_y = +0.5
                    if event.key == pygame.K_LEFT:
                        sh_img_ch_x = -0.5
                    if event.key == pygame.K_RIGHT:
                        sh_img_ch_x = +0.5
                if event.type==pygame.KEYUP:
                    if(event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                        sh_img_ch_x=0
                        sh_img_ch_y=0
            self.screen.fill(self.bg_color)
        
            sh_img_x += sh_img_ch_x
            sh_img_y += sh_img_ch_y
            sh(sh_img_x,sh_img_y,sh_img)
            #print(str(sh_img_x) + " " + str(sh_img_y))

            if(sh_img_x<=0):
                sh_img_x=0
            elif(sh_img_x>=1160):
                sh_img_x=1160
            elif(sh_img_y<=8):
                sh_img_y=8
            elif(sh_img_y>=870):
                sh_img_y=870


            pygame.draw.line(self.screen,(0,0,0),[lines['l1'][0],lines['l1'][1]],[lines['l1'][2],lines['l1'][3]],5)
            lines['l1'][0]+=lines['l1'][4]
            lines['l1'][2]+=lines['l1'][5]
            if(lines['l1'][2]==1200):
               lines['l1'][4]=-1
               lines['l1'][5]=-1
            if(lines['l1'][0]==0):
               lines['l1'][4]=1
               lines['l1'][5]=1

            pygame.draw.line(self.screen,(0,0,0),[lines['l2'][0],lines['l2'][1]],[lines['l2'][2],lines['l2'][3]],5)
            pygame.draw.line(self.screen,(0,0,0),[lines['l3'][0],lines['l3'][1]],[lines['l3'][2],lines['l2'][3]],5)
            lines['l2'][0]+=lines['l2'][4]
            lines['l2'][2]+=lines['l2'][5]
            lines['l3'][0]+=lines['l3'][4]
            lines['l3'][2]+=lines['l3'][5]
            if(lines['l3'][2]==1200):
                lines['l2'][4]=lines['l2'][5]=lines['l3'][4]=lines['l3'][5]=-1
            if(lines['l2'][0]==0):
                lines['l2'][4]=lines['l2'][5]=lines['l3'][4]=lines['l3'][5]=1
            
            pygame.draw.line(self.screen,(0,0,0),[lines['l4'][0],lines['l4'][1]],[lines['l4'][2],lines['l4'][3]],5)
            pygame.draw.line(self.screen,(0,0,0),[lines['l5'][0],lines['l5'][1]],[lines['l5'][2],lines['l5'][3]],5)
            pygame.draw.line(self.screen,(0,0,0),[lines['l6'][0],lines['l6'][1]],[lines['l6'][2],lines['l6'][3]],5)
            lines['l4'][0]+=lines['l4'][4]
            lines['l4'][2]+=lines['l4'][5]
            lines['l5'][0]+=lines['l5'][4]
            lines['l5'][2]+=lines['l5'][5]
            lines['l6'][0]+=lines['l6'][4]
            lines['l6'][2]+=lines['l6'][5]
            if(lines['l6'][2]==1200):
                lines['l5'][4]=lines['l5'][5]=lines['l4'][4]=lines['l4'][5]=lines['l6'][4]=lines['l6'][5]=-1
            if(lines['l4'][0]==0):
                lines['l5'][4]=lines['l5'][5]=lines['l4'][4]=lines['l4'][5]=lines['l6'][4]=lines['l6'][5]=1


            pygame.draw.line(self.screen,(0,0,0),[lines['p1'][0],lines['p1'][1]],[lines['p1'][2],lines['p1'][3]],5)
            lines['p1'][0]+=lines['p1'][4]
            lines['p1'][2]+=lines['p1'][5]
            if(lines['p1'][2]==1200):
               lines['p1'][4]=-1
               lines['p1'][5]=-1
            if(lines['p1'][0]==0):
               lines['p1'][4]=1
               lines['p1'][5]=1

            pygame.draw.line(self.screen,(0,0,0),[lines['p2'][0],lines['p2'][1]],[lines['p2'][2],lines['p2'][3]],5)
            pygame.draw.line(self.screen,(0,0,0),[lines['p3'][0],lines['p3'][1]],[lines['p3'][2],lines['p2'][3]],5)
            lines['p2'][0]+=lines['p2'][4]
            lines['p2'][2]+=lines['p2'][5]
            lines['p3'][0]+=lines['p3'][4]
            lines['p3'][2]+=lines['p3'][5]
            if(lines['p3'][2]==1200):
                lines['p2'][4]=lines['p2'][5]=lines['p3'][4]=lines['p3'][5]=-1
            if(lines['p2'][0]==0):
                lines['p2'][4]=lines['p2'][5]=lines['p3'][4]=lines['p3'][5]=1


            pygame.draw.line(self.screen,(0,0,0),[lines['p4'][0],lines['p4'][1]],[lines['p4'][2],lines['p4'][3]],5)
            pygame.draw.line(self.screen,(0,0,0),[lines['p5'][0],lines['p5'][1]],[lines['p5'][2],lines['p5'][3]],5)
            pygame.draw.line(self.screen,(0,0,0),[lines['p6'][0],lines['p6'][1]],[lines['p6'][2],lines['p6'][3]],5)
            lines['p4'][0]+=lines['p4'][4]
            lines['p4'][2]+=lines['p4'][5]
            lines['p5'][0]+=lines['p5'][4]
            lines['p5'][2]+=lines['p5'][5]
            lines['p6'][0]+=lines['p6'][4]
            lines['p6'][2]+=lines['p6'][5]
            if(lines['p6'][2]==1200):
                lines['p5'][4]=lines['p5'][5]=lines['p4'][4]=lines['p4'][5]=lines['p6'][4]=lines['p6'][5]=-1
            if(lines['p4'][0]==0):
                lines['p5'][4]=lines['p5'][5]=lines['p4'][4]=lines['p4'][5]=lines['p6'][4]=lines['p6'][5]=1

    
            
    
            pygame.display.update()


if __name__=="__main__":
    sh=super_hero()
    sh.run_sh()
        

