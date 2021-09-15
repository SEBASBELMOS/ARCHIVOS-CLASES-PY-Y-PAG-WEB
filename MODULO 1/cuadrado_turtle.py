# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 13:27:31 2021

@author: sebasbelmos
"""

import turtle

t = turtle.Turtle()

def cuadrado(l):
    t.forward(l)
    t.left(90)
    t.forward(l)
    t.left(90)
    t.forward(l)
    t.left(90)
    t.forward(l)

t.penup()
t.forward(50)
t.pendown()
cuadrado(100)
t.penup()
t.left(180)
t.forward(200)
t.left(180)
t.pendown()
cuadrado(100)

turtle.done()
turtle.getscreen()._root.mainloop()