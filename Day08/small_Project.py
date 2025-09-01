# Small Game of Snake Gun And Water

import random
choices=["Snake","Gun","Water"]


Again=True

while(Again):
    Player1=input("Choose one between Snake ,gun and water :").capitalize()
    Computer=random.choice(choices)
    print("You chosse =",Player1)
    print("Computer chosse =",Computer)
    if (Player1 == Computer):
        
        print("DRAW!")
    elif(Player1== "Snake" and Computer=="Water") or (Player1=="Gun" and Computer=="Snake") or(Player1=="Water" and Computer=="Gun"):
       
        print("Player Win!")
    else:
       
        print("Computer WIN!")
    Again=input("Wana Play Again ,Choose True & False:").capitalize()
       