u= "Object Distance (u)"
f="Focal Length (f)"
v="Image Distance (v)"
a= "yes"
b= "no"
y = "LENS FORMULA"
x = "TRANSFORMER FORMULA" 
w= "POWER OF LENS" 
v = "TRANSFORMER CURRENT"

Vs = "Secondary Voltage"
Vp = " Primary Voltage"
Ns = "Number of turns in Secondary "
Np= "Number of turns in Primary"







print("======================================================")
print("      PHYSICS ALL EQUATIONS  ")
print("======================================================")
print(" \n DID YOU SUBSRIBE TO @AADI_FX222 ?")
answer= input("\na.yes / \nb.no=").lower()

if answer == b:
    print( " PLEASE SUPPORT")

else:
    print(" WHAT PROBLEM ARE YOU TRYING TO SOLVE?")
    print("======================================================")
    print("======================================================")
formula= input("\n1.LENS FORMULA( 1/f = 1/v - 1/u )|\n2. JOULE S LAW ( H = I^2Rt) | \n3.TRANSFORMER FORMULA (Vs / Vp = Ns / Np)|\n4. POWER OF LENS |\n5.TRANSFORMER CURRENT(Vs / Vp = Ip / Is)")
print("======================================================")
print("======================================================")

if  formula == x :
    print("======================================================")
    print("======================================================")
    print(" \n  Vs = (Secondary Voltage)  \n Vp =(Primary Voltage) \n  Ns = (Number of turns in Secondary ) \n Np =  (Number of turns in Primary) ")

elif formula == y :
    print("======================================================")
    print("======================================================")
    print(" 1.f = (vu) / (u - v)|\n 2.v = (uf) / (f + u)|\n 3.u = (fv) / (f - v)")
    print (" \n    Object Distance (u)  \n    Image Distance (v)\n Focal Length (f) ")
    print("======================================================")
    
    selection = input(" what do you want to find out ? u/v/f").strip().lower()
    if selection == "f":
        u_val = int(input(" WHAT IS YOUR OBJECT DISTANCE (u)?="))
        v_val = int(input(" WHAT IS YOUR DISTANCE OF IMAGE(v)?="))
        f_val = (v_val * u_val) / (u_val - v_val)
        print("u=",u_val)
        print("v'=",v_val)
        
        print(" FOCAL LENGTH IS :", f_val)
        print("======================================================")
        print("======================================================")

elif selection == "v":
    u_val = int(input(" WHAT IS YOUR OBJECT DISTANCE ?(u)="))
    f_val = int(input(" WHAT IS YOUR FOCAL LENGTH?(f)="))
    v_val = (u_val * f_val) / (f_val + u_val)
print("u=",u_val)
print("f=",f_val)
    print("IMAGE DISTANCE IS:", v_val)

elif selection == "u":
    f_val = int(input(" WHAT IS YOUR FOCAL LENGTH?(f)="))
    v_val = int(input(" WHAT IS YOUR DISTANCE OF IMAGE(v)?="))
    u_val = (f_val * v_val) / (f_val - v_val)
    print(" OBJECT DISTANCE IS :", u_val)
    print("======================================================")
    print("======================================================")   
    selection = input(" what do you want to find out ? (Vs/Vp/Ns/Np)").strip().lower()
    if selection == "vs":
        Vp_val = int(input(" WHAT IS PRIMARY VOLTAGE (Vp)?"))
        Ns_val = int(input(" WHAT IS NUMBER OF TURNS IN SECONDARY  (Ns)?"))
        Np_val = int(input(" WHAT IS NUMBER OF TURNS IN PRIMARY (Np)?"))
        Vs_val = (Ns_val * Vp_val) / Np_val
        print(" SECONDARY VOLTAGE IS :", Vs_val)
    elif selection == "vp":
        Vs_val = int(input(" WHAT IS SECONDARY VOLTAGE ?(Vs)?"))
        Np_val = int(input(" WHAT IS NUMBER OF TURNS IN PRIMARY (Np)?"))
        Ns_val = int(input(" WHAT IS NUMBER OF TURNS IN SECONDARY  (Ns)?"))
        Vp_val = (Vs_val * Np_val) / Ns_val
        print(" PRIMARY VOLTAGE IS :", Vp_val)
    elif selection == "ns":
        Vs_val = int(input(" WHAT IS SECONDARY VOLTAGE ?(Vs)?"))
        Np_val = int(input(" WHAT IS NUMBER OF TURNS IN PRIMARY (Np)?"))
        Vp_val = int(input(" WHAT IS PRIMARY VOLTAGE (Vp)?"))
        Ns_val = (Vs_val * Np_val) / Vp_val
        print(" NUMBER OF TURNS IN SECONDARY IS :", Ns_val)
    elif selection == "np":
        Ns_val = int(input(" WHAT IS NUMBER OF TURNS IN SECONDARY  (Ns)?"))
        Vp_val = int(input(" WHAT IS PRIMARY VOLTAGE (Vp)?"))
        Vs_val = int(input(" WHAT IS SECONDARY VOLTAGE ?(Vs)?"))
        Np_val = (Ns_val * Vp_val) / Vs_val
        print(" NUMBER OF TURNS IN PRIMARY:", Np_val)
