#!/usr/bin/env python
# coding: utf-8

# In[1]:


#draw_word jolly using turtle libraries
import turtle
wn = turtle.Screen()
#providing the title name 
wn.title("JOLLY")
#setting the backgroud color
wn.bgcolor("black")
t=turtle.Turtle()
t.shape("turtle")
t.penup()
#declaring the position of turtle to start the drawing by using the Plot X-axis & y-axis
t.setpos(-150,50)
#drawing the letter "j"
t.pendown()
t.pensize(20)
t.speed(0)
t.pencolor("purple")
t.fd(100)
t.bk(50)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(30)
t.penup()
t.setpos(-50,50)
t.goto(5,-25)
#drawing the letter "O"
t.pendown()
t.pensize(20)
t.pencolor("purple")
t.speed(1)
t.circle(30)
t.penup()
#drawing the letter "l"
t.setpos(30,50)
t.goto(40,-50)
t.pendown()
t.pensize(20)
t.pencolor("purple")
t.speed(1)
t.fd(100)
t.bk(100)
t.rt(90)
t.fd(50)
t.penup()
#drawing the letter "l"
t.setpos(60,60)
t.goto(115,-50)
t.pendown()
t.pensize(20)
t.pencolor("purple")
t.speed(1)
t.left(90)
t.fd(100)
t.bk(100)
t.rt(90)
t.fd(50)
t.penup()
#drawing the letter "y"
t.setpos(185,50)
t.pendown()
t.pensize(20)
t.pencolor("purple")
t.speed(1)
t.rt(60)
t.fd(70)
t.lt(120)
t.fd(70)
t.bk(115)
t.penup()
t.setpos(250,-80)
t.pendown()
t.pensize(5)
t.pencolor("lime")
t.circle(250)
t.penup()
t.setpos(100,-130)
t.pendown()
t.pencolor("red")
t.write("JOKER", align="CENTER", font=("Dades", 40))
t.penup()
t.hideturtle()
wn.exitonclick()


# In[ ]:




