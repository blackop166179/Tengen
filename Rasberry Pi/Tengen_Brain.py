import math
import json

def errorCheck(LA, LB, LC):
    with open ('Tengen_Memory2.json', 'r') as GVAL:
        data = json.load(GVAL)
        Tic = data['Tic']
    while True:
        try:
            if Tic == 0:  
                Tx = float(input("input x coordinate"))
                Ty = float(input("input y coordinate"))
                #aC = float(input("input angle of incidence in degrees"))
                aC = 90

            else:
                with open ('Tengen_Memory2.json', 'r') as GVAL:
                    data = json.load(GVAL)
                    Tx = data['Tx']
                    Ty = data['Ty']
                    aC = data['aC']
                break

             #bad value check

            if Tx < 0 or Ty < 0:
                print("Invalid input. Please enter positive values.")
                print("reebooting")
                raise ValueError("Invalid input. Please enter positive values.")

            # Additional geometric validity checks (By == 0, LD == 0, triangle inequality)
            eps = 1e-9
            rad = math.degrees(aC)
            # compute prospective PB (Bx,By) using same branching logic as later
            if aC < 0:
                Bx_check = Tx - math.cos(rad) * LC
            else:
                Bx_check = Tx + math.cos(rad) * LC

            if abs(aC) <= 90:
                By_check = Ty + math.sin(rad) * LC
            else:
                By_check = Ty - math.sin(rad) * LC

            if abs(By_check) < eps:
                raise ValueError("Invalid input. By is zero (reflection line undefined).")
            LD2 = Bx_check**2 + By_check**2
            if LD2 < eps:
                raise ValueError("Invalid input. PB at origin (LD=0) causes degenerate triangle.")
            # triangle inequality on LD^2 to ensure acos domain safety
            min_ld2 = (LA - LB)**2
            max_ld2 = (LA + LB)**2
            if LD2 < min_ld2 - eps or LD2 > max_ld2 + eps:
                raise ValueError("Domain error. target creates invalid triangle.")
            # Domain and Range Error check
            Xmax = LA + LB + LC
            if Tx > Xmax:
                raise ValueError("Domain error. Target X value too big.")
            Ymax = math.sin(math.acos(Tx/Xmax))*Xmax
            if Ty > Ymax:
                raise ValueError("Range error. Target Y value too big.")

            
            with open ('Tengen_Memory2.json', 'w') as GVAL:
                json.dump({'Tx': float(Tx), 'Ty': float(Ty), 'aC': float(aC), 'Tic': 1}, GVAL)
            break 
        except ValueError:
            print("Rebooting")
    del(By_check, Bx_check, eps, rad, Xmax, Ymax, min_ld2, max_ld2)
    return Tx, Ty, aC

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

  with open ('Tengen_Memory1.json', 'r') as f:
    data = json.load(f)
    CaA = data['CaA']
    CaB = data['CaB']
    CaC = data['CaC']
  #calculate changes
  dA = CaA - aA
  dB = CaB - aB
  dC = CaC - aC

  #decide best option for aA
  if oaA is not None:
    doA = CaA - oaA
    if abs(doA) < abs(dA):
      dA = doA
  
  with open ('Tengen_Memory1.json', 'w') as f:
    json.dump({'CaA': aA, 'CaB': aB, 'CaC': aC}, f)
  del (CaA, CaB, CaC, aA, aB, aC, oaA, doA)
  return(dA, dB, dC)

