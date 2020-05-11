# This is just a module, you don't run standalone, it will just show a error
# 

#List Files Ease
listtxt="list.txt"
#folder
folder="swicons/"

#Awakaned
Awakened="Awakened/"
#Second Awakening
SecondAwakened="SecondAwakened/"
#Normal
Normal="Normal/"

#Fire
Fire="Fire/"
#Wind
Wind="Wind/"
#Water
Water="Water/"
#Dark
Dark="Dark/"
#Light
Light="Light/"

#AngelMons
Angelmon="AngelMon/"
#RuneTypes
RuneType="RuneType/"

#Stars
Star="Star"
#Symbols
Symbol="Symbol"

#Function createmonlist
def createmonlist(monstr):
    x=open(monstr+listtxt,"r")
    #gt = go through
    listgt= x.readlines()
    listx=[]
    for i in listgt:
        i=i.rstrip("\n")
        listx.append(monstr+i)
    x.close()
    return  listx

#Creating Mon Lists(Don't change anything please)
#Assigning Normals
FireMons=createmonlist(folder+Normal+Fire)
WaterMons=createmonlist(folder+Normal+Water)
WindMons=createmonlist(folder+Normal+Wind)
LightMons=createmonlist(folder+Normal+Light)
DarkMons=createmonlist(folder+Normal+Dark)
#Assinging Awakenings
AwakenedFireMons=createmonlist(folder+Awakened+Fire)
AwakenedWaterMons=createmonlist(folder+Awakened+Water)
AwakenedWindMons=createmonlist(folder+Awakened+Wind)
AwakenedLightMons=createmonlist(folder+Awakened+Light)
AwakenedDarkMons=createmonlist(folder+Awakened+Dark)
#Assinging Second Awakenings
SecondAwakenedFireMons=createmonlist(folder+SecondAwakened+Fire)
SecondAwakenedWaterMons=createmonlist(folder+SecondAwakened+Water)
SecondAwakenedWindMons=createmonlist(folder+SecondAwakened+Wind)
SecondAwakenedLightMons=createmonlist(folder+SecondAwakened+Light)
SecondAwakenedDarkMons=createmonlist(folder+SecondAwakened+Dark)
#Assigning AngelMons
AngelMonsFire=createmonlist(folder+Angelmon+Fire)
AngelMonsWater=createmonlist(folder+Angelmon+Fire)
AngelMonsWind=createmonlist(folder+Angelmon+Fire)
AngelMonsLight=createmonlist(folder+Angelmon+Fire)
AngelMonsDark=createmonlist(folder+Angelmon+Fire)
#Assigning RuneTypes
