import random
a=["rock", "paper","scissors"]
Player_choise=input("Player:-")
Computer_choise=random.choice(a)
print("Computer:-",Computer_choise)
if Player_choise==Computer_choise :
    print("play again")
elif Player_choise=="rock" and Computer_choise=="scissors":
    print("Player wins  π₯") 
elif Player_choise=="rock" and Computer_choise=="paper":
    print("Computer wins π₯")     
elif Player_choise=="scissors" and Computer_choise=="rock":
    print("Computer wins π₯")    
elif Player_choise=="scissors" and Computer_choise=="paper":
    print("Player wins π₯")
elif Player_choise=="paper" and Computer_choise=="scissors":
    print("Computer wins π₯")
if Player_choise=="paper" and Computer_choise=="rock":
    print("Player winsπ₯")             


