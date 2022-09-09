#Simulation of a rocket launch just for fun
import time

def Launch_Countdown(length_of_countdown):
    while(length_of_countdown != 0):
        print (length_of_countdown)
        time.sleep(1)
        length_of_countdown-=1
    print("LIFT OFF")

def Assemble_Rocket(propulsionForce=0,mass=0,fuel=0,depletionRate=0):
    current_Configuration = {
        "force": propulsionForce,
        "fuel":fuel,
        "mass":mass,
        "depletionRate":depletionRate
    }
    return current_Configuration

def EditSpaceCraft(rocket):

    return rocket


def Launch():
    rocket = Assemble_Rocket(109.8,20,100,1)
    Launch_Countdown(2)
    print(calculateDistance(rocket,0,100))
    print(sumDistance(rocket))

def Main_Menu():
    choice = input("launch or edit spacecraft:\n")
    if choice == 'launch':
        Launch()
    elif choice == 'edit spacecraft':
        EditSpaceCraft()
    ##elif choice ==

if __name__== '__main__':
    Main_Menu()