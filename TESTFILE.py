import json

CaC = 6
CaB = 5
CaA = 3

with open ('Tengen_Memory.json', 'r') as f:
  data = json.load(f)


CP = data["Hippocampus"]
CaA = CP["CaA"]
CaB = CP["CaB"]
CaC = CP["CaC"]

with open ('Tengen_Memory.json', 'r') as f:
    data = json.load(f)
    CaA = data["Hippocampus"]["CaA"]
    CaB = data["Hippocampus"]["CaB"]
    CaC = data["Hippocampus"]["CaC"]

print (CaA)
print (CaB)
print (CaC)


