import tkinter as tk

app=tk.Tk()
app.title("Dompet Digital")

saldo=500000

label=tk.Label(app,text=f"Saldo: Rp {saldo}")
label.pack()

def cek_saldo():
    label.config(text=f"Saldo: Rp {saldo}")

btn=tk.Button(app,text="Cek Saldo",command=cek_saldo)
btn.pack()

app.mainloop()