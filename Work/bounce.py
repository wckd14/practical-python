# bounce.py
#
# Exercise 1.5

height = 100
rebound = 3/5

for i in range(10):
	print(i+1,round(rebound*height,4))
	height = rebound*height
	
