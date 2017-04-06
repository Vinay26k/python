from random import randint
import sys
r = 9
t = 3
def play():
    val = randint(0,r)
    print("You have three tries :D")
    for i in range(t):
        print("Guess the number : ")
        guess = int(raw_input())
        if guess == val:
            print("Hurray!! You got it right :D\n")
            break
        elif guess-val<0: #3-4
            print("It's not that Low, increase value and try again")
        else:
            print("It's not that high, decrease value and try again")
    print("Answer is:"+ str(val)+"\n")
def change():
    print("Enter numbers range:")
    r = int(input())
    print("Enter number of tries:")
    t = int(input())
    return r,t
def Exit():
    print("xXxXxXx End xXxXxXx")
    sys.exit()
print('''
*****************************************************************
*                                                               *
*                                                               *
*                   Guess the Number Game                       *
*#!python 2                                                     *
*#https://github.com/Vinay26k                                   *
*Mini Project                                                   *
*                                                               *
*****************************************************************
''')
print("Default Numbers Range set to : 0-"+ str(r)+"\nTries :" +str(t))
print("Press (1) to Change default settings else (2) to run the game")
if(int(input())==1):
    r,t = change()
while(1):
    print("Default Numbers Range set to : 0-"+ str(r)+"\nTries :" +str(t))
    print("\n1.To Guess \n2.To Exit")
    options = { 1:play, 2:Exit}
    options[int(input())]()
        
