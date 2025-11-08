import pgzrun, random
WIDTH, HEIGHT=800, 500
TITLE="Catch Dr. Robotnik!"
Robotnik=Actor("eggman.png")
Robotnik.pos=random.randint(0, 800), random.randint(0, 500)
score=0
message="Catch the Doctor!"
def draw():
    screen.fill("Blue")
    Robotnik.draw()
    screen.draw.text(message, (10, 10))
    screen.draw.text("score="+str(score), (10, 30))

def on_mouse_down(pos):
    global score, message
    print(pos)
    if Robotnik.collidepoint(pos):
      message="Caught!"
      score+=10
    else:
       message="Oops!"
       score-=5
    Robotnik.pos=random.randint(0, 800), random.randint(0, 500)
pgzrun.go()