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

def calculateDistance(rocket,initialVelocity=0):
    vi=initialVelocity*(fuelConsumption(rocket)/rocket["depletionRate"])
    a=calculateAcceleration(rocket)
    t= calculateTime(rocket)
    t2 = t*t
    return vi+(1/2*a*t2)

def calculateForce(rocket):
    return rocket["force"]-9.8

def calculateMass(rocket):
    return rocket["mass"]

def calculateAcceleration(rocket):
    return calculateForce(rocket)/rocket["mass"]

def calculateTime(rocket):
    return rocket["fuel"]/rocket["depletionRate"]

def fuelConsumption(rocket):
    return rocket["fuel"]/rocket["depletionRate"]

def EditSpaceCraft():
    pass

def Launch():
    rocket = Assemble_Rocket(100,20,100,1)
    Launch_Countdown(10)
    print(calculateDistance(rocket))

def Main_Menu():
    choice = input("launch or edit spacecraft")
    if choice == 'launch':
        Launch()
    elif choice == 'edit spacecraft':
        EditSpaceCraft()
    ##elif choice ==


if __name__== '__main__':
    Main_Menu()