#sprite classes for game
import pygame
from random import *
from settings import *
import time
vrata=pygame.image.load("vrata1.png")
stoji1=pygame.image.load("stoji i gleda naprijed.png")
stoji2=pygame.image.load("stoji i gleda lijevo.png")
stoji3=pygame.image.load("stoji i gleda desno.png")
stoji4=pygame.image.load("stoji i gleda nazad.png")
lijevo1=pygame.image.load("seta i gleda lijevo.png")
lijevo2=pygame.image.load("seta i gleda lijevo druga noga.png")
desno1=pygame.image.load("seta i gleda desno.png")
desno2=pygame.image.load("seta i gleda desno druga noga.png")
gore1=pygame.image.load("seta i gleda naprijed.png")
gore2=pygame.image.load("seta i gleda naprijed druga noga.png")
nazad1=pygame.image.load("seta i gleda nazad.png")
nazad2=pygame.image.load("seta i gleda nazad druga noga.png")
zmaj_naprijed=pygame.image.load("zmaj naprijed.png")
zmaj_naprijed1=pygame.image.load("zmaj naprijed druga noga.png")
zmaj_nazad=pygame.image.load("zmaj nazad.png")
zmaj_nazad1=pygame.image.load("zmaj nazad druga noga.png")
zmaj_desno=pygame.image.load("zmaj desno.png")
zmaj_desno1=pygame.image.load("zmaj desno druga noga.png")
zmaj_lijevo=pygame.image.load("zmaj lijevo.png")
zmaj_lijevo1=pygame.image.load("zmaj lijevo druga noga.png")
protivnik_naprijed=pygame.image.load("protivnik naprijed.png")
protivnik_naprijed1=pygame.image.load("protivnik naprijed druga noga.png")
protivnik_nazad=pygame.image.load("protivnik nazad.png")
protivnik_nazad1=pygame.image.load("protivnik nazad druga noga.png")
protivnik_desno=pygame.image.load("protivnik desno.png")
protivnik_desno1=pygame.image.load("protivnik desno druga noga.png")
protivnik_lijevo=pygame.image.load("protivnik lijevo.png")
protivnik_lijevo1=pygame.image.load("protivnik lijevo druga noga.png")
protivnik_stoji1=pygame.image.load("protivnik stoji naprijed.png")
protivnik_stoji2=pygame.image.load("protivnik stoji nazad.png")
protivnik_stoji3=pygame.image.load("protivnik stoji desno.png")
protivnik_stoji4=pygame.image.load("protivnik stoji lijevo.png")
metak=pygame.image.load("metak.png")
protivnik_metak=pygame.image.load("protivnik metak.png")
srce=pygame.image.load("srce.png")
srce=pygame.transform.scale(srce,(20,33))
vec=pygame.math.Vector2
brojac=3
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        self.walking=False
        self.current_frame=0
        self.last_update=0
        self.image=stoji1
        self.rect=self.image.get_rect()
        self.rect.center=(sirina/2,visina/2)
        self.pos=vec(sirina/2,visina/2)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def update(self):
        global brojac
        self.animate()
        self.acc=vec(0,0)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x=-player_acc
            brojac=1
        if keys[pygame.K_RIGHT]:
            self.acc.x=player_acc
            brojac=2
        if keys[pygame.K_UP]:
            self.acc.y=-player_acc
            brojac=3
        if keys[pygame.K_DOWN]:
            self.acc.y=player_acc
            brojac=4
        

        #usporenje
        self.acc+=self.vel*player_friction
        #jednadzbe gibanja
        self.vel+=self.acc
        if abs(self.vel.x)<0.1:
            self.vel.x=0
        if abs(self.vel.y)<0.1:
            self.vel.y=0
        self.pos+=self.vel+0.5*self.acc
        #kraj mape
        if self.pos.x>sirina-93:
            self.pos.x=sirina-93
        if self.pos.x<15:
            self.pos.x=15
        if self.pos.y>visina-20:
            self.pos.y=visina-20
        if self.pos.y<20:
            self.pos.y=20
        if len(self.game.mobs)==0 and self.game.borba==True:
            self.pos=vec(sirina/2,visina/2)
        self.rect.center=self.pos
    def animate(self):
        global brojac
        now=pygame.time.get_ticks()
        if self.vel.x!=0 or self.vel.y!=0:
            self.walking=True
        else:
            self.walking=False
        #walk animation
        if self.walking:
            if now-self.last_update>400:
                self.last_update=now
                self.current_frame=(self.current_frame+1)%2
                bottom=self.rect.bottom
                if self.vel.x>0 and self.vel.x>self.vel.y:
                    if self.current_frame==0:
                        self.image=desno2
                    else:
                        self.image=desno1
                elif self.vel.x<0 and self.vel.x<self.vel.y:
                    if self.current_frame==0:
                        self.image=lijevo2
                    else:
                        self.image=lijevo1
                elif self.vel.y<0 and self.vel.y<self.vel.x:
                    if self.current_frame==0:
                        self.image=gore2
                    else:
                        self.image=gore1
                elif self.vel.y>0 and self.vel.y>self.vel.x:
                    if self.current_frame==0:
                        self.image=nazad2
                    else:
                        self.image=nazad1
                self.rect=self.image.get_rect()
                self.rect.bottom=bottom
        if self.vel.x==0 and self.vel.y==0:
            bottom=self.rect.bottom
            if brojac==1:
                self.image=stoji2
            elif brojac==2:
                self.image=stoji3
            elif brojac==3:
                self.image=stoji1
            else:
                self.image=stoji4
            self.rect=self.image.get_rect()
            self.rect.bottom=bottom
    def nazad(self):
        self.rect.center=(sirina/2,visina/2)
        self.pos=vec(sirina/2,visina/2)
