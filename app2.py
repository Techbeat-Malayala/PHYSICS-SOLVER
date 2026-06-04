import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
title_label = tk.Label(root, text ="⚛ Physics Solver Dashboard", font =("Poppins SemiBold",42,), fg = "#060546" )
root.geometry("1400x3200")
title_label = tk.Label(root, text="⚛ Physics Solver ", font=("Arial", 18, "bold"),fg ="#1E293B")
root.configure(bg="#1E293B") 
title_label = tk.Label(root, text="⚛ Physics Solver ", font=("Arial", 18, "bold"),fg ="#FFFFFF",bg = "#1E293B")
title_label.pack(pady=15,padx=10)

lens_frame = tk.LabelFrame(root, text=" 🔍 Lens  formula Calculator ", font=("Poppins SemiBold", 12), fg="#FFFFFF", bg="#313244", bd=2, padx=20, pady=10)
lens_frame.pack(fill="x", padx=5, pady=10)

tk.Label(lens_frame, text="Object Distance (u in cm):", fg="#8B5CF6", bg="#313244").grid(row=0, column=0, sticky="w", pady=2)
entry_u = tk.Entry(lens_frame, bg="#45475a", fg="white", insertbackground="white")
entry_u.grid(row=0, column=1, pady=2, padx=5)

tk.Label(lens_frame, text="Image Distance (v in cm):", fg="#8B5CF6", bg="#313244").grid(row=1, column=0, sticky="w", pady=2)
entry_v = tk.Entry(lens_frame, bg="#45475a", fg="white", insertbackground="white")
entry_v.grid(row=1, column=1, pady=2, padx=5)

lens_result = tk.Label(lens_frame, text="Result will appear here...", fg="#8B5CF6", bg="#313244", font=("Poppins SemiBold", 10, "italic"))
lens_result.grid(row=3, columnspan=2, pady=8)






def solve_lens():
    try:
        u = float(entry_u.get())
        v = float(entry_v.get())
        if v == 0 or u == 0 or v == u:
            lens_result.config(text="Error: Division by zero.", fg="#FFFFFF")
            return
        inv_f = (1 / v) - (1 / u)
        f = 1 / inv_f
        lens_result.config(text=f"Focal Length (f) = {round(f, 2)} cm", fg="#a6e3a1")
    except ValueError:
        lens_result.config(text="Error: Enter valid numbers.", fg="#FFFFFF")

btn_lens = tk.Button(lens_frame, text="Calculate f", command=solve_lens, bg="#d089fa", fg="#11111b", font=("Arial", 10, "bold"), activebackground="#b4befe")
btn_lens.grid(row=2, columnspan=2, pady=5, sticky="we")

trans_frame = tk.LabelFrame(root, text=" ⚡ Transformer Calculator ", font=("Arial", 12, "bold"), fg="#fab387", bg="#313244", bd=2, padx=20, pady=10)
trans_frame.pack(fill="x", padx=15, pady=10)

tk.Label(trans_frame, text="Primary Turns (Np):",font=("Orbitron", 10, "bold"), fg="#cdd6f4", bg="#313244").grid(row=0, column=0, sticky="w", pady=2)
entry_np = tk.Entry(trans_frame, bg="#45475a", fg="white", insertbackground="white")
entry_np.grid(row=0, column=1, pady=2, padx=5)

tk.Label(trans_frame, text="Secondary Turns (Ns):", font=("Orbitron", 10, "bold"), fg="#cdd6f4", bg="#313244").grid(row=1, column=0, sticky="w", pady=2)
entry_ns = tk.Entry(trans_frame, bg="#45475a", fg="white", insertbackground="white")
entry_ns.grid(row=1, column=1, pady=2, padx=5)

tk.Label(trans_frame, text="Primary Voltage (Vp):", font=("Orbitron", 10, "bold"),   fg="#cdd6f4", bg="#313244").grid(row=2, column=0, sticky="w", pady=2)
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

























































































































































