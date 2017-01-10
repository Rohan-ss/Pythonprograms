import random
import atexit

def quit_gracefully():
    print ('Bye')


user=0
comp=0

try:
    points = input("Enter How many points are required to win ?")
    atexit.register(quit_gracefully)
    while user!=points or comp!=points:
        player = input("Choice ((R)ock/(P)aper/(S)cissors): ");
        player = player.lower();
        while (player != "rock" and player != "paper" and player != "scissors"):
                print(player);
                player = input("That choice is not valid.\nEnter your choice ((R)ock/(P)aper/(S)cissors): ");
                player = player.lower();

        computerInt = random.randint(0,2);
        if (computerInt == 0):
                computer = "Rock";
        elif (computerInt == 1):
                computer = "Paper";
        elif (computerInt == 2):
                computer = "Scissors";
        else:
                computer = "Huh? Error...";


        if (player == computer):
                result ="Draw"
        elif (player == "rock"):
                if (computer == "paper"):
                        result ="Computer wins!"
                else:
                        result ="You win!"
        elif (player == "paper"):
                if (computer == "rock"):
                        result ="You win!"
                else:
                        result ="Computer wins!"
        elif (player == "scissors"):
                if (computer == "rock"):
                        result ="Com3puter wins!"
                else:
                        result ="You win!"

        if result == "You win!" :
            user=user+1    
        else :
            comp = comp+1

        print("Your choice: " + player + "\tComputer choice: " + computer +"\t"+result);
        if user==points or comp==points :
            print("Final Score :  Human ",user ,"\tComputer ",comp);
            
        else :
            print("Score :  Human ",user ,"\tComputer ",comp);
            
        
            
            
except EOFError:
    pass
            
