import random
import re


stamina=10
alive="true"
def report(stamina):
    if stamina>8:
        print("The alien is strong! It resists your pathetic attack!")
    elif stamina>5:
        print("With a loud grunt, the alien stands firm.")
    elif stamina>3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    else:
        print ("The alien is certain to fall soon! It staggers and reels!") 
def fight(stam):
    response=input("enter your response:-")
    if "hit" in response or "attack" in response: 
        less = random.randint(0, stam)   
        stam-=less
        report(stam)
    elif "fight" in response:
        print ("Fight how? You have no weapons, silly space traveler!")
    else:
        print ("The alien zaps you with its powerful ray gun!")
        return("true")
    return("false") 
alive=fight(stamina)
if alive=="true":
    print ("\nThe alien lives on, and you, sadly, do not.\n")
else:
     print ("\nThe alien has been vanquished. Good work!\n")

# Iss program ko sahi kar ke file submit karo.
               
