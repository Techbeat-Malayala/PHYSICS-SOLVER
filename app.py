import sys
import tkinter as tk
from tkinter import messagebox
except ModuleNotFoundError
    print("\n" + "="*50)
    print("❌ ERROR: Tkinter library is missing on your system!")
    print("="*50)
    print("To fix this, run the command based on your OS:")
    print("🔹 Linux (Ubuntu/Kali): sudo apt install python3-tk")
    print("🔹 Mac (Homebrew):     brew install python-tk")
    print("🔹 Windows:            Re-install Python and check 'tcl/tk and IDLE'")
    print("="*50 + "\n")
    sys.exit(1)
root = tk.Tk()
root.title("🌌 Physics Solver Dashboard")
root.geometryroot.geometry("400x800")
root.configure(bg="#1e1e2e") 
title_label = tk.Label(root, text="🌌 Physics Solver Engine", font=("Arial", 18, "bold"), fg="#cdd6f4", bg="#1e1e2e")
title_label.pack(pady=15)

lens_frame = tk.LabelFrame(root, text=" 🔍 Thin Lens Calculator ", font=("Arial", 12, "bold"), fg="#a6e3a1", bg="#313244", bd=2, padx=10, pady=10)
lens_frame.pack(fill="x", padx=20, pady=10)

tk.Label(lens_frame, text="Object Distance (u in cm):", fg="#cdd6f4", bg="#313244").grid(row=0, column=0, sticky="w", pady=2)
entry_u = tk.Entry(lens_frame, bg="#45475a", fg="white", insertbackground="white")
entry_u.grid(row=0, column=1, pady=2, padx=5)

tk.Label(lens_frame, text="Image Distance (v in cm):", fg="#cdd6f4", bg="#313244").grid(row=1, column=0, sticky="w", pady=2)
entry_v = tk.Entry(lens_frame, bg="#45475a", fg="white", insertbackground="white")
entry_v.grid(row=1, column=1, pady=2, padx=5)

lens_result = tk.Label(lens_frame, text="Result will appear here...", fg="#f9e2af", bg="#313244", font=("Arial", 10, "italic"))
lens_result.grid(row=3, columnspan=2, pady=8)

def solve_lens():
    try:
        u = float(entry_u.get())
        v = float(entry_v.get())
        if v == 0 or u == 0 or v == u:
            lens_result.config(text="Error: Division by zero.", fg="#f38ba8")
            return
        inv_f = (1 / v) - (1 / u)
        f = 1 / inv_f
        lens_result.config(text=f"Focal Length (f) = {round(f, 2)} cm", fg="#a6e3a1")
    except ValueError:
        lens_result.config(text="Error: Enter valid numbers.", fg="#f38ba8")

btn_lens = tk.Button(lens_frame, text="Calculate f", command=solve_lens, bg="#89b4fa", fg="#11111b", font=("Arial", 10, "bold"), activebackground="#b4befe")
btn_lens.grid(row=2, columnspan=2, pady=5, sticky="we")


# --- 3. TRANSFORMER CALCULATOR (ട്രാൻസ്ഫോർമർ ഫോർമുല വിഭാഗം) ---
trans_frame = tk.LabelFrame(root, text=" ⚡ Transformer Calculator ", font=("Arial", 12, "bold"), fg="#fab387", bg="#313244", bd=2, padx=10, pady=10)
trans_frame.pack(fill="x", padx=20, pady=10)

tk.Label(trans_frame, text="Primary Turns (Np):", fg="#cdd6f4", bg="#313244").grid(row=0, column=0, sticky="w", pady=2)
entry_np = tk.Entry(trans_frame, bg="#45475a", fg="white", insertbackground="white")
entry_np.grid(row=0, column=1, pady=2, padx=5)

tk.Label(trans_frame, text="Secondary Turns (Ns):", fg="#cdd6f4", bg="#313244").grid(row=1, column=0, sticky="w", pady=2)
entry_ns = tk.Entry(trans_frame, bg="#45475a", fg="white", insertbackground="white")
entry_ns.grid(row=1, column=1, pady=2, padx=5)

tk.Label(trans_frame, text="Primary Voltage (Vp):", fg="#cdd6f4", bg="#313244").grid(row=2, column=0, sticky="w", pady=2)
entry_vp = tk.Entry(trans_frame, bg="#45475a", fg="white", insertbackground="white")
entry_vp.grid(row=2, column=1, pady=2, padx=5)

trans_result = tk.Label(trans_frame, text="Result will appear here...", fg="#f9e2af", bg="#313244", font=("Arial", 10, "italic"))
trans_result.grid(row=4, columnspan=2, pady=8)

def solve_trans():
    try:
        np = float(entry_np.get())
        ns = float(entry_ns.get())
        vp = float(entry_vp.get())
        if np <= 0 or ns <= 0:
            trans_result.config(text="Error: Turns must be > 0.", fg="#f38ba8")
            return
        vs = (ns * vp) / np
        trans_result.config(text=f"Secondary Voltage (Vs) = {round(vs, 2)} V", fg="#fab387")
    except ValueError:
        trans_result.config(text="Error: Fill all fields with numbers.", fg="#f38ba8")

btn_trans = tk.Button(trans_frame, text="Calculate Vs", command=solve_trans, bg="#fab387", fg="#11111b", font=("Arial", 10, "bold"), activebackground="#f5e0dc")
btn_trans.grid(row=3, columnspan=2, pady=5, sticky="we")

root.mainloop()

























































































































































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
elif formula == y :
    print("======================================================")
    print("======================================================")

