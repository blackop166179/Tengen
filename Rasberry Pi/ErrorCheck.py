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