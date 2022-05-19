#Igrica-platform game
import pygame
import random
from tkinter import *
import time
from settings import *
from sprites import *
from pitanja import *
from os import path


class Game:
    def __init__(self):
        #initialize game
        global brojac1
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("pozadina.wav")
        self.screen=pygame.display.set_mode((sirina,visina),pygame.FULLSCREEN)
        self.last_update=0
        self.last_update1=0
        self.last_update3=0
        pygame.display.set_caption(ime)
        self.clock=pygame.time.Clock()
        all_sprites=pygame.sprite.Group()
        self.font_name=pygame.font.match_font(FONT_NAME)
        self.running=True
        self.mbrojac=1
        self.borba=False
        self.lives=3

    def draw_text(self,text,size,color,x,y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(text,True,color)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.screen.blit(text_surface,text_rect)
    def draw_text1(self,text,size,color,x,y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(text,True,color)
        text_rect=text_surface.get_rect()
        text_rect.topright=(x,y)
        self.screen.blit(text_surface,text_rect)
    def draw_text2(self,text,size,color,x,y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(text,True,color)
        text_rect=text_surface.get_rect()
        text_rect.topleft=(x,y)
        self.screen.blit(text_surface,text_rect)

    
    def new(self):
        #start new game
        self.all_sprites=pygame.sprite.Group()
        self.mobs=pygame.sprite.Group()
        self.srcad=pygame.sprite.Group()
        self.srce1=Srce1(self)
        self.srce2=Srce2(self)
        self.srce3=Srce3(self)
        self.srcad.add(self.srce1)
        self.srcad.add(self.srce2)
        self.srcad.add(self.srce3)
        self.igrac=pygame.sprite.Group()
        self.vratas1=pygame.sprite.Group()
        self.vratas2=pygame.sprite.Group()
        self.vratas3=pygame.sprite.Group()
        self.mbullets=pygame.sprite.Group()
        self.zmaj=Zmaj(self)
        self.player=Player(self)
        self.vrata1=Vrata1()
        self.vrata2=Vrata2()
        self.vrata3=Vrata3()
        self.player_health=Player_health(self)
        self.all_sprites.add(self.vrata3)
        self.all_sprites.add(self.vrata2)
        self.all_sprites.add(self.vrata1)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.zmaj)
        self.all_sprites.add(self.player_health)
        self.igrac.add(self.player_health)
        self.vratas3.add(self.vrata3)
        self.vratas2.add(self.vrata2)
        self.vratas1.add(self.vrata1)
        self.mobovi=[]
        self.bullets=pygame.sprite.Group()
        self.igrac.add(self.zmaj)
        self.igrac.add(self.player)
        self.pucanj=pygame.mixer.Sound("pucanj.wav")
        self.udarac=pygame.mixer.Sound("udarac.wav")
        self.lvlup=pygame.mixer.Sound("lvl up.wav")
        self.tocno=pygame.mixer.Sound("tocno.wav")
        self.run()
    
    def run(self):
        self.playing=True
        pygame.mixer.music.play(-1)
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #game loop-update
        global brojac1
        self.all_sprites.update()
        self.srcad.update()
        hits_vrata1=pygame.sprite.spritecollide(self.player,self.vratas1,False)
        hits_vrata2=pygame.sprite.spritecollide(self.player,self.vratas2,False)
        hits_vrata3=pygame.sprite.spritecollide(self.player,self.vratas3,False)
        if odgovori[(lista[brojac1])]=="A":
            if hits_vrata3:
                for i in range(self.mbrojac):
                    self.mob=Mob(self)
                    self.mobs.add(self.mob)
                self.tocno.play()
                self.screen.fill(black)
                self.draw_text("FIGHT!",50,white,sirina/2,visina/2)
                pygame.display.update()
                time.sleep(1)
                self.run1()
            elif hits_vrata1 or hits_vrata2:
                pygame.mixer.music.load("krivo.wav")
                pygame.mixer.music.play(-1)
                self.screen.fill(black)
                self.draw_text("Krivi odgovor, imate jos {0} pokušaja.".format(self.lives-1),50,white,sirina/2,visina/2)
                pygame.display.update()
                time.sleep(2)
                self.player.nazad()
                self.player_health.nazad()
                self.zmaj.nazad()
                self.srce1.nazad()
                self.srce2.nazad()
                self.srce3.nazad()
                if self.lives<=0:
                    self.running=False
                else:
                    if self.lives==3:
                        self.srce3.ubit()
                    elif self.lives==2:
                        self.srce2.ubit()
                    elif self.lives==1:
                        self.srce1.ubit()
                    self.lives-=1
        elif odgovori[(lista[brojac1])]=="B":
            if hits_vrata2:
                for i in range(self.mbrojac):
                    self.mob=Mob(self)
                    self.mobs.add(self.mob)
                self.tocno.play()
                self.screen.fill(black)
                self.draw_text("FIGHT!",50,white,sirina/2,visina/2)
                pygame.display.update()
                
                time.sleep(1)
                self.run1()
            elif hits_vrata1 or hits_vrata3:
                pygame.mixer.music.load("krivo.wav")
                pygame.mixer.music.play(-1)
                self.screen.fill(black)
                self.draw_text("Krivi odgovor, imate jos {0} pokušaja.".format(self.lives-1),50,white,sirina/2,visina/2)
                pygame.display.update()
                time.sleep(2)
                self.player.nazad()
                self.player_health.nazad()
                self.zmaj.nazad()
                self.srce1.nazad()
                self.srce2.nazad()
                self.srce3.nazad()
                if self.lives<=0:
                    self.playing=False
                else:
                    if self.lives==3:
                        self.srce3.ubit()
                    elif self.lives==2:
                        self.srce2.ubit()
                    elif self.lives==1:
                        self.srce1.ubit()
                    self.lives-=1

                    
        elif odgovori[(lista[brojac1])]=="C":
            if hits_vrata1:
                for i in range(self.mbrojac):
                    self.mob=Mob(self)
                    self.mobs.add(self.mob)
                self.tocno.play()
                self.screen.fill(black)
                self.draw_text("FIGHT!",50,white,sirina/2,visina/2)
                pygame.display.update()
                time.sleep(1)
                self.run1()
            elif hits_vrata2 or hits_vrata3:
                pygame.mixer.music.load("krivo.wav")
                pygame.mixer.music.play(-1)
                self.screen.fill(black)
                self.draw_text("Krivi odgovor, imate jos {0} pokušaja.".format(self.lives-1),50,white,sirina/2,visina/2)
                pygame.display.update()
                time.sleep(2)
                self.player.nazad()
                self.player_health.nazad()
                self.zmaj.nazad()
                self.srce1.nazad()
                self.srce2.nazad()
                self.srce3.nazad()
                if self.lives<=0:
                    self.playing=False
                else:
                    if self.lives==3:
                        self.srce3.ubit()
                    elif self.lives==2:
                        self.srce2.ubit()
                    elif self.lives==1:
                        self.srce1.ubit()
                    self.lives-=1


                
    def events(self):
        #game loop-events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.playing:
                    self.playing=False
                    self.running=False
        tipke=pygame.key.get_pressed()
        if tipke[pygame.K_ESCAPE]:
            self.playing=False
            self.running=False
        if self.lives<=0:
            self.playing=False

    
    def draw(self):
        #game loop-draw
        global brojac1
        self.screen.blit(pozadina, [0,0])
        self.all_sprites.draw(self.screen)
        self.draw_text(pitanja[(lista[brojac1])],30,black,sirina/2,visina-50)
        self.draw_text2(a[(lista[brojac1])],30,black,0,55)
        self.draw_text(b[(lista[brojac1])],30,black,sirina/2,55)
        self.draw_text1(c[(lista[brojac1])],30,black,sirina,55)
        tekst=font.render("A",True,black)
        self.screen.blit(tekst,(75,5))
        tekst1=font.render("B",True,black)
        self.screen.blit(tekst1,(sirina/2,5))
        tekst2=font.render("C",True,black)
        self.screen.blit(tekst2,(sirina-75,5))
        self.srcad.draw(self.screen)
        #flip
        pygame.display.flip()
    
    def show_start_screen(self):
        #game start screen
        self.screen.blit(start, [0,0])
        self.draw_text(ime,100,white,sirina/2,0)
        self.draw_text("Strelice su za kretanje, lijevi klik miša za pucanje",50,green,sirina/2,200)
        self.draw_text("Da bi otežali igricu možete pucati samo u osam smjerova",50,green,sirina/2,250)
        self.draw_text("Igrica se igra tako da tocno odgovorite na pitanje i ubijete protivnike u areni",50,green,sirina/2,300)
        self.draw_text("Ukoliko krivo odgovorite na pitanje ili umrete izgubili ste 1 život (od 3)!",50,green,sirina/2,350)
        self.draw_text("Ukoliko želiš izaći tijekom igre stisni ESC",50,green,sirina/2,450)
        self.draw_text("Stisni bilo koju tipku za početak",50,green,sirina/2,400)
        pygame.display.flip()
        self.cekanje()
    def show_go_screen(self):
        #game over screen
        if not self.running:
            return
        self.screen.blit(kraj,[0,0])
        self.draw_text("Pritisnite p za ponovni pokušaj a ESC za prekid.",50,white,sirina/2,visina/2+50)
        self.draw_text("Rezultat:{0}/30".format(brojac1),50,white,sirina/2,visina/2-50)
        if brojac1>=27:
            self.draw_text("Ocjena: odličan(5)",50,white,sirina/2,visina/2+100)
        elif brojac1>=22:
            self.draw_text("Ocjena: vrlo dobar(4)",50,white,sirina/2,visina/2+100)
        elif brojac1>=18:
            self.draw_text("Ocjena: dobar(3)",50,white,sirina/2,visina/2+100)
        elif brojac1>=15:
            self.draw_text("Ocjena: dovoljan(2)",50,white,sirina/2,visina/2+100)
        elif brojac1<15:
            self.draw_text("Ocjena: nedovoljan(1)",50,white,sirina/2,visina/2+100)
        pygame.display.update()
        self.cekanje1()
        
                
    def cekanje(self):
        waiting=True
        while waiting:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    waiting=False
                    self.running=False
                if event.type==pygame.KEYUP:
                    waiting=False
    def cekanje1(self):
        global brojac1
        waiting=True
        while waiting:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    waiting=False
                    self.running=False
            tipke=pygame.key.get_pressed()
            if tipke[pygame.K_ESCAPE]:
                waiting=False
                self.running=False
                self.playing=False
                self.borba=False
                self.alive=False
            elif tipke[pygame.K_p]:
                waiting=False
                self.playing=True
                self.running=True
                brojac1=0
                self.mbrojac=1
                self.borba=False
                self.lives=3
                shuffle(lista)
                pygame.sprite.Sprite.kill(self.srce1)
                pygame.sprite.Sprite.kill(self.srce2)
                pygame.sprite.Sprite.kill(self.srce3)
                self.srcad.add(self.srce1)
                self.srcad.add(self.srce2)
                self.srcad.add(self.srce3)
                pygame.mixer.music.load("pozadina.wav")
                pygame.mixer.music.play()
    def cekanje2(self):
        global brojac1
        waiting=True
        while waiting:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    waiting=False
                    self.running=False
            tipke=pygame.key.get_pressed()
            if tipke[pygame.K_ESCAPE]:
                self.running==False
                self.playing=False
                self.borba=False
                self.waiting=False
                pygame.quit()
            elif tipke[pygame.K_p]:
                waiting=False
                self.playing=True
                self.running=True
                brojac1=0
                self.mbrojac=1
                self.borba=False
                self.lives=3
                shuffle(lista)
                pygame.sprite.Sprite.kill(self.srce1)
                pygame.sprite.Sprite.kill(self.srce2)
                pygame.sprite.Sprite.kill(self.srce3)
                self.srcad.add(self.srce1)
                self.srcad.add(self.srce2)
                self.srcad.add(self.srce3)
                pygame.mixer.music.load("pozadina.wav")
                pygame.mixer.music.play()
                                  
    def winscreen(self):
        self.screen.blit(win,[0,0])
        self.draw_text("Pritisnite p za ponovni pokušaj a ESC za prekid.",50,green,sirina/2,visina/2+50)
        self.draw_text("Rezultat:{0}/30".format(brojac1),50,green,sirina/2,visina/2-50)
        self.draw_text("Ocjena: odličan (5)",50,green,sirina/2,visina/2+150)
        pygame.display.update()
        self.cekanje2()
    def run1(self):
        #new battle
        self.borba=True
        pygame.mixer.music.load("borba.wav")
        pygame.mixer.music.play(-1)
        while self.borba:
            self.clock.tick(FPS)
            self.events1()
            self.update1()
            self.draw1()
        
    def update1(self):
        #update battle loop
        self.bullets.update()
        self.igrac.update()
        self.mobs.update()
        self.mbullets.update()
        self.srcad.update()
    def events1(self):
        #battle loop-events
        global brojac1
        global player_health
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.borba:
                    self.borba=False
                self.playing=False
                self.running=False
        tipke=pygame.key.get_pressed()
        if tipke[pygame.K_ESCAPE]:
            self.playing=False
            self.running=False
            self.borba=False
        if self.lives<=0:
            self.playing=False
        mouse1=pygame.mouse.get_pressed()
        if mouse1[0]==1:
            now=pygame.time.get_ticks()
            if now-self.last_update>250:
                self.last_update=now
                self.mouse=pygame.mouse.get_pos()                       
                self.zmaj.shoot()
        now1=pygame.time.get_ticks()
        if now1-self.last_update1>500:
            self.last_update1=now1
            a=randint(1,4)
            for h in self.mobs:
                h.shoot1(a)
        mshot=pygame.sprite.groupcollide(self.bullets,self.mobs,True,True)
        if len(self.mobs)==0:
            brojac1+=1
            self.all_sprites.update()
            self.igrac.update()
            for gt in self.mbullets:
                self.mbullets.remove(gt)
            for ih in self.bullets:
                self.bullets.remove(ih)
            self.borba=False
            if (brojac1+1)%3==0:
                self.mbrojac+=1
            player_health=100
            self.srce1.nazad()
            self.srce2.nazad()
            self.srce3.nazad()
            pygame.mixer.music.load("pozadina.wav")
            self.lvlup.play()
            self.screen.fill(black)
            self.draw_text("Uspjeli ste!",50,white,sirina/2,visina/2)
            if brojac1<30:
                self.draw_text("Sad ide level {0}".format(brojac1+1),50,white,sirina/2,visina/2+60)
            else:
                self.draw_text("POBJEDA!",50,white,sirina/2,visina/2+60)
            pygame.display.update()
            time.sleep(1)
            pygame.mixer.music.play(-1)
            if brojac1==30:
                self.winscreen()
        if self.lives<=0:
            self.playing=False
            
    def draw1(self):
        #battle loop-draw
        self.screen.blit(arena, [0,0])
        self.igrac.draw(self.screen)
        self.bullets.draw(self.screen)
        self.mobs.draw(self.screen)
        self.mbullets.draw(self.screen)
        self.srcad.draw(self.screen)
        #flip
        pygame.display.flip()

alive=True    
g=Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
pygame.quit()
    
