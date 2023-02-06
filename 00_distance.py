#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5



# TODO здесь заполнение словаря
print('enter x1')
x1 = int(input())
print('enter x2')
x2 = int(input())
print('enter y1')
y1 = int(input())
print('enter y2')
y2 = int(input())
distances = {((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5}
print(distances)




