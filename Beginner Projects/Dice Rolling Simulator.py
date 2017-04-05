#!python 2
#https://github.com/Vinay26k
import random
import sys
def Exit():
    print "You have selected to Stop the Game"
    sys.exit()
def DiceRoll():
    print random.randint(1,6)
    
print "1: To Roll \t2:To Exit"
while(1):
    options = { 1: DiceRoll, 2: Exit }
    options[input()]()
    print "Wanna try again ?! 1: To Roll \t2:To Exit"
    

