from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,100):
  move(i)
  turn(9)
  color(colors[i%3])
  
  
for j in range(0,10):
  print(j)
  
