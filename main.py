#Simulation of a rocket launch just for fun
import time

from click import launch


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

def calculateDistance(rocket,initialVelocity=0,time=0):
    vi=initialVelocity*(fuelConsumption(rocket)/rocket["depletionRate"])
    a=calculateAcceleration(rocket)
    if time == 0:
        t= calculateTime(rocket)
        t2 = t*t
        return vi+(1/2*a*t2)
    else:
        t2 = time*time
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

def calculateFinalVelocity(rocket, vi=0,t=1):
    vf = vi+calculateAcceleration(rocket)*t
    return vf

def calculateFuel(rocket):
    return rocket["fuel"]-rocket["depletionRate"]

def sumDistance(rocket):
    sum=0
    vi=0
    while rocket["fuel"] >0:
        sum = sum+calculateDistance(rocket,vi,1)
        vi=calculateFinalVelocity(rocket, vi)
        rocket["fuel"]=calculateFuel(rocket)
    return sum

def EditSpaceCraft():
    pass


def Launch():
    rocket = Assemble_Rocket(10.8,20,10,1)
    Launch_Countdown(2)
    print(calculateDistance(rocket))
    print(sumDistance(rocket))

def Main_Menu():
    choice = input("launch or edit spacecraft")
    if choice == 'launch':
        Launch()
    elif choice == 'edit spacecraft':
        EditSpaceCraft()
    ##elif choice ==


if __name__== '__main__':
    Main_Menu()