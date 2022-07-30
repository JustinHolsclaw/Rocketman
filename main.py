#Simulation of a rocket launch just for fun
import time

def Launch_Countdown(length_of_countdown):
    while(length_of_countdown != 0):
        print (length_of_countdown)
        time.sleep(1)
        length_of_countdown-=1
    print("LIFT OFF")

def Assemble_Rocket():
    current_Configuration = {
        "Propulsion_System": {
            "Name": "Saturn",
            "Mass": 100,
            "Cost": 100,
            "Fuel_Per_Second": 2,
            "Force": 5000
            },
        "Cargo_System": {
            "Name": "Tesla Car",
            "Mass": 2000,
            "Cost": 50000,
            "Reward": 2000000000
        },
        "Payload":{
            "Fuel": {"Type": "Solid",
                     "Mass": 1000},
        }
    }
    return current_Configuration

def Calculate_Current_Mass():
    current_rocket = Assemble_Rocket()
    current_mass = current_rocket.get("Propulsion_System")


def Calculate_Profit():
    pass

def Launch():
    pass

def EditSpaceCraft():
    pass

def Main_Menu(choice):

    while choice != 'exit':
        print(f"Main Menu\n")
        print(f"Launch")
        print(f"Edit Spacecraft")
        print(f"Exit")

        if choice == 'Launch':
            Launch()
        elif choice == 'Edit Spacecraft':
            EditSpaceCraft()
        elif choice == 'Exit':
            exit()
        else:
            print(f"Invalid choice")
    
        


if __name__== '__main__':
    Launch_Countdown(10)