class Srce1(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        self.image=srce
        self.pos=vec(sirina/2-28,visina/2-100)
        self.rect=self.image.get_rect()
        self.rect.center=(sirina/2-28,visina/2-100)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def update(self):
        global brojac
        self.acc=vec(0,0)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x=-player_acc
            brojac=1
        if keys[pygame.K_RIGHT]:
            self.acc.x=player_acc
            brojac=2
        if keys[pygame.K_UP]:
            self.acc.y=-player_acc
            brojac=3
        if keys[pygame.K_DOWN]:
            self.acc.y=player_acc
            brojac=4
        #usporenje
        self.acc+=self.vel*player_friction
        #jednadzbe gibanja
        self.vel+=self.acc
        if abs(self.vel.x)<0.1:
            self.vel.x=0
        if abs(self.vel.y)<0.1:
            self.vel.y=0
        self.pos+=self.vel+0.5*self.acc
        #kraj mape
        if self.pos.x>sirina-126:
            self.pos.x=sirina-126
        if self.pos.x<-16:
            self.pos.x=-16
        if self.pos.y>visina-125:
            self.pos.y=visina-125
        if self.pos.y<-75:
            self.pos.y=-75
        if len(self.game.mobs)==0 and self.game.borba==True:
            self.pos=vec(sirina/2-28,visina/2-100)
        self.rect.center=self.pos
        if not self.game.srce1:
            self.kill()
        if not self.game.playing:
            self.pos=vec(sirina/2-28,visina/2-100)
    def ubit(self):
        self.kill()
    def nazad(self):
        self.pos=vec(sirina/2-28,visina/2-100)
        self.rect.center=(sirina/2-28,visina/2-100)
class Srce2(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        self.image=srce
        self.pos=vec(sirina/2+5,visina/2-100)
        self.rect=self.image.get_rect()
        self.rect.center=(sirina/2+5,visina/2-100)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def update(self):
        global brojac
        self.acc=vec(0,0)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x=-player_acc
            brojac=1
        if keys[pygame.K_RIGHT]:
            self.acc.x=player_acc
            brojac=2
        if keys[pygame.K_UP]:
            self.acc.y=-player_acc
            brojac=3
        if keys[pygame.K_DOWN]:
            self.acc.y=player_acc
            brojac=4
        #usporenje
        self.acc+=self.vel*player_friction
        #jednadzbe gibanja
        self.vel+=self.acc
        if abs(self.vel.x)<0.1:
            self.vel.x=0
        if abs(self.vel.y)<0.1:
            self.vel.y=0
        self.pos+=self.vel+0.5*self.acc
        #kraj mape
        if self.pos.x>sirina-93:
            self.pos.x=sirina-93
        if self.pos.x<15:
            self.pos.x=15
        if self.pos.y>visina-125:
            self.pos.y=visina-125
        if self.pos.y<-75:
            self.pos.y=-75
        if len(self.game.mobs)==0 and self.game.borba==True:
            self.pos=vec(sirina/2+5,visina/2-100)
        self.rect.center=self.pos
        if not self.game.srce2:
            self.kill()
        if not self.game.playing:
            self.pos=vec(sirina/2+5,visina/2-100)
    def ubit(self):
        self.kill()
    def nazad(self):
       self.pos=vec(sirina/2+5,visina/2-100)
       self.rect.center=(sirina/2+5,visina/2-100)
class Srce3(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        self.image=srce
        self.pos=vec(sirina/2+37,visina/2-100)
        self.rect=self.image.get_rect()
        self.rect.center=(sirina/2+37,visina/2-100)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def update(self):
        global brojac
        self.acc=vec(0,0)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x=-player_acc
            brojac=1
        if keys[pygame.K_RIGHT]:
            self.acc.x=player_acc
            brojac=2
        if keys[pygame.K_UP]:
            self.acc.y=-player_acc
            brojac=3
        if keys[pygame.K_DOWN]:
            self.acc.y=player_acc
            brojac=4
        #usporenje
        self.acc+=self.vel*player_friction
        #jednadzbe gibanja
        self.vel+=self.acc
        if abs(self.vel.x)<0.1:
            self.vel.x=0
        if abs(self.vel.y)<0.1:
            self.vel.y=0
        self.pos+=self.vel+0.5*self.acc
        #kraj mape
        if self.pos.x>sirina-60:
            self.pos.x=sirina-60
        if self.pos.x<48:
            self.pos.x=48
        if self.pos.y>visina-125:
            self.pos.y=visina-125
        if self.pos.y<-75:
            self.pos.y=-75
        if len(self.game.mobs)==0 and self.game.borba==True:
            self.pos=vec(sirina/2+37,visina/2-100)
        self.rect.center=self.pos
        if not self.game.srce3:
            self.kill()
        if not self.game.playing:
            self.pos=vec(sirina/2+37,visina/2-100)
    def ubit(self):
        self.kill()
    def nazad(self):
        self.pos=vec(sirina/2+37,visina/2-100)
        self.rect.center=(sirina/2+37,visina/2-100)
class Player_health(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game=game
        pygame.sprite.Sprite.__init__(self)
        self.last_update2=0
        self.pos=vec(sirina/2,visina/2-75)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def update(self):
        global player_health
        if player_health>75:
            self.player_health_color=green
        elif player_health>50:
            self.player_health_color=yellow
        else:
            self.player_health_color=red
        self.image=pygame.Surface((player_health,15))
        self.image.fill(self.player_health_color)
        self.rect=self.image.get_rect()
        self.rect.center=(sirina/2,visina/2-75)
        now2=pygame.time.get_ticks()
        if now2-self.last_update2>75:
            self.last_update2=now2
            self.col()
        self.acc=vec(0,0)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x=-player_acc
        if keys[pygame.K_RIGHT]:
            self.acc.x=player_acc
        if keys[pygame.K_UP]:
            self.acc.y=-player_acc
        if keys[pygame.K_DOWN]:
            self.acc.y=player_acc

        #usporenje
        self.acc+=self.vel*player_friction
        #jednadzbe gibanja
        self.vel+=self.acc
        if abs(self.vel.x)<0.1:
            self.vel.x=0
        if abs(self.vel.y)<0.1:
            self.vel.y=0
        self.pos+=self.vel+0.5*self.acc
        #kraj mape
        if self.pos.x>sirina-93:
            self.pos.x=sirina-93
        if self.pos.x<15:
            self.pos.x=15
        if self.pos.y>visina-95:
            self.pos.y=visina-95
        if self.pos.y<-55:
            self.pos.y=-55
        if len(self.game.mobs)==0 and self.game.borba==True:
            self.pos=vec(sirina/2,visina/2-75)
        if len(self.game.mobs)==0:
            player_health=100
        self.rect.center=self.pos
    def col(self):
        global player_health
        shot=pygame.sprite.groupcollide(self.game.igrac,self.game.mbullets,False,True)
        if shot:
            player_health-=10
            self.game.udarac.play()
        if player_health<=0:
            if self.game.lives<=0:
                self.running=False
            else:
                self.game.borba=False
                pygame.mixer.music.load("pozadina.wav")
                pygame.mixer.music.play(-1)
                player_health=100
                if self.game.lives==3:
                    self.game.srcad.remove(self.game.srce3)
                elif self.game.lives==2:
                    self.game.srcad.remove(self.game.srce2)
                elif self.game.lives==1:
                    self.game.srcad.remove(self.game.srce1)
                self.game.lives-=1
                self.game.screen.fill(black)
                self.game.draw_text("Umrli ste! Imate jos {0} pokušaja.".format(self.game.lives),50,white,sirina/2,visina/2)
                pygame.display.flip()
                for gh in self.game.mbullets:
                    self.game.mbullets.remove(gh)
                for tt in self.game.mobs:
                    self.game.mobs.remove(tt)
                for gg in self.game.bullets:
                    self.game.bullets.remove(gg)
                time.sleep(1)
    def nazad(self):
        self.pos=vec(sirina/2,visina/2-75)

class Vrata1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image=vrata
            self.rect=self.image.get_rect()
            self.rect.center=(sirina-75,200)
class Vrata2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image=vrata
            self.rect=self.image.get_rect()
            self.rect.center=(sirina/2,200)
class Vrata3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image=vrata
            self.rect=self.image.get_rect()
            self.rect.center=(75,200)
class Zmaj(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game=game
        pygame.sprite.Sprite.__init__(self)
        self.walking=False
        self.current_frame=0
        self.last_update=0
        self.image=zmaj_naprijed
        self.rect=self.image.get_rect()
        self.rect.center=(sirina/2+50,visina/2)
        self.pos=vec(sirina/2+78,visina/2+27)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def update(self):
        global brojac
        self.animate()
        self.acc=vec(0,0)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x=-player_acc
            brojac=1
        if keys[pygame.K_RIGHT]:
            self.acc.x=player_acc
            brojac=2
        if keys[pygame.K_UP]:
            self.acc.y=-player_acc
            brojac=3
        if keys[pygame.K_DOWN]:
            self.acc.y=player_acc
            brojac=4
        
        #usporenje
        self.acc+=self.vel*player_friction
        #jednadzbe gibanja
        self.vel+=self.acc
        if abs(self.vel.x)<0.1:
            self.vel.x=0
        if abs(self.vel.y)<0.1:
            self.vel.y=0
        self.pos+=self.vel+0.5*self.acc
        #kraj mape
        if self.pos.x>sirina-15:
            self.pos.x=sirina-15
        if self.pos.x<93:
            self.pos.x=93
        if self.pos.y>visina:
            self.pos.y=visina
        if self.pos.y<50:
            self.pos.y=50
        if len(self.game.mobs)==0 and self.game.borba==True:
            self.pos=vec(sirina/2+78,visina/2+27)
        self.rect.center=self.pos
    def animate(self):
        global brojac
        now=pygame.time.get_ticks()
        if self.vel.x!=0 or self.vel.y!=0:
            self.walking=True
        else:
            self.walking=False
        #walk animation
        if self.walking:
            if now-self.last_update>400:
                self.last_update=now
                self.current_frame=(self.current_frame+1)%2
                bottom=self.rect.bottom
                if self.vel.x>0 and self.vel.x>self.vel.y:
                    if self.current_frame==0:
                        self.image=zmaj_desno1
                    else:
                        self.image=zmaj_desno
                elif self.vel.x<0 and self.vel.x<self.vel.y:
                    if self.current_frame==0:
                        self.image=zmaj_lijevo1
                    else:
                        self.image=zmaj_lijevo
                elif self.vel.y<0 and self.vel.y<self.vel.x:
                    if self.current_frame==0:
                        self.image=zmaj_naprijed1
                    else:
                        self.image=zmaj_naprijed
                elif self.vel.y>0 and self.vel.y>self.vel.x:
                    if self.current_frame==0:
                        self.image=zmaj_nazad1
                    else:
                        self.image=zmaj_nazad
                self.rect=self.image.get_rect()
                self.rect.bottom=bottom
        if self.vel.x==0 and self.vel.y==0:
            bottom=self.rect.bottom
            if brojac==1:
                self.image=zmaj_lijevo
            elif brojac==2:
                self.image=zmaj_desno
            elif brojac==3:
                self.image=zmaj_naprijed
            else:
                self.image=zmaj_nazad
            self.rect=self.image.get_rect()
            self.rect.bottom=bottom

    def shoot(self):
        self.game.pucanj.play()
        bullet=Bullets(self.pos.x,self.pos.y,self.game.mouse)
        self.game.bullets.add(bullet)
    def nazad(self):
        self.rect.center=(sirina/2+50,visina/2)
        self.pos=vec(sirina/2+78,visina/2+27)
class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y,mouse):
        pygame.sprite.Sprite.__init__(self)
        self.image=metak
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.pos=vec(x,y)
        self.mouse = mouse
        self.x=x
        self.y=y
    def update(self):
        if self.x-50<self.mouse[0]<self.x+50:
            brzina=0
        elif self.mouse[0]!=0 and abs(self.mouse[0])>20 and abs(self.mouse[0])<100:
            brzina=self.mouse[0]
        elif self.mouse[0]==0:
            brzina=0
        else:
            brzina=30
        if self.y-50<self.mouse[1]<self.y+50:
            brzina_y=0
        elif self.mouse[1]!=0 and abs(self.mouse[1])>20 and abs(self.mouse[1])<100:
            brzina_y=self.mouse[1]
        elif self.mouse[1]==0:
            brzina_y=0
        else:
            brzina_y=30
        if self.x-50<self.mouse[0]<self.x+50 and self.y-50<self.mouse[1]<self.y+50:
            self.kill()
        if self.mouse[0]>self.x:
            self.pos.x+=brzina
        elif self.mouse[0]<self.x:
            self.pos.x-=brzina
        else:
            self.pos.x+=0
        if self.mouse[1]>self.y:
            self.pos.y+=brzina_y
        elif self.mouse[1]<self.y:
            self.pos.y-=brzina_y
        else:
            self.pos.y+=0
        #kraj mape
        if self.pos.x>sirina:
            self.kill()
        if self.pos.x<0:
            self.kill()
        if self.pos.y>visina:
            self.kill()
        if self.pos.y<0:
            self.kill()
        self.rect.center=self.pos
        if brzina_y==0 and brzina==0:
            self.kill()
class Mob(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game=game
        pygame.sprite.Sprite.__init__(self)
        self.walking=False
        self.current_frame=0
        self.last_update=0
        self.last_update1=0
        self.image=protivnik_stoji1
        self.rect=self.image.get_rect()
        f=randint(0,sirina)
        g=randint(0,visina)
        self.rect.center=(f,g)
        self.pos=vec(f,g)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def update(self):
        global brojac
        self.animate()
        self.acc=vec(0,0)
        now1=pygame.time.get_ticks()
        if now1-self.last_update1>700:
            self.last_update1=now1
            self.vel.x=randint(-20,20)
            self.vel.y=randint(-20,20)
        #jednadzbe gibanja
        self.pos+=self.vel
        #kraj mape
        if self.pos.x>sirina:
            self.pos.x=sirina
        if self.pos.x<0:
            self.pos.x=0
        if self.pos.y>visina:
            self.pos.y=visina
        if self.pos.y<0:
            self.pos.y=0
        self.rect.center=self.pos
    def animate(self):
        global brojac
        now=pygame.time.get_ticks()
        if self.vel.x!=0 or self.vel.y!=0:
            self.walking=True
        else:
            self.walking=False
        #walk animation
        if self.walking:
            if now-self.last_update>400:
                self.last_update=now
                self.current_frame=(self.current_frame+1)%2
                bottom=self.rect.bottom
                if self.vel.x>0 and self.vel.x>self.vel.y:
                    if self.current_frame==0:
                        self.image=protivnik_desno1
                    else:
                        self.image=protivnik_desno
                elif self.vel.x<0 and self.vel.x<self.vel.y:
                    if self.current_frame==0:
                        self.image=protivnik_lijevo1
                    else:
                        self.image=protivnik_lijevo
                elif self.vel.y<0 and self.vel.y<self.vel.x:
                    if self.current_frame==0:
                        self.image=protivnik_naprijed1
                    else:
                        self.image=protivnik_naprijed
                elif self.vel.y>0 and self.vel.y>self.vel.x:
                    if self.current_frame==0:
                        self.image=protivnik_nazad1
                    else:
                        self.image=protivnik_nazad
                self.rect=self.image.get_rect()
                self.rect.bottom=bottom
        if self.vel.x<0.1 and self.vel.y<0.1:
            bottom=self.rect.bottom
            if brojac==1:
                self.image=protivnik_stoji2
            elif brojac==2:
                self.image=protivnik_stoji3
            elif brojac==3:
                self.image=protivnik_stoji1
            else:
                self.image=protivnik_stoji4
            self.rect=self.image.get_rect()
            self.rect.bottom=bottom
    def shoot1(self,a):
        mbullet=mshoot(self.pos.x,self.pos.y,a)
        self.game.mbullets.add(mbullet)
class mshoot(pygame.sprite.Sprite):
    def __init__(self,x,y,a):
        pygame.sprite.Sprite.__init__(self)
        self.a=a
        self.image=protivnik_metak
        self.rect=self.image.get_rect()
        self.pos=vec(x,y)
        self.rect.center=(x,y)
        self.vel=vec(0,0)
    def update(self):
        if self.a==1:
            brzina_x=20
            brzina_y=0
        elif self.a==2:
            brzina_x=-20
            brzina_y=0
        elif self.a==3:
            brzina_y=20
            brzina_x=0
        else:
            brzina_y=-20
            brzina_x=0
        self.pos.x+=brzina_x
        self.pos.y+=brzina_y
        #kraj mape
        self.rect.center=self.pos
        if self.pos.x>sirina+100:
            self.kill()
        if self.pos.x<-100:
            self.kill()
        if self.pos.y>visina+100:
            self.kill()
        if self.pos.y<-100:
            self.kill()

                
            
            
            
        
        
    

        
