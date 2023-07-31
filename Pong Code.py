import pygame,sys

pygame.init()

green=(0,255,0)
white=(255,255,255)

display=pygame.display.set_mode((800,600))
icon=pygame.image.load("jigsaw.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Pong")

#ball
ballImg=pygame.image.load("ball.png")
ball_x=250
ball_y=150
move_ball_x=0.5
move_ball_y=0.5

#player1
barImg1=pygame.image.load("or.png")
bar_x1=50
bar_y1=300
move_bar_y1=0.4

#player2
barImg2=pygame.image.load("or.png")
bar_x2=700
bar_y2=300
move_bar_y2=0.4

score1=0
score2=0
font=pygame.font.Font("freesansbold.ttf",32)
text_x=250
text_y=10

def ball(x,y):
    display.blit(ballImg,(x,y))

def player1(x,y):
    display.blit(barImg1,(x,y))

def player2(x,y):
    display.blit(barImg2,(x,y))

def IsCollision(ball_x,ball_y,bar_y1,bar_y2,bar_x1,bar_x2):
    if ball_x+10==bar_x1+64 and ball_y+70>bar_y1 and ball_y<bar_y1+70:
        return True
    if ball_x+64+10==bar_x2 and ball_y+70>bar_y2 and ball_y<bar_y2+70:
        return True
    
def show_score(x,y):
    score=font.render("Player1:"+str(score1)+"  "+"Player2:"+str(score2),True,white)
    display.blit(score,(x,y))
    
running=True
while running:

    display.fill(green)
     
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                move_bar_y1=-0.5
            if event.key==pygame.K_s:
                move_bar_y1=0.5
            if event.key==pygame.K_UP:
                move_bar_y2=-0.5
            if event.key==pygame.K_DOWN:
                move_bar_y2=0.5

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                move_bar_y2=0
            if event.key==pygame.K_s or event.key==pygame.K_w:
                move_bar_y1=0

    bar_y1+=move_bar_y1
    if bar_y1<0:
        bar_y1=0
    elif bar_y1>600-64:
        bar_y1=600-64

    bar_y2+=move_bar_y2
    if bar_y2<0:
        bar_y2=0
    elif bar_y2>600-64:
        bar_y2=600-64

    ball_x+=move_ball_x
    if ball_x<0:
        move_ball_x=0.5
        score2+=1
    elif ball_x>800-64:
        move_ball_x=-0.5
        score1+=1

    ball_y+=move_ball_y
    if ball_y>600-64:
        move_ball_y=-0.5
    elif ball_y<0:
        move_ball_y=0.5

    collision=IsCollision(ball_x,ball_y,bar_y1,bar_y2,bar_x1,bar_x2)
    if collision:
        move_ball_x=-move_ball_x
        
    player1(bar_x1,bar_y1)
    player2(bar_x2,bar_y2)
    ball(ball_x,ball_y)
    show_score(text_x,text_y)
    pygame.display.update()

