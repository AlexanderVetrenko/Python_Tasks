#!/usr/bin/python
# -*- coding: utf-8 -*-
# По двум заданным числам проверить является ли одно квадратом второго

def IsSquare(x,y):
    if y == x**2 or x == y**2: return True
    else: return False

a = int(input('Введите первое целое число '))
b = int(input('Введите второе целое число '))

if IsSquare(a,b): print('Одно из чисел является квадратом второго')
else: print('Введенные числа не соответствуют условию задачи')