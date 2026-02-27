import json
import Tengen_Brain

LA = 5
LB = 4
LC = 1

with open ('Tengen_Memory2.json', 'w') as GVAL:        
    json.dump({'Tx': 0, 'Ty': 0, 'aC': 90, 'Tic': 0}, GVAL)

Tx, Ty, aC = Tengen_Brain.errorCheck(LA, LB, LC)

aA, oaA = Tengen_Brain.Target_Lock(Tx,Ty,aC, 1)

aB, aD = Tengen_Brain.Target_Lock(Tx,Ty,aC, 0)

dA, dB, dC = Tengen_Brain.angle_change(aA,aB,aC,oaA)


#send to arduino
print (aA)
print (aB)
print (aC)
print (dA)
print (dB)
print (dC)

