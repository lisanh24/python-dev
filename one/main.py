# # calling my cat names
# catName = []
#
# while True:
#     print("Enter the name of cat : " + str(len(catName)+1) + ' (or enter nothing to stop)' )
#     name = input()
#     if name == '':
#         break
#     catName = catName + [name]
# print("The cat names are :")
# for name in catName:
#     print(' '+name)
from sqlalchemy.sql.functions import random
from sympy import pprint

# # using enumerators:
# import  random
# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for index, item in enumerate(supplies):
#     print(index, item)
#
# print(random.choice(supplies))
# supplies.sort()
# print(supplies)
# supplies.sort(reverse=True)
# print(supplies)


# print(type(('lisan',)))

# name = "Lisan"
# print(id(name))
# age = 19
# print(id(age))

# game of lfe
# Conway's Game of Life
# import random, time, copy
# WIDTH = 60
# HEIGHT = 20
#
# # Create a list of list for the cells:
# nextCells = []
# for x in range(WIDTH):
#     column = [] # Create a new column.
#     for y in range(HEIGHT):
#         if random.randint(0, 1) == 0:
#             column.append('#') # Add a living cell.
#         else:
#             column.append(' ') # Add a dead cell.
#     nextCells.append(column) # nextCells is a list of column lists.
#
# while True: # Main program loop.
#     print('\n\n\n\n\n') # Separate each step with newlines.
#     currentCells = copy.deepcopy(nextCells)
#
#     # Print currentCells on the screen:
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             print(currentCells[x][y], end='') # Print the # or space.
#         print() # Print a newline at the end of the row.
#
#     # Calculate the next step's cells based on current step's cells:
#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             # Get neighboring coordinates:
#             # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
#             leftCoord  = (x - 1) % WIDTH
#             rightCoord = (x + 1) % WIDTH
#             aboveCoord = (y - 1) % HEIGHT
#             belowCoord = (y + 1) % HEIGHT
#
#             # Count number of living neighbors:
#             numNeighbors = 0
#             if currentCells[leftCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-left neighbor is alive.
#             if currentCells[x][aboveCoord] == '#':
#                 numNeighbors += 1 # Top neighbor is alive.
#             if currentCells[rightCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-right neighbor is alive.
#             if currentCells[leftCoord][y] == '#':
#                 numNeighbors += 1 # Left neighbor is alive.
#             if currentCells[rightCoord][y] == '#':
#                 numNeighbors += 1 # Right neighbor is alive.
#             if currentCells[leftCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-left neighbor is alive.
#             if currentCells[x][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom neighbor is alive.
#             if currentCells[rightCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-right neighbor is alive.
#
#             # Set cell based on Conway's Game of Life rules:
#             if currentCells[x][y] == '#' and (numNeighbors == 2 or
# numNeighbors == 3):
#                 # Living cells with 2 or 3 neighbors stay alive:
#                 nextCells[x][y] = '#'
#             elif currentCells[x][y] == ' ' and numNeighbors == 3:
#                 # Dead cells with 3 neighbors become alive:
#                 nextCells[x][y] = '#'
#             else:
#                 # Everything else dies or stays dead:
#                 nextCells[x][y] = ' '
#     time.sleep(1) # Add a 1-second pause to reduce flickering.


#chapter 5:
# mycat = {'size':'fat','color':'gray','disposition':'loud'}
# for k, v in mycat.items():
#     print(k + ' : '+v)

# mycat = {'size':'big','color':'orange','disposition':'loud'}
# for i in mycat.items():
#     print(i)

# using pretty print
# import  pprint
# message = "It was a bright cold day in April, and thr clocks were strikinh thirteen"
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
#
# pprint.pprint(count)


# print("Lisan".upper())
# print(', '.join(["lisan","hossain","Shaed"]))
# print(' '.join(["lisan","hossain","Shaed"]))
# print(' <--> '.join(["lisan","hossain","Shaed"]))
# print('My name is lisan Hossian'.split())
# print('My name is lisan Hossian'.split('s'))
# print('My name is lisan Hossian'.partition('s'))
# print("Lisan".rjust(25,'_'))
# print("Lisan".rjust(15,'_'))
# print("Lisan".rjust(10,'_'))
# print("Lisan".rjust(5,'_'))


# # playing with l and r just:
# for i in range(10,20):
#     print("Lisan".center(i,'_'))

# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
#
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# import pyperclip
#
# sen  = pyperclip.paste()
# print(sen)

# matching regex objects
