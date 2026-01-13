import sys
import math

LA = 5
LB = 4
LC = 1

print("Input Target X Value")
Tx = int(input())
print("Input Target Y Value")
Ty = int(input())
print("Input desired angle for arm C to be")
aC = int(input())

# Domain and Range Error check
Xmax = LA + LB + LC
if Tx > Xmax:
  print("Domain error. target X value too big.")
   print("exiting, retry")
  sys.exit()
Ymax = math.sin(math.acos(Tx/Xmax))*Xmax
if Ty > Ymax:
  print("Range error. target Y value too big.")
  print("exiting, retry")
  sys.exit()

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
  YN = 1
  aB = aD
else:
  YN = 0
  aB = 360 - aD
#optional inversions later

#find aA, gonna cause issues ngl
if YN == 0:
  aA = math.degrees(math.cos(PAy/LA))
elif YN == 1:
  aA = math.degrees(math.cos(oPAy/LA))
  
