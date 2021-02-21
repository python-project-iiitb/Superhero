import pygame
from classes import Line

class Line:
    def __init__(self,x1,y1,x2,y2,x1_ch,x2_ch):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x1_ch=x1_ch
        self.x2_ch=x2_ch
    def move_line(self):
        if(self.x2==1200):
            self.x1_ch=-1
            self.x2_ch=-1
        if(self.x1==0):
            self.x1_ch=1
            self.x2_ch=1
        self.x1+=self.x1_ch
        self.x2+=self.x2_ch
        return self.x1,self.x2    
        



class super_hero:
    def __init__(self):
        pygame.init()   #initialising pygame
        pygame.display.set_caption("SUPER HERO")

        #creating the screen
        self.screen=pygame.display.set_mode((1200,800))
        self.bg_color=(64,47,117)

        

    def run_sh(self):
        run=True
        x1=200
        y1=720
        x2=1000
        y2=720
        x1_ch=1
        x2_ch=1
        lines={
                'l1':[200,720,1000,720,1,1],
                'l2':[100,640,500,640,1,1],
                'l3':[600,640,1100,640,1,1],
                'l4':[100,560,350,560,1,1],
                'l5':[450,560,700,560,1,1],
                'l6':[800,560,1050,560,1,1],
                'p1':[200,80,1000,80,1,1],
                'p2':[100,160,500,160,1,1],
                'p3':[600,160,1100,160,1,1],
                'p4':[100,240,350,240,1,1],
                'p5':[450,240,700,240,1,1],
                'p6':[800,240,1050,240,1,1]
                } 

        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            self.screen.fill(self.bg_color)

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
        

