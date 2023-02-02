# This is a sample Python scrip
# c'est un projet d'aplication avec python qui permet au entreprise d'avoir des reporting sur leur données sans une réél maitrise de l'informatique

#l'iddée est ici de créé un outil similaire a pawer bi mais plus simple a²vec plus de données

import turtle
turtle.title('Sixteen Petals Flower')
turtle.setworldcoordinates(-2000,-2000,2000,2000)

def draw_flower(x,y,tilt,radius):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)

for tilt in range(0,360,30):
    draw_flower(0,0,tilt,1000)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
