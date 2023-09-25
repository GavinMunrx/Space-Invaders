# Gavin Munro
# a coded version of space invaders, use left and right arrow keys to
# move and space to shoot.

startmenu = True # variable for start menu
while startmenu == True: # conditional statement for start menu 
    UserInput = str(input('Start-S / Help-H / End-E -->')) # displayed menu bar asking the user which function one wishes to preform
    if UserInput == 'H': # if statement for when user inputs the help function 
        print('SPACE INVADERS, USE LEFT AND RIGHT ARROW KEYS TO MOVE, SPACE +\
              BAR TO SHOOT, AND MOST IMPORTANTLY... SURVIVE!') # Explaining what the program does
    elif UserInput == 'S': # if statement for when user inputs the start function 
        startmenu=False # Statament to become removed from the loop
    elif UserInput == 'E': # if statement for when user inputs the quit function 
        startmenu=False # Statament to become removed from the loop
        quit() # quitting the program
    else:
        print("Invalid Response")
        startmenu == True# statement for if user inputs an invalid letter

import turtle
import os
import math
import random

# setting background image
background = turtle.Screen()
background.bgcolor('black')
background.title('SPACE INVADERS')
background.bgpic("bg5.gif")

#Register Shape
turtle.register_shape("alien1-50px.gif")
turtle.register_shape("player1.gif")
turtle.register_shape("rocket.gif")

# Create outer border
border = turtle.Turtle()
border.speed(0)
border.color('white')
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

# Setting Score
score = 0

# Displaying score
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color('White')
scoreboard.penup()
scoreboard.setposition(-290, 275)
scorestr = 'Score:  %s' %score
scoreboard.write(scorestr, False, align='left', font=('Arial', 18, 'normal'))
scoreboard.hideturtle()

# creating player
player = turtle.Turtle()
player.shape("player1.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

speed_player = 30
#number of aliens
number_of_aliens = 8
# create empty list
aliens = []

#Add aliens to list
for i in range(number_of_aliens):
    # Enemy Alien
    aliens.append(turtle.Turtle())

for alien in aliens:
    alien.shape("alien1-50px.gif")
    alien.penup()
    alien.speed(0)
    x = random.randint(-250, 200)
    y = random.randint(150, 250)
    alien.setposition(x,y)
    

# Speed of Alien
alienspeed = 15

# laser speed
laser = turtle.Turtle()
laser.shape('rocket.gif')
laser.penup()
laser.speed(0)
laser.setheading(90)
laser.shapesize(0.5, 0.5)
laser.hideturtle()

# Speed of laser
laserspeed = 30

# define laser state
ready = ('ready to fire')
fire = ('laser is firing')
laserstate = 'ready'

# move player left and right
def move_left():
    x = player.xcor()
    x -= speed_player
    if x < - 285:
        x = - 285
    player.setx(x)

def move_right():
    x = player.xcor()
    x += speed_player
    if x > 275:
        x = 275
    player.setx(x)

# Laser definition
def fire_laser():
    #declare laser state to global in case it needs change
    global laserstate
    if laserstate == 'ready':
        laserstate = 'fire'
        
# move laser just above player
        x = player.xcor()
        y = player.ycor() + 10
        laser.setposition(x, y)
        laser.showturtle()

# defining collision
def Collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 50:
        return True
    else:
        return False
    
# key bindings
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_laser, 'space')

# main loop of game
while True:

    for alien in aliens:
        #move alien
        x = alien.xcor()
        x += alienspeed
        alien.setx(x)
    # enemy movement
        if alien.xcor() > 255:
            for a in aliens:
                y = a.ycor()
                y -= 40
                a.sety(y)
            #Change alien Direction
            alienspeed*= -1
        if alien.xcor() < -255:
            for a in aliens:
                y = a.ycor()
                y -= 40
                a.sety(y)
            #Change alien Direction
            alienspeed*= -1

            # move laser
        if laserstate == 'fire':
            y = laser.ycor()
            y+= laserspeed
            laser.sety(y)

         # see if laser has reached the top
        if laser.ycor() > 275:
            laser.hideturtle()
            laserstate = 'ready'
            
    # check for a collision between laser and enemy
        if Collision(laser, alien):
            # reset the laser
            laser.hideturtle()
            laserstate = 'ready'
            laser.setposition(0, -400)
            #reset alien
            x = random.randint(-250, 200)
            y = random.randint(200, 250)
            alien.setposition(x,y)
            #Update score
            score += 10
            scorestr = 'Score: %s' %score
            scoreboard.clear()

            scoreboard.write(scorestr, False, align='left', font=('Arial', 18, 'normal'))
        if alien.ycor() < -250:
            for alien in aliens:
                alien.hideturtle()
            player.hideturtle()
            laser.hideturtle()
            Gameover = turtle.Turtle()
            Gameover.speed(0)
            Gameover.color('green')
            Gameover.penup()
            Gameover.setposition(0, 0)
            Gameoverstr = 'GAME OVER'
            Gameover.write(Gameoverstr, False, align='center', font=('Arial', 60, 'normal'))
            Gameover.hideturtle()
            print('Game Over')
            break


    # When alien kills player
        if Collision(player, alien):
            for alien in aliens:
                alien.hideturtle()
            player.hideturtle()
            laser.hideturtle()
            Gameover = turtle.Turtle()
            Gameover.speed(0)
            Gameover.color('green')
            Gameover.penup()
            Gameover.setposition(0, 0)
            Gameoverstr = 'GAME OVER'
            Gameover.write(Gameoverstr, False, align='center', font=('Arial', 60, 'normal'))
            Gameover.hideturtle()
            print('Game Over')
            break
    else:
        continue

    break
False





