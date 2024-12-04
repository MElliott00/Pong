#Pong game


from base64 import b16decode
import turtle

wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Score
score_a = 0
score_b = 0

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .4
ball.dy = .4

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 18, "normal"))


#function moving paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

#Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#main game loop
game_over = False

while not game_over:
    wn.update()
    
    

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #boarder check up
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
       
        
    #border check bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
             

    #bodercheck right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        
    #bodercheck left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        
    #Right paddle ball collision

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
       ball.setx(340)
       ball.dx *= -1
     
       
    #left paddle ball colision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
       ball.setx(-340)
       ball.dx *= -1
       
    #check if player has won
    if score_a == 5 or score_b == 5:
       game_over = True
       if score_a == 5:
           winner = "Player A"
       else:
           winner = "Player B"
       pen.clear()
       pen.write(f"Game Over! {winner} wins!", align="center", font=("Courier", 18, "normal"))
       print(f"Game Over {winner} wins")
     
    #quits program   
    wn.update()
    wn.listen()
    
    
      