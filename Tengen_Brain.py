import math
import json
import ErrorCheck


with open ('Tengen_Memory1.json', 'r') as f:
  data = json.load(f)
  CaA = data['CaA']
  CaB = data['CaB']
  CaC = data['CaC']

with open ('Tengen_Memory2.json', 'w') as GVAL:        
  json.dump({'Tx': 0, 'Ty': 0, 'aC': 90, 'Tic': 0}, GVAL)

LA = 5
LB = 4
LC = 1

Tx, Ty, aC = ErrorCheck.errorCheck(LA, LB, LC)

def Target_Lock (Tx, Ty, aC, AoB):

  #Find PB (Bx,By)
  if aC < 0:
    Bx = Tx - math.cos(aC) * LC
  else:
    Bx = Tx + math.cos(aC) * LC
    #aC = aC - 90

  if abs(aC) <= 90:
    By = Ty + math.sin(aC) * LC
  else:
    By = Ty - math.sin(aC) * LC
    #aC = aC - 90 

  PB = (Bx,By)

  #find LD
  LD = math.sqrt((Bx**2)+(By**2))

  #find angles of Triangle BAD
  aD = math.degrees(math.acos(((LB**2)+(LA**2)-(LD**2))/(2*LA*LB)))
  taB = math.degrees(math.acos(((LD**2)+(LA**2)-(LB**2))/(2*LA*LD)))
  taA = math.degrees(math.acos(((LD**2)+(LB**2)-(LA**2))/(2*LB*LD)))

  #altitude of BAD 
  Al = LB * math.sin(taA)
  BoD = LB * math.cos(taA)
  AlDx = Bx - (Bx * (BoD/LD))
  AlDy = By - (By * (BoD/LD))

  PAlD = (AlDx,AlDy)

  #find PA
  #line of reflection is y = (-Bx/By)x 
  M = -Bx/By
  PAx = AlDx - Al/math.sqrt(1+M**2)
  PAy = AlDy + Al/math.sqrt(1+M**2)
  oPAx = AlDx + Al/math.sqrt(1+M**2)
  oPAy = AlDy - Al/math.sqrt(1+M**2)

  #check if work
  if oPAy<0:
    Y = 1
    aB = aD
  elif PAy<0:
    Y = 2
    aB = aD
  elif PAy>0 and oPAy>0:
    Y = 3
    aB = aD

  oaA = math.degrees(math.cos(oPAy/LA))
  aA = math.degrees(math.cos(PAy/LA))
  
  #decicde oututs
  if AoB == 1:
    if Y == 1:
      return(aA, None)
    elif Y == 2:
      return(oaA, None)
    elif Y == 3:
      return(aA, oaA)
  
  elif AoB == 0:
    return(aB,aD)
  del(PAx,PAy,oPAx,oPAy,Bx,By,PB,LD,aD,taB,taA,Al,BoD,AlDx,AlDy,PAlD,M)
  


def angle_change (CaA, CaB, CaC, aA, aB, aC, oaA):
  #calculate changes
  dA = CaA - aA
  dB = CaB - aB
  dC = CaC - aC

  #decide best option for aA
  if oaA is not None:
    doA = CaA - oaA
    if abs(doA) < abs(dA):
      dA = doA
  del (CaA, CaB, CaC, aA, aB, aC, oaA, doA)
  return(dA, dB, dC)

aA, oaA = Target_Lock(Tx,Ty,aC, 1)

aB, aD = Target_Lock(Tx,Ty,aC, 0)

dA, dB, dC = angle_change(CaA,CaB,CaC,aA,aB,aC,oaA)


#send to arduino
print (aA)
print (aB)
print (aC)
print (dA)
print (dB)
print (dC)


with open ('Tengen_Memory1.json', 'w') as f:
  json.dump({'CaA': aA, 'CaB': aB, 'CaC': aC}, f)