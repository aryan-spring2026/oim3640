#for i in range(4, 1, -1): 
        #print("Iteration:", i)
        #print("Square:", i * i)
        #print()

#x = 10

#def foo():
    #message = "Hello"
    #x = 5
    #return x

#print(foo())
#print(x)
#print('message')

#Draw a square
#"""
#🧱🧱🧱🧱
#🧱🧱🧱🧱
#🧱🧱🧱🧱
#🧱🧱🧱🧱
#"""

#def draw_square(size):
 #   for i in range(size):
  #      print('🧱' * size)
   # print()

#draw_square(4)

#"""
#Create a function to draw a triangle
#🧱
#🧱🧱
#🧱🧱🧱
#🧱🧱🧱🧱
#"""

#def draw_triangle(rows):
 #   for i in range(rows):
  #      print('🧱' * (i + 1))
   #     print()
    
#draw_triangle(4)

"""
Draw a triangle like this (size = 5)

    #        4 spaces + 1 # = 5      5-0-1 = 4
   ##        3 spaces + 2 # = 5      5-1-1 = 3
  ###        2 spaces + 3 # = 5      5-2-1 = 2
 ####        1 space + 4 # = 5       5-3-1 = 1
#####        0 space + 5 # = 5       5-4-1 = 0

for i in range(size):
In row i, how many spaces are there? i - 1

how many #s are there? i + 1
"""

def draw_triangle(size):
    for i in range(size):
        print(" " * (size - i - 1) + "#" * (i + 1))

draw_triangle(5)