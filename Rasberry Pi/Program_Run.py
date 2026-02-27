import Tengen_Brain

LA = 5
LB = 4
LC = 1

Tengen_Brain.ready()

Tx, Ty, aC = Tengen_Brain.errorCheck(LA, LB, LC)

aA, oaA = Tengen_Brain.Target_Lock(Tx,Ty,aC, 1, LA, LB, LC)

aB, aD = Tengen_Brain.Target_Lock(Tx,Ty,aC, 0, LA, LB, LC)

dA, dB, dC = Tengen_Brain.angle_change(aA,aB,aC,oaA)


#send to arduino
print (aA)
print (aB)
print (aC)
print (dA)
print (dB)
print (dC)

