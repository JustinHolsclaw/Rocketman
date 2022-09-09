

def Calculate_Current_Mass():
    current_rocket = Assemble_Rocket()
    current_mass = current_rocket.get("Propulsion_System")

def Calculate_Profit():
    pass

def calculateDistance(rocket,initialVelocity=0,time=0):
    a=calculateAcceleration(rocket)
    vi=initialVelocity*time  
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