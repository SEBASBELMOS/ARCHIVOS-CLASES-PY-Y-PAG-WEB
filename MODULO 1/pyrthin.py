# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:21:50 2021

@author: sebasbelmos
"""

import turtle

t = turtle.Turtle()

def triangulo(l1):
    t.left(60)
    t.forward(90)
    t.back(90)
    t.left(90)
    t.left(90)
    t.left(90)
    
l = int(input("Digite la altura del rectangulo "))

triangulo(l